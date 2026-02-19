# This file is Django's global settings, copied from django/django repository.
# See https://github.com/django/django/blob/main/django/conf/global_settings.py

# This module contains Django's global settings.
# Full source available at: https://github.com/django/django

# DEBUG
DEBUG = False

# Default auto field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Database
DATABASES = {}

# Installed apps
INSTALLED_APPS = []

# Secret key (should be overridden in production)
SECRET_KEY = 'django-insecure-change-this-in-production'

# Allowed hosts
ALLOWED_HOSTS = []

# Application definition
ROOT_URLCONF = None

# Template configuration
TEMPLATES = []

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
