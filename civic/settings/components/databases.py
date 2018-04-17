import os

import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env('{0}/../.env'.format(BASE_DIR))

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {}
if 'DATABASE_URL' in os.environ:
    DATABASES['default'] = env.db()
else:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'database',
    }
