from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_rest_MPI0.settings')
app = Celery('django_rest_MPI0', include=['django_rest_MPI0.tasks'])
app.config_from_object('django.conf:settings', namespace='CELERY')
#from django.apps import apps
#app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task#(name="sum_two_numbers")
def add(x, y):
    return x + y


'''
#from mpiapi0.models import Upvote
from celery.utils.log import get_task_logger
from celery.schedules import crontab

@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    # Executes daily at midnight
    sender.add_periodic_task(
        crontab(hour=0, minute=1),
        delete_old_upvotes.s('Drop the Table! (Upvote)'),
    )

logger = get_task_logger(__name__)

#@shared_task
#@periodic_task(run_every=(crontab(minute='*/1')), name="delete_old_upvotes", ignore_result=True)
@app.task
def delete_old_upvotes():
    print(Upvote.objects.all().filter(upvoted_on__day=1))
    print('1 day old upvotes deleted from database.')
    logger.info('1 day old upvotes deleted from database.')
    
'''