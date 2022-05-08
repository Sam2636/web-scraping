

import time
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pymongo
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

from webdriver_manager.chrome import ChromeDriverManager
import pyperclip as pc

# starting time
start = time.time()

# for driver we can download and specifiy the path or we can use the below code  
driver = webdriver.Chrome(ChromeDriverManager().install())

client =pymongo.MongoClient('mongodb+srv://aiotylabs:aiotylabs2020!@cluster0.zpris.mongodb.net/test')
#client =pymongo.MongoClient('mongodb://127.0.0.1:27017/')

my_db=client['webscrap']
info=my_db.scrap_1

#https://opensea.io/collection/coca-cola

driver.get("https://google.com")
#driver.get("https://opensea.io/assets?search[categories][0]=art&search[query]=blitmap")
driver.maximize_window()
driver.delete_all_cookies()
driver.refresh()
driver.implicitly_wait(2)