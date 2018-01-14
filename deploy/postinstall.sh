#!/bin/bash

# Restart logs to catch new config
sudo service awslogs restart

source /home/ubuntu/.bash_profile

cd /home/ubuntu/apps/politico-civic/

# Make sure PIPENV is configured correctly
export PIPENV_VENV_IN_PROJECT=1
export PIPENV_IGNORE_VIRTUALENVS=1

pyenv global general
pipenv install &&
pipenv run python manage.py collectstatic --noinput &&
pipenv run python manage.py migrate &&
sudo service politico-civic.uwsgi restart
