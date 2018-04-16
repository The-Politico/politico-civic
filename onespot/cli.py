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
def server_launch():
    """
    Creates a new server through terraform
    """
    os.chdir('terraform')
    run(['terraform', 'apply'])


@server.command('setup')
def server_setup():
    """
    Setup an existing server with Fabric
    """
    run(['fab', 'servers.setup'])

@server.command('update')
def server_update():
    """
    Update repo on server
    """
    run(['fab', 'master', 'servers.checkout_latest'])


@server.command('destroy')
def server_destroy():
    """
    Destroys server architecture using terraform
    """
    os.chdir('terraform')
    run(['terraform', 'destroy'])
