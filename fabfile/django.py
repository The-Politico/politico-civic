import server_config

from fabric.api import cd, roles, run, task


@task
@roles("east")
def management(cmd):
    with cd(server_config.SERVER_PROJECT_PATH):
        run("python manage.py {0}".format(cmd))
