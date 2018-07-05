"""
Django settings for globus_portal_framework project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

###############################################################################
# Search Settings
###############################################################################

# "perfdata" search index
SEARCH_INDEX = '5e83718e-add0-4f06-a00d-577dc78359bc'
SEARCH_MAPPER = ('globus_portal_framework', 'default_search_mapper')
SEARCH_SCHEMA = os.path.join(os.path.dirname(__file__), 'data/datacite.json')

SEARCH_ENTRY_FIELD_PATH = 'perfdata'
# Specify the field containing the title
SEARCH_ENTRY_TITLE = 'titles'

SEARCH_RESULTS_PER_PAGE = 10
SEARCH_MAX_PAGES = 10
# This will be the automatic search query when the user loads the page, if
# they have not submitted their own query or there is no query loaded in the
# session. "*" will automatically search everything, but may not be desirable
# if there is a lot of search data in the index, as searches will take a while
DEFAULT_QUERY = '*'

###############################################################################
# Transfer Settings
###############################################################################


# Variables stored per-search entry on the Globus Search index.
ENTRY_SERVICE_VARS = {
    'globus_group': 'globus_group',
    'globus_http_link': 'globus_http_link',
    'globus_http_scope': 'globus_http_scope'
}
ENTRY_SERVICE_VARS_MAPPER = ('globus_portal_framework',
                             'default_service_vars_mapper')
PREVIEW_DATA_SIZE = 2048

###############################################################################
# General Settings
###############################################################################

# Create 'local_settings.py' and put your below values there to avoid
# accidentally committing them.
# Secret key can be generated with 'openssl rand -hex 32'
SECRET_KEY = ''
DEBUG = False
# Get your keys at 'developers.globus.org'
SOCIAL_AUTH_GLOBUS_KEY = '<your_Globus_Auth_Client_ID>'
SOCIAL_AUTH_GLOBUS_SECRET = '<your_Globus_Auth_Client_Secret>'
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'globus_portal_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Social Django needed for Globus Auth
    'social_django.middleware.SocialAuthExceptionMiddleware',
    # Redirect to auth page if expired tokens, then back to original page
    'globus_portal_framework.middleware.ExpiredTokenMiddleware',
]

AUTHENTICATION_BACKENDS = [
   'globus_portal_framework.auth.GlobusOAuth2',
   'django.contrib.auth.backends.ModelBackend',
]

SOCIAL_AUTH_SANITIZE_REDIRECTS = False
# Access type needed to get a refresh token
SOCIAL_AUTH_GLOBUS_AUTH_EXTRA_ARGUMENTS = {
    'access_type': 'offline',
}

# Additional extras
GLOBUS_HTTP_ENDPOINT = 'https://b4eab318-fc86-11e7-a5a9-0a448319c2f8' \
                       '.petrel.host'
PREVIEW_TOKEN_NAME = 'petrel_https_server'

SOCIAL_AUTH_GLOBUS_SCOPE = [
    'urn:globus:auth:scope:search.api.globus.org:search',
    'urn:globus:auth:scope:transfer.api.globus.org:all',
    'https://auth.globus.org/scopes/56ceac29-e98a-440a-a594-b41e7a084b62/all'
]

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
CSRF_USE_SESSIONS = True

ROOT_URLCONF = 'globus_portal_framework.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'globus_portal_framework.context_processors.globals',
            ],
        },
    },
]

WSGI_APPLICATION = 'globus_portal_framework.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'stream': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
        },
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
    },

    'loggers': {
        'django.db.backends': {
                    'handlers': ['stream'],
                    # 'handlers': ['null'],  # Quiet by default!
                    # 'propagate': False,
                    'level': 'WARNING',
                    },
        'globus_portal_framework': {
            'handlers': ['stream'],
            'level': 'DEBUG',
            'propagate': True,
        }
    },
}

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

# Override any settings here if a local_settings.py file exists
try:
    from globus_portal_framework.local_settings import *  # noqa
except ImportError:
    pass
