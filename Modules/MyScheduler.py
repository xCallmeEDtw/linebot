from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import requests
import os

def sensor():
    print('123')
    url= 'https://gobuyssd.herokuapp.com/alive'
    r = requests.get(url)
    print(r.status_code)
    #print(r.text) 

    
# def work1():
#     r = requests.get('https://gobuyssd.herokuapp.com/')
#     print(r.text)   

def MyScheduler():
    sched = BackgroundScheduler(daemon=True)
    interval = IntervalTrigger(
        minutes= 1,
        start_date='2019-4-24 08:00:00',
        end_date='2099-4-24 08:00:00',
        timezone='Asia/Taipei')
    sched.add_job(sensor,trigger=interval)
    sched.add_job(work1, 'cron', hour=12, minute=30, end_date='2021-10-30',timezone='Asia/Taipei')
    sched.add_job(work1, 'cron', hour=19, minute=00, end_date='2021-10-30',timezone='Asia/Taipei')
    

    sched.start()
    return ''
