import click
import os

from subprocess import run


@click.group()
@click.version_option()
def cli():
    """
    CLI base function
    """


@cli.group()
def server():
    """Manages server."""


@server.command('launch')
@click.option(
    '--target', default='staging', help='The server environment to target'
)
def server_launch(target):
    """
    Creates a new server through terraform
    """
    os.chdir('terraform/{}'.format(target))
    run(['terraform', 'apply'])


@server.command('setup')
@click.option(
    '--target', default='staging', help='The server environment to target'
)
def server_setup(target):
    """
    Setup an existing server with Fabric
    """
    run(['fab', target, 'servers.setup'])


@server.command('update')
@click.option(
    '--target', default='staging', help='The server environment to target'
)
def server_update(target):
    """
    Update repo on server
    """
    run(['fab', target, 'master', 'servers.checkout_latest'])


@server.command('destroy')
@click.option(
    '--target', default='staging', help='The server environment to target'
)
def server_destroy(target):
    """
    Destroys server architecture using terraform
    """
    os.chdir('terraform/{}'.format(target))
    run(['terraform', 'destroy'])
