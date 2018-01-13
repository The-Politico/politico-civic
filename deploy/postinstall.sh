#!/bin/sh
sudo service awslogs restart
cd /home/ubuntu/apps/politico-civic
source /home/ubuntu/.bash_profile
pyenv global general
pipenv install
pipenv run python manage.py migrate
pipenv run python manage.py collectstatic
sudo service politico-civic.uwsgi restart
