#!/bin/bash
. ~/.bash_profile
pyenv global 3.6.4
cd apps/politico-civic
python manage.py migrate
mkdir -p civic/static_results
python manage.py collectstatic --noinput