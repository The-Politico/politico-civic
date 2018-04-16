#!/bin/bash
. ~/.bash_profile
pyenv global 3.6.4
mkdir -p apps/
cd apps
git clone https://github.com/The-Politico/politico-civic.git
cd politico-civic
pip install -r requirements.txt