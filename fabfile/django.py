from fabric import local, task


@task
def migrate_db():
    local('python manage.py migrate')
