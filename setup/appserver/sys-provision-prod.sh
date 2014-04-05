#!/usr/bin/env bash
#
# sys-provision-prod.sh
# - Provisions a production server for boomers-web.

# Install system dependencies
sudo yum update -y
sudo yum upgrade -y
sudo yum install -y mysql-devel

# Add nowu group/user
groupadd webapps
useradd --create-home -g webapps -p "$pb3E_b9" nowu

# Set up SSH keys
sudo -u nowu -i mkdir .ssh
# TODO: put id_rsa and id_rsa.pub into ~/.ssh
sudo -u nowu -i echo "Host github.com" > ~/.ssh/config
sudo -u nowu -i echo "  User mattcaldwell" >> ~/.ssh/config
sudo -u nowu -i echo "  IdentityFile ~/.ssh/id_rsa" >> ~/.ssh/config
chmod 700 ~/.ssh/id_rsa
chmod 700 ~/.ssh/id_rsa.pub

# Install celery
#useradd --system --no-create-home celery
mkdir /home/nowu/celery
chown nowu:nowu /home/now/celery
pip install celery
# TODO: copy init script and default script to /etc

# TODO: install rabbitmq
# ---> http://www.thegeekstuff.com/2013/04/install-rabbitmq-server/
# ---> wget http://www.rabbitmq.com/releases/rabbitmq-server/v3.2.3/rabbitmq-server-3.2.3-1.noarch.rpm
# ---> rpm --import http://www.rabbitmq.com/rabbitmq-signing-key-public.asc
# ---> yum install rabbitmq-server-3.2.3-1.noarch.rpm

# Install redis
pushd .
sudo useradd --system --no-create-home redis
cd /tmp
wget http://download.redis.io/releases/redis-2.8.6.tar.gz
tar xz redis-2.8.6.tar.gz
cd redis-2.8.6
make
make install
mkdir /etc/redis /var/lib/redis
sed -e "s/^daemonize no$/daemonize yes/" -e "s/^dir \.\//dir \/var\/lib\/redis\//" -e "s/^loglevel debug$/loglevel notice/" -e "s/^logfile stdout$/logfile \/var\/log\/redis.log/" redis.conf  > /etc/redis/6379.conf
cp utils/redis_init_script /etc/init.d/redis-server
chmod 744 /etc/init.d/redis-server
service redis start
popd

# Create virtualenv
pip install virtualenv virtualenvwrapper
source /usr/local/bin/virtualenvwrapper.sh
export WORKON_HOME=/home/nowu/.virtualenvs
mkdir -p $WORKON_HOME
mkvirtualenv --no-site-packages boomers-web
echo "/home/nowu/boomers-web" > $WORKON_HOME/.project
chown -R nowu:webapps /home/nowu/.virtualenvs

# Set up nowu's environment
echo "export DJANGO_SETTINGS_MODULE=boomers.settings.prod" >> /home/nowu/.bashrc
echo "export WORKON_HOME=~/.virtualenvs" >> /home/nowu/.bashrc
echo 'export BOOMER_RDS_PASS="jgKvArs%3G5r' >> /home/nowu/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> /home/nowu/.bashrc
echo "workon boomers-web" >> /home/nowu/.bashrc

# Clone the repository
sudo -u nowu -i git clone git@github.com:GannettDigital/boomers-web.git

# TODO: nginx config: /etc/nginx/conf.d/default.conf
# This should use uwsgi pass-through
# Then: service nginx restart

# uwsgi configuration
mkdir /etc/uwsgi
cp /home/nowu/boomers-web/setup/appservers/uwsgi_init /etc/init.d/uwsgi
chmod 744 /etc/init.d/uwsgi
cp /home/nowu/boomers-web/setup/appservers/uwsgi.ini /etc/uwsgi/boomers.ini
service uwsgi start

# uwsgi logs
mkdir /var/log/uwsgi
chown nowu:webapps /var/log/uwsgi

service celeryd start
service celerybeat start
