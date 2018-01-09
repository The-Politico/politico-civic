from fabric.api import run, task


@task
def management(cmd):
    run('python manage.py {0}'.format(cmd))
