from fabric.api import local, task


@task
def migrate_db():
    local('python manage.py migrate')