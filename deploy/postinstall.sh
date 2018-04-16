#!/bin/bash
set -e
source /home/ubuntu/.bash_profile

cd /home/ubuntu/apps/politico-civic/

pyenv global 3.6.4
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
sudo service politico-civic.uwsgi restart
