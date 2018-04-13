#!/bin/bash
set -e
source /home/ubuntu/.bash_profile

# Move to the project dir... This is important.
cd /home/ubuntu/apps/politico-civic/

cp /home/ubuntu/.env .

pyenv global 3.6.4
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
sudo service politico-civic.uwsgi restart
