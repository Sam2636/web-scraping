#scopex webscraping script using python 

""" 
.........updated on 28/10/2021......

.........@sam dhana seelan.........
 """


import time
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pymongo
import re
import sys
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

from webdriver_manager.chrome import ChromeDriverManager
import pyperclip as pc


#email-error-message
""" name_vm='user_0:spider_02_test'
mail_id='samdhanaseelan2636@gmail.com'
user='sam' """




# starting time
start = time.time()

# for driver we can download and specifiy the path or we can use the below code  
driver = webdriver.Chrome(ChromeDriverManager().install())


client =pymongo.MongoClient('mongodb+srv://aiotylabs:aiotylabs2020!@cluster0.zpris.mongodb.net/test')

my_db=client['webscrap']
mycol = my_db["mycol23"]
info=my_db.scsc



driver.get("https://opensea.io/assets?search[categories][0]=art")
#driver.get("https://opensea.io/assets?search[categories][0]=art&search[query]=blitmap")
driver.maximize_window()
driver.delete_all_cookies()
driver.refresh()
driver.implicitly_wait(30)
#time.sleep(2)  # Allow 2 seconds for the web page to open
scroll_pause_time = 1# You can set your own pause time. My laptop is a bit slow so I use 1 sec
screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
i = 1

urls = []
s=[]     #----------->
for x in mycol.distinct("collector_address"):
    p=s.append(x)
    #print(s) """

obj = driver.find_elements_by_xpath("//a[@class='styles__StyledLink-sc-l6elh8-0 ekTmzq AccountHeader--social-container']")
li=[]
for w in obj:
    social_link=w.get_attribute("href")
    li.append(social_link)
if len(li)>0:
    pass
else:
    li.append(0)
print(li)

# end time
end = time.time()

tim= end - start
# total time taken
#print(f"Runtime of the program is {(end - start)/60} minutes")
def run_time(seconds):
    seconds_in_day = 86400
    seconds_in_hour = 3600
    seconds_in_minute = 60


    days = seconds // seconds_in_day
    seconds = seconds - (days * seconds_in_day)

    hours = seconds // seconds_in_hour
    seconds = seconds - (hours * seconds_in_hour)

    minutes = seconds // seconds_in_minute
    seconds = seconds - (minutes * seconds_in_minute)

    print("{0:.0f} days, {1:.0f} hours, {2:.0f} minutes, {3:.0f} seconds.".format(days, hours, minutes, seconds))

run_time (float(tim))            #(input("Enter a number of seconds: "))

#print("{} is success".format(name_vm))
#sus="{} is success".format(name_vm)
#requests.get("http://www.thewhizly.co.in/sendinblue/scopex_email.php?email={}&name={}&error={}&vm_id={}".format(mail_id,user,(repr(e)),name_vm))
