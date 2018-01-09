import server_config

from fabric.api import cd, run, task


@task
def management(cmd):
    with cd(server_config.SERVER_PROJECT_PATH):
        run('pipenv run python manage.py {0}'.format(cmd))
