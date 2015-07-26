# -*- coding: utf-8 -*-

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

from django.core.exceptions import ImproperlyConfigured


BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Set default path to django apps
PROJECT_APPS_ROOT = os.path.join(BASE_DIR, '../apps')
sys.path.append(PROJECT_APPS_ROOT)


def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#yfk@wee8bv^_tymyc+70oszp*uxfnf)qjio8wps&zkqt70&no'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
THUMBNAIL_DEBUG = False
THUMBNAIL_PRESERVE_FORMAT = True


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '../templates')],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'debug': False,
        },
    },
]


# Application definition
DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
]


THIRD_PARTY_APPS = [
    'raven.contrib.django.raven_compat',
    'sorl.thumbnail',
    'rest_framework',
]


PROJECT_APPS = [
    'strings',
]


SITE_ID = 1


MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'devspro.urls'


WSGI_APPLICATION = 'devspro.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
LANGUAGE_CODE = 'en-gb'


TIME_ZONE = 'Europe/London'


USE_I18N = True


USE_L10N = False


USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'


STATIC_ROOT = os.path.join(BASE_DIR, '../static')


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


# The default file storage backend used during the build process
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)


MEDIA_ROOT = os.path.join(BASE_DIR, '../media')
MEDIA_URL = '/media/'

# MANDRILL
DEFAULT_FROM_EMAIL = 'debug@edvinas.co.uk'


SERVER_EMAIL = 'debug@edvinas.co.uk'


# ADMINS
ADMINS = (
    ('Edvinas Jurevicius', 'ikonitas@gmail.com'),
)


# MANAGERS
MANAGERS = (
    ('Edvinas Jurevicius', 'ikonitas@gmail.com'),
)


RAVEN_CONFIG = {
    'dsn': '',
}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'simple': {
            'format': '%(name)s %(levelname)s %(asctime)s %(message)s',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },

    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'sentry.error': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'raven.contrib.django.handlers.SentryHandler',
        },
        'sentry.critical': {
            'level': 'CRITICAL',
            'filters': ['require_debug_false'],
            'class': 'raven.contrib.django.handlers.SentryHandler',
        },
        'sentry.warning': {
            'level': 'WARNING',
            'filters': ['require_debug_false'],
            'class': 'raven.contrib.django.handlers.SentryHandler',
        }
    },
    'loggers': {
        '': {
            'filters': ['require_debug_false'],
            'handlers': ['sentry.error', 'sentry.critical', 'sentry.warning', 'mail_admins'],
            'propagate': True,
        },
        'django.request': {
            'filters': ['require_debug_false'],
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        }
    }
}


COVERAGE_EXCLUDES_FOLDERS = ['/var/envs/devspro/lib/python2']

