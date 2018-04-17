import os

import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env('{0}/../.env'.format(BASE_DIR))

SECRET_KEY = os.getenv('SECRET_KEY', 'secret')
ALLOWED_HOSTS = ['.politicoapps.com', 'localhost']

DEBUG = env('DEBUG')

# HTTPS
SECURE_SSL_REDIRECT = False if DEBUG else True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ROOT_URLCONF = 'civic.urls'

WSGI_APPLICATION = 'civic.wsgi.application'