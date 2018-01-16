#!/bin/bash
set -e
# Restart logs to catch new config
sudo service awslogs restart

source /home/ubuntu/.bash_profile

# Move to the project dir... This is important.
cd /home/ubuntu/apps/politico-civic/

# Make sure PIPENV is configured correctly
export PIPENV_VENV_IN_PROJECT=1
export PIPENV_IGNORE_VIRTUALENVS=1

pyenv global general
pipenv install --verbose
pipenv run python manage.py migrate
pipenv run python manage.py collectstatic --noinput
sudo service politico-civic.uwsgi restart
