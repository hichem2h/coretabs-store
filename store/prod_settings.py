import os

import dj_database_url

from .settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
debug_option = os.environ.get('DEBUG').lower()
if debug_option == 'true':
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(';')

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}