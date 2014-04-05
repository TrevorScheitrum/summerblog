#!/usr/bin/env bash
#
# sys-provision.sh
# - Provisions a development server for boomers-web.

# Install system dependencies
sudo apt-get -y update
sudo DEBIAN_FRONTEND=noninteractive apt-get -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" dist-upgrade
sudo apt-get -y install python-software-properties
sudo add-apt-repository -y ppa:chris-lea/node.js
sudo apt-get -y update
sudo apt-get -y install make git-core python-pip python-dev nodejs libmysqlclient-dev rabbitmq-server
sudo apt-get -y install libjpeg-dev
sudo apt-get -y install postgresql postgresql-server-dev-9.1

# Install python dependencies
sudo pip install --upgrade pip
sudo pip install virtualenv virtualenvwrapper

# Install front-end dependencies
sudo npm install -g grunt-cli
sudo /opt/vagrant_ruby/bin/gem install compass
sudo /opt/vagrant_ruby/bin/gem install bootstrap-sass
