from django.test import TestCase

# Create your tests here.
import datetime, time
#from mpiapi0.models import Upvote ### something wrong with import. Run through terminal "python3 manage.py shell"

list1 = [1, 2, 3]

today1 = datetime.datetime.now()
yesterday1 = datetime.datetime.now()-datetime.timedelta(days=1)

print(today1, yesterday1)
#print('======== time: ', Upvote.objects.all().filter(upvoted_on__day=1)) #

print(datetime.date.today().day)
print((datetime.date.today()-datetime.timedelta(days=1)).day)

#today = datetime.date.today()-datetime.timedelta(days=1)
# Upvote.objects.all().filter(upvoted_on__day=1))  ### to delete database raw

today_start = datetime.datetime.now()
print(today_start < today_start+datetime.timedelta(minutes=1))
print(today_start, '-----', today_start+datetime.timedelta(minutes=1))
tommorow = today_start+datetime.timedelta(minutes=1)

while True:
    while datetime.datetime.now() < tommorow:
        time.sleep(10)
        print(today_start, datetime.datetime.now())
    else:
        today_start = datetime.datetime.now()
        tommorow = today_start+datetime.timedelta(minutes=1)
        print('A day has passed. Today is:', today_start, datetime.date.today())

