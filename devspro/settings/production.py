# -*- coding: utf-8 -*-

from .base import *  # NOQA @UnusedWildImport


ALLOWED_HOSTS = ['zatan.pythonanywhere.com']


EMAIL_BACKEND = ''


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


DEBUG = False

TEMPLATES[0]['OPTIONS'].update({
    'loaders': [
        ('django.template.loaders.cached.Loader', [
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ]),
    ]
})


INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + PROJECT_APPS


