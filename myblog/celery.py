from __future__ import absolute_import
from django.conf import settings
from celery import Celery

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings')

app = Celery('myblog', backend='amqp', broker='amqp://')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.config_from_object('django.conf:settings')


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))