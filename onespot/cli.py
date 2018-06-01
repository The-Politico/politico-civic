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


@cli.group()
def election():
    """Manages election nights."""


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


@election.command('init')
@click.argument('date')
@click.option('--test', is_flag=True, help='Pass test flag to elex')
@click.option(
    '--target', default='staging', help='The server environment to target'
)
def election_init(date, target, test):
    """
    Initializes election data in the database, sets up necessary config files,
    and bootstraps content in the database.
    """
    if test:
        test_flag = '--test'
    else:
        test_flag = ''

    bootstrap_elex = 'bootstrap_elex {0} {1}'.format(date, test_flag)
    bootstrap_results_config = 'bootstrap_results_config {0}'.format(date)
    bootstrap_content = 'bootstrap_content {0}'.format(date)

    run(['fab', target, 'django.management:{0}'.format(bootstrap_elex)])
    run([
        'fab', target, 'django.management:{0}'.format(bootstrap_results_config)
    ])
    run(['fab', target, 'django.management:{0}'.format(bootstrap_content)])


@election.command('start')
@click.argument('date')
@click.option('--test', is_flag=True, help='Pass test flag to elex')
@click.option('--nobot', is_flag=True, help='Pass no-bot flag to reup')
@click.option(
    '--target', default='staging', help='The server environment to target'
)
def election_start(date, target, test, nobot):
    """
    Starts results and reup processes on the server.
    """
    if test:
        test_flag = '--test'
    else:
        test_flag = ''

    if nobot:
        no_bot_flag = '--nobot'
    else:
        no_bot_flag = ''

    run(['fab', target, 'servers.start_results:{0},{1}'.format(
        date, test_flag
    )])
    run(['fab', target, 'servers.start_reup:{0},{1}'.format(date, no_bot_flag)])


@election.command('stop')
@click.option(
    '--target', default='staging', help='The server environment to target'
)
def election_stop(target):
    """
    Stops results and reup processes on the server.
    """
    run(['fab', target, 'servers.stop_service:results'])
    run(['fab', target, 'servers.stop_service:reup'])


@election.command('finish')
@click.argument('date')
@click.option('--test', is_flag=True, help='Pass test flag to elex')
@click.option(
    '--target', default='staging', help='The server environment to target'
)
def election_finish(date, target, test):
    if test:
        test_flag = '--test'
    else:
        test_flag = ''

    run(['fab', target, 'servers.stop_service:results'])
    run(['fab', target, 'servers.stop_service:reup'])

    get_once = 'get_results {} {} --run_once'.format(date, test_flag)
    reup_once = 'bootstrap_results_db {} {} --tabulated --run_once'.format(
        date, test_flag
    )
    run(['fab', target, 'django.management:{}'.format(get_once)])
    run(['fab', target, 'django.management:{}'.format(reup_once)])


@election.command('zeroes')
@click.argument('date')
@click.option('--test', is_flag=True, help='Pass test flag to elex')
@click.option(
    '--target', default='staging', help='The server environment to target'
)
def election_zeroes(date, target, test):
    if test:
        test_flag = '--test'
    else:
        test_flag = ''

    get_zeroes = 'get_results {} {} --zeroes --run_once'.format(date, test_flag)
    bake = 'bake_elections {}'.format(date)
    run(['fab', target, 'django.management:{}'.format(get_zeroes)])
    run(['fab', target, 'django.management:{}'.format(bake)])


@election.command('replay')
@click.argument('date')
@click.option('--nobot', is_flag=True, help='Pass no-bot flag to reup')
@click.option(
    '--target', default='staging', help='The server environment to target'
)
def election_test_replay(date, target, nobot):
    if nobot:
        no_bot_flag = '--nobot'
    else:
        no_bot_flag = ''

    run(['fab', target, 'servers.start_results:{0},,--replay'.format(date)])
    run(['fab', target, 'servers.start_reup:{0},{1}'.format(date, no_bot_flag)])
