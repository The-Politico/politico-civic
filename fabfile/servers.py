#!/usr/bin/env python

"""
Commands work with servers. (Hiss, boo.)
"""

import copy
import logging

from jinja2 import Template

import server_config
from fabric.api import cd, local, put, require, run, settings, sudo, task
from fabric.state import env

logging.basicConfig(format=server_config.LOG_FORMAT)
logger = logging.getLogger(__name__)
logger.setLevel(server_config.LOG_LEVEL)

"""
Setup
"""


@task
def setup():
    """
    Setup servers for deployment.

    This does not setup services or push to S3. Run deploy() next.
    """
    require('branch', provided_by=['master', 'branch'])

    install_node_dependencies()
    create_directories()
    clone_repo()
    checkout_latest()
    install_requirements()
    setup_logs()


@task
def install_node_dependencies():
    """
    Install node and dependencies
    """
    sudo('apt update')
    sudo('apt install nodejs -y')
    sudo('apt install npm -y')
    sudo('apt install nodejs-legacy -y')
    sudo('npm install -g topojson')


@task
def create_directories():
    """
    Create server directories.
    """
    run('mkdir -p %(SERVER_PROJECT_PATH)s' % server_config.__dict__)
    sudo('mkdir -p /etc/uwsgi')
    sudo('mkdir -p /etc/uwsgi/sites')
    sudo('mkdir -p /run/uwsgi')


@task
def clone_repo():
    """
    Clone the source repository.
    """
    run('git clone %(REPOSITORY_URL)s %(SERVER_PROJECT_PATH)s' %
        server_config.__dict__)


@task
def checkout_latest(remote='origin'):
    """
    Checkout the latest source.
    """
    run('cd %s; git fetch %s' % (server_config.SERVER_PROJECT_PATH, remote))
    run('cd %s; git checkout %s; git pull %s %s' %
        (server_config.SERVER_PROJECT_PATH, env.branch, remote, env.branch))


@task
def install_requirements():
    """
    Install the latest requirements.
    """
    with cd('%(SERVER_PROJECT_PATH)s' %
            server_config.__dict__):
        run('source ~/.bash_profile')
        run('pyenv global general')
        run('pipenv install')


@task
def setup_logs():
    """
    Create log directories.
    """
    sudo('mkdir %(SERVER_LOG_PATH)s' % server_config.__dict__)
    sudo('chown ubuntu:ubuntu %(SERVER_LOG_PATH)s' % server_config.__dict__)


@task
def install_crontab():
    """
    Install cron jobs script into cron.d.
    """
    sudo('cp %(SERVER_PROJECT_PATH)s/cronjobs/* /etc/cron.d' %
         server_config.__dict__)


@task
def uninstall_crontab():
    """
    Remove a previously install cron jobs script from cron.d
    """
    sudo('rm /etc/cron.d/%(PROJECT_FILENAME)s' % server_config.__dict__)


def delete_project():
    """
    Remove the project directory. Invoked by shiva.
    """
    run('rm -rf %(SERVER_PROJECT_PATH)s' % server_config.__dict__)


"""
Configuration
"""


def _get_template_conf_path(service, extension):
    """
    Derive the path for a conf template file.
    """
    return 'confs/%s.%s' % (service, extension)


def _get_rendered_conf_path(service, extension):
    """
    Derive the rendered path for a conf file.
    """
    return 'confs/rendered/%s.%s.%s' % (
        server_config.PROJECT_FILENAME, service, extension
    )


def _get_installed_conf_path(service, remote_path, extension):
    """
    Derive the installed path for a conf file.
    """
    return '%s/%s.%s.%s' % (
        remote_path, server_config.PROJECT_FILENAME, service, extension
    )


def _get_installed_service_name(service):
    """
    Derive the init service name for an installed service.
    """
    return '%s.%s' % (server_config.PROJECT_FILENAME, service)


@task
def render_confs():
    """
    Renders server configurations.
    """

    # Copy the server_config so that when we load the secrets they don't
    # get exposed to other management commands
    context = copy.copy(server_config.__dict__)

    for service, remote_path, extension in server_config.SERVER_SERVICES:
        template_path = _get_template_conf_path(service, extension)
        rendered_path = _get_rendered_conf_path(service, extension)

        with open(template_path, 'r') as read_template:

            with open(rendered_path, 'w') as write_template:
                payload = Template(read_template.read())
                write_template.write(payload.render(**context))


@task
def deploy_confs():
    """
    Deploys rendered server configurations to the specified server.
    This will reload nginx and the appropriate uwsgi config.
    """
    render_confs()

    with settings(warn_only=True):
        for service, remote_path, extension in server_config.SERVER_SERVICES:
            rendered_path = _get_rendered_conf_path(service, extension)
            installed_path = _get_installed_conf_path(
                service, remote_path, extension
            )

            a = local('md5 -q %s' % rendered_path, capture=True)
            b = run('md5sum %s' % installed_path).split()[0]

            if a != b:
                logging.info('Updating %s' % installed_path)
                put(rendered_path, installed_path, use_sudo=True)

                if service == 'nginx':
                    sudo('rm /etc/nginx/sites-enabled/%s.nginx.conf' %
                         server_config.PROJECT_FILENAME)
                    sudo('ln -s /etc/nginx/sites-available/%s.nginx.conf'
                         ' /etc/nginx/sites-enabled' %
                         server_config.PROJECT_FILENAME)
                    sudo('service nginx restart')
                elif service == 'uwsgi':
                    service_name = _get_installed_service_name(service)
                    sudo('initctl reload-configuration')
                    sudo('service %s restart' % service_name)
                elif service == 'app':
                    sudo('mkdir /run/uwsgi/')
                    sudo('touch %s' % server_config.UWSGI_SOCKET_PATH)
                    sudo('chmod 777 %s' % server_config.UWSGI_SOCKET_PATH)
                    sudo('chown ubuntu:www-data /run/uwsgi/')
            else:
                logging.info('%s has not changed' % rendered_path)


@task
def nuke_confs():
    """
    DESTROYS rendered server configurations from the specified server.
    This will reload nginx and stop the uwsgi config.
    """
    for service, remote_path, extension in server_config.SERVER_SERVICES:
        with settings(warn_only=True):
            installed_path = _get_installed_conf_path(
                service, remote_path, extension
            )

            sudo('rm -f %s' % installed_path)

            if service == 'nginx':
                sudo('service nginx reload')
            elif service == 'uwsgi':
                service_name = _get_installed_service_name(service)
                sudo('service %s stop' % service_name)
                sudo('initctl reload-configuration')
            elif service == 'app':
                sudo('rm %s' % server_config.UWSGI_SOCKET_PATH)


@task
def start_service(service):
    """
    Start a service on the server.
    """
    service_name = _get_installed_service_name(service)
    sudo('service %s start' % service_name)


@task
def stop_service(service):
    """
    Stop a service on the server
    """
    service_name = _get_installed_service_name(service)
    sudo('service %s stop' % service_name)


@task
def restart_service(service):
    """
    Start a service on the server.
    """
    service_name = _get_installed_service_name(service)
    sudo('service %s restart' % service_name)


@task
def fabcast(command):
    """
    Actually run specified commands on the server specified
    by staging() or production().
    """
    run('cd %s && bash run_on_server.sh pipenv run fab %s %s'
        % (server_config.SERVER_PROJECT_PATH, env.branch, command))
