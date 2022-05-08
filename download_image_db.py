
import pymongo
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common import exceptions 

from webdriver_manager.chrome import ChromeDriverManager
import pyperclip as pc
""" myclient = pymongo.MongoClient("mongodb+srv://aiotylabs:aiotylabs2020!@cluster0.zpris.mongodb.net/test")
mydb = myclient["webscrap"]
mycol = mydb["nft_links_1"]
info=mydb.nft_links_2 """

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://opensea.io/assets?search[categories][0]=art")
#driver.get("https://opensea.io/assets?search[categories][0]=art&search[query]=blitmap")
driver.maximize_window()
driver.delete_all_cookies()
driver.refresh()
driver.implicitly_wait(2)
#time.sleep(2)  # Allow 2 seconds for the web page to open
scroll_pause_time = 1# You can set your own pause time. My laptop is a bit slow so I use 1 sec
screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
i = 1

urls = [] 
x = mycol.find({},{"_id": 0,"nft_links":1})
   
s=[]
for x in mycol.distinct("nft_links"):
    p=s.append(x)
    #print(s)
#print(s)
for lo in s[500:5000]:
    s=driver.get(str(lo))
    #time.sleep(2)
    driver.implicitly_wait(1)
        
    driver.maximize_window()

    Llink_of_Nft = lo

    #image    
    obj = driver.find_elements_by_xpath("//img[@class='Image--image']")
    li=[]
    for w in obj:
        img_src=w.get_attribute("src")
        li.append(img_src)
        print(img_src)
    
    if len(li)==1:
        pass
    else:
        li.append(0)  

    #assert animation
    #//div[@class='AssetMedia--animation']
    #//iframe[@allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture']
    obj = driver.find_elements_by_xpath("//iframe[@allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture']")
    pi=[]
    lk=[]
    for w in obj:
        Amg_src=w.get_attribute("src")

        pi.append(Amg_src)
        
        print(Amg_src)
    
    if len(pi)==1:
        pass
    else:
        pi.append(0)

    #gif     --------------> working
    #obj = driver.find_elements_by_xpath("//video[@class='AssetMedia--video']")
    gif_s = driver.find_elements_by_xpath("//source")
    si=[]
    for w in gif_s:
        gif_src=w.get_attribute("src")
        si.append(gif_src) 
    print(len(si))  
    print(si)
    if len(si)==1:
        pass
    else:
        si.append(0)   

    dic={
        "NFt_link":lo,
        "NFT_image_link":li[0],
        "Assert_img_link":pi[0],
        "gif_video":si[0],
        #"downloaded_img":d
    }        

    #info.insert_one(dic)
    print(dic)

    print(li[0])
    print(si[0])
    print(pi[0])
print("successful")