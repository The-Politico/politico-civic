from fabric.api import local, task


@task
def migrate_db():
    local('python manage.py migrate')


@task
def collectstatic():
    local('python manage.py collectstatic')


@task
def management(cmd):
    local('python manage.py {0}'.format(cmd))