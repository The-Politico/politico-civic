import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'civic.settings')

app = Celery('civic')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.update(
    broker_url=os.getenv('REDIS_URL', 'redis://127.0.0.1:6379'),
    task_serializer='json',
    timezone='America/New_York',
)
# Use synchronous in local dev
if settings.DEBUG:
    app.conf.update(task_always_eager=True)
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS, related_name='celery')
