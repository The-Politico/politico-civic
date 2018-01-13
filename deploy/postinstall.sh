#!/bin/bash
export PIPENV_VENV_IN_PROJECT=1
export PIPENV_IGNORE_VIRTUALENVS=1
sudo service awslogs restart
cd /home/ubuntu/apps/politico-civic
source /home/ubuntu/.bash_profile
pyenv global general
pipenv install &&
pipenv run python manage.py migrate &&
pipenv run python manage.py collectstatic --noinput &&
sudo service politico-civic.uwsgi restart
