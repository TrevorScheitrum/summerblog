# Parse database configuration from $DATABASE_URL
import os
import dj_database_url

try:
    from settings import *
except:
    pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


DATABASES = {      
    'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
       'NAME': "summerblog",                      # Or path to database file if using sqlite3.
       # The following settings are not used with sqlite3:
       'USER': 'tascheitrum',
       'PASSWORD': 'matrix3',
    }
}


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration

#STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
STATIC_ROOT = "/home/tascheitrum/webapps/summerblog_static/"


# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = '/home/tascheitrum/webapps/summerblog/summerblog/summerblog/media-assets/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/media/'


# Make this unique, and don't share it with anybody.
SECRET_KEY = ')$@*3!)v)%8m7=+s7sj=ygh3soujd4&4u!z_)9k0xt6=kz-q8a6'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'settings.webfaction_wsgi.application'

CKEDITOR_IMAGE_BACKEND = 'pillow'
#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

#AWS_STORAGE_BUCKET_NAME = "summerblog-assets"
#STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'


#LOGIN_URL = "django.contrib.auth.views.login"  # not 100% necessary
#LOGIN_REDIRECT_URL = "/"

#AWS_QUERYSTRING_AUTH = False
#STATIC_URL = 'http://s3.amazonaws.com/%s' % AWS_STORAGE_BUCKET_NAME + '/'

