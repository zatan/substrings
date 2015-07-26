# -*- coding: utf-8 -*-

import multiprocessing

SITE_NAME = 'devspro'

bind = 'unix:/var/tmp/{}_gunicorn.sock'.format(SITE_NAME)
workers = multiprocessing.cpu_count() * 2 + 1
pidfile = '/var/tmp/{}_gunicorn.pid'.format(SITE_NAME)
user = 'www-data'
max_requests = 100
errorlog = '/var/log/gunicorn/{}-gunicorn-error.log'.format(SITE_NAME)


