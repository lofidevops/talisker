from __future__ import absolute_import, unicode_literals
import logging
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_app.settings')

app = Celery('django_app')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks('django_app')


@app.task(bind=True)
def debug_task(self):
    logging.getLogger(__name__).info(
        'request', extra={'request': repr(self.request)})
