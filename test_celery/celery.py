from __future__ import absolute_import
from celery import Celery

#initialize instance of Celery named 'app' - will be used for creating task
# just the name of the project package : test-celery
# broker url format: 'transport://user:password@hostname:port/vhostname'
# backend: specifies the backend url - where results will be stored
#           rpc - sending results back as AMQP message
# include : specifies the list of modules that need to be imported when
#           Celery worker starts

app = Celery('test-celery',
            broker='amqp://ijhajj:password@localhost/ijhajj_vhost',
            backend='rpc://',
            include=['test_celery.tasks'])
