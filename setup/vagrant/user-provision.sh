#!/usr/bin/env bash
#
# user-provision.sh
# - Provisions a development environment for boomers-web

ENV=summerblog
PROFILE=/home/vagrant/.bash_profile
WORKON_HOME=/home/vagrant/.virtualenvs

# Create ~/.bash_profile if needed
if [ ! -f "$PROFILE" ]
then
    touch $PROFILE
fi

# Virtualenvwrapper
echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python" >> $PROFILE
echo "export WORKON_HOME=$WORKON_HOME" >> $PROFILE
echo ". `which virtualenvwrapper.sh`" >> $PROFILE

# Set default directory
echo "cd /vagrant" >> $PROFILE

# Reload .bash_profile
. $PROFILE

# Create and initialize the virtual environment
mkvirtualenv -a $PWD --no-site-packages $ENV
workon $ENV

# Install python dependencies
pip install -r setup/requirements.txt

# Install front-end dependencies
#npm install

# Start grunt server in background
#grunt &

# Ensure we are always in the virtualenv
echo "workon $ENV" >> $PROFILE
