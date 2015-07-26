# -*- coding: utf-8 -*-


from .base import *   # NOQA @UnusedWildImport


INTERNAL_IPS = (
    '192.168.1.29',
)


SECRET_KEY = 'devspro'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_env_variable('DJANGO_DATABASE_NAME'),
        'USER': get_env_variable('DJANGO_DATABASE_USER'),
        'HOST': get_env_variable('DJANGO_DATABASE_HOST'),
        'PASSWORD': get_env_variable('DJANGO_DATABASE_PASSWORD'),
        'PORT': '5432',
        'ATOMIC_REQUESTS': True
    },
}


# Debug templates
DEBUG = True
THUMBNAIL_DEBUG = True
TEMPLATES[0]['OPTIONS'].update({'debug': True})


# Output email to console.
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


THIRD_PARTY_APPS += [
    'debug_toolbar',
    'django_extensions',
]


MIDDLEWARE_CLASSES += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + PROJECT_APPS


# Stop sentry reporting errors in debug mode.
RAVEN_CONFIG['dsn'] = ''


