import time
#import pymongo
import json
import csv
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

#client =pymongo.MongoClient('mongodb://127.0.0.1:27017/')

#my_db=client['webscrap']
#info=my_db.scraping

s=driver.get('https://etherscan.io/txs')
driver.maximize_window()

#table =driver.find_element_by_class_name("table table-hover")
#blockchain transaction details:
li=[]
header = driver.find_element_by_tag_name("tr")
print(header.text.splitlines())
""" for i in header:
    print(i.text)  """
value=driver.find_element_by_id('paywall_mask')
s=value.text.splitlines()
d=li.append(s[7])
e=li.append(s[8])
print(s)

#print(li.split)


