import server_config

from fabric.api import task
from fabric.state import env
from . import servers

"""
Base configuration
"""
env.user = server_config.SERVER_USER
env.forward_agent = True
env.hosts = server_config.SERVERS

"""
Branches

Changing branches requires deploying that branch to a host.
"""

@task
def master():
    """
    Work on development branch.
    """
    env.branch = 'master'


@task
def branch(branch_name):
    """
    Work on any specified branch.
    """
    env.branch = branch_name


@task
def deploy_server():
    servers.checkout_latest()
    servers.restart_service('uwsgi')
