import server_config

from fabric.api import task
from fabric.state import env
from . import daemons, django, servers

"""
Base configuration
"""
env.user = server_config.SERVER_USER
env.forward_agent = True

"""
Branches

Changing branches requires deploying that branch to a host.
"""


@task
def production():
    env.hosts = server_config.PRODUCTION_SERVERS
    env.roledefs = {
        "east": [server_config.PRODUCTION_SERVERS[0]],
        "west": [server_config.PRODUCTION_SERVERS[1]],
    }


@task
def staging():
    env.hosts = server_config.STAGING_SERVERS
    env.roledefs = {
        "east": [server_config.STAGING_SERVERS[0]],
        "west": [server_config.STAGING_SERVERS[1]],
    }


@task
def master():
    """
    Work on development branch.
    """
    env.branch = "master"


@task
def branch(branch_name):
    """
    Work on any specified branch.
    """
    env.branch = branch_name


@task
def deploy_server():
    servers.checkout_latest()
    servers.restart_service("uwsgi")
