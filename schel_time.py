import schedule
import time
import os

os.system('python infinite_scroll_check.py')
def job():
    os.system('python infinite_scroll_check.py')
    
schedule.every(2).seconds.do(job)
#schedule.every().hour.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)