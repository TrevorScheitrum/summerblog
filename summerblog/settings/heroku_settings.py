# Parse database configuration from $DATABASE_URL
import os
import dj_database_url

try:
    from settings import *
except:
    pass

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'ddugen3tfj23bt',
    'HOST': 'ec2-107-21-100-118.compute-1.amazonaws.com',
    'PORT': 5432,
    'USER': 'jjrizlgbzvosaj',
    'PASSWORD': '35dbydktkDgUREOwh0KIUGhh7X'
  }
}

DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'


DEBUG = True
TEMPLATE_DEBUG = DEBUG


# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = '/home/media/uploads/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/static_media/'

ADMIN_MEDIA_PREFIX = '/media/'


# Make this unique, and don't share it with anybody.
SECRET_KEY = ')$@*3!)v)%8m7=+s7sj=ygh3soujd4&4u!z_)9k0xt6=kz-q8a6'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'settings.wsgi.application'

CKEDITOR_IMAGE_BACKEND = 'pillow'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_STORAGE_BUCKET_NAME = "summerblog-assets"
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'


LOGIN_URL = "django.contrib.auth.views.login"  # not 100% necessary
LOGIN_REDIRECT_URL = "/"

AWS_QUERYSTRING_AUTH = False
STATIC_URL = 'http://s3.amazonaws.com/%s' % AWS_STORAGE_BUCKET_NAME + '/'

