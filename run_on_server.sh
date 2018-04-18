cd /home/ubuntu/
export PATH="/home/ubuntu/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
pyenv global 3.6.4
cd `dirname "$0"`
eval $@