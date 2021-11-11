from celery import app
#from celery.schedules import crontab
#from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
#from celery import periodic_task, crontab, get_task_logger
from mpiapi0.models import Upvote
from celery import shared_task

'''
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Executes daily at midnight
    sender.add_periodic_task(
        crontab(hour=0, minute=1),
        delete_old_upvotes.s('Drop the Table! (Upvote)'),
    )
'''

logger = get_task_logger(__name__)

import datetime, time
#@periodic_task(run_every=(crontab(minute='*/1')), name="delete_old_upvotes", ignore_result=True)
@shared_task()
def delete_old_upvotes():
    #print(Upvote.objects.all().filter(upvoted_on__day=1))
    #print('1 day old upvotes deleted from database.')
    print('#@#@#@#@#@ Today is: ', datetime.datetime.now())
    yestarday = (datetime.date.today()-datetime.timedelta(days=1)).day
    print(yestarday, 'yestarday date is: ', (datetime.date.today()-datetime.timedelta(days=1)))
    
    while Upvote.objects.all().filter(upvoted_on__day=yestarday).first() != None:
        print('Is it None: ', type(Upvote.objects.all().filter(upvoted_on__day=yestarday).first()))
        if Upvote.objects.all().filter(upvoted_on__day=yestarday).first() == None:
            print('Nothing to delete')

        day_upvoted_on = Upvote.objects.all().filter(upvoted_on__day=yestarday).first().upvoted_on.day
        print('day_upvoted_on ', day_upvoted_on)
        if day_upvoted_on == yestarday:
            Upvote.objects.all().filter(upvoted_on__day=yestarday).delete()
            print('Upvoted row deleted')
        else:
            return 'No yestarday upvotes or Upvotes has been reset if None=None. Does it: None = ' + str(Upvote.objects.all().filter(upvoted_on__day=yestarday).first())
        time.sleep(10)
    else:
        return 'Upvotes has been reset'

    #logger.info('1 day old upvotes deleted from database.')
    