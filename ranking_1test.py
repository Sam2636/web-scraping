#//a[@class='styles__StyledLink-sc-l6elh8-0 ekTmzq CarouselCard--main CollectionCardreact__Card-sc-1b2ne4j-0 fyrXjw']

#scopex webscraping script using python 

""" 
.........updated on 12/10/2021......

.........@sam dhana seelan.........
 """


import time
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pymongo
from pymongo import MongoClient
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common import exceptions 

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pyperclip as pc

# starting time
start = time.time()

#driver = webdriver.Edge(EdgeChromiumDriverManager().install())
# for driver we can download and specifiy the path or we can use the below code  
driver = webdriver.Chrome(ChromeDriverManager().install())

client =MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')

my_db=client['webscrap']
info=my_db.rank



#driver.get("https://opensea.io/assets?search[categories][0]=art")
driver.get("https://opensea.io/rankings")
#driver.get("https://www.amazon.com/")
#driver.get("https://opensea.io/assets?search[categories][0]=art&search[query]=blitmap")
driver.maximize_window()
driver.delete_all_cookies()
driver.refresh()
#x=driver.find_element_by_xpath("//button[@class='Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 hcFcTD ebWXmm ButtonGroupreact__StyledButton-sc-1skvztv-0 eztnHW ToggleButtonGroupreact__StyledGroupButton-sc-1kkabdn-0 bnWGYU']").click()

driver.implicitly_wait(2)

#//a[@class='styles__StyledLink-sc-l6elh8-0 ekTmzq Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 Itemreact__ItemBase-sc-1idymv7-0 fBcBFY jYqxGr dCVDRE fresnel-lessThan-xl']
pi=[]
li=[]
urls = []
for k in range(0,2):
    driver.implicitly_wait(1)
    scroll_pause_time = 1# You can set your own pause time. My laptop is a bit slow so I use 1 sec
    screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
    i=1
    for j in range(0,10):
        # scroll one screen height each time
        #time.sleep(3) 
        driver.implicitly_wait(1)

        driver.implicitly_wait(15)
        # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
        scroll_height = driver.execute_script("return document.body.scrollHeight;")  
        # Break the loop when the height we need to scroll to is larger than the total scroll height
        if (screen_height) * i > scroll_height:
            pass  

        driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
        i += 1 
        time.sleep(scroll_pause_time)

        obj= driver.find_elements_by_xpath("//div[@role='listitem']/a")
        #obj = driver.find_elements_by_xpath("//a[@class='styles__StyledLink-sc-l6elh8-0 ekTmzq Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 Itemreact__ItemBase-sc-1idymv7-0 fBcBFY jYqxGr dCVDRE fresnel-lessThan-xl']")
        print(obj)
        serialno=1
        for w in obj:
            print(serialno)
            serialno=serialno+1
            try:
                links_slug=w.get_attribute("href")
                links_src=w.text.replace('\n',",").split(',')
                print(links_src)
                li.append(links_src)
                pi.append(links_slug)
            except StaleElementReferenceException:   
                try:
                    #links_src=w.get_attribute("href")
                    links_src=w.text
                    print(links_src)
                    li.append(links_src)
                    pi.append(links_slug)
                except StaleElementReferenceException: 
                    pass  

        
        ''' secti= driver.find_elements_by_xpath("//div[@class='Overflowreact__OverflowContainer-sc-7qr9y8-0 jPSCbX']")
        lk=[]
        for j in secti:

            heade=j.text
            ep=urls.append(heade)
            print(heade)
        print(lk)  '''

        #links_collection
        #//a[@class='styles__StyledLink-sc-l6elh8-0 ekTmzq Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 Itemreact__ItemBase-sc-1idymv7-0 fBcBFY jYqxGr dCVDRE fresnel-lessThan-xl']
        



        #//button[@class='Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 fTomoL hJoTEY']
    try:
        print("---")
        ''' secti= driver.find_element_by_xpath("//div[@class='Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 bmuUBa jYqxGr']/button[1]")
        secti.click()   '''
        button = driver.find_element_by_class_name("Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 kGCMze ghtTPW")

        # clicking on the button
        button.click() 
    except:

        print("<>")
        pass
#print(len(urls))

res = []
#for i in urls:
for i in li:
    if i not in res:
        dicc={
            "nft_collection_links":i
        }
        #info.insert_one(dicc) 
        res.append(i)
ser=[]        
for l in pi:
    if l not in ser:
        dicc={
            "slug":l
        }
        #info.insert_one(dicc) 
        ser.append(l)

driver.implicitly_wait(3)
#Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 kGCMze ghtTPW
""" try:

    sectioo= driver.find_element_by_xpath("//button[@class='Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 kGCMze ghtTPW']")
    sectioo.click()
    print("----")
except:
    print("oooooooooooooooh")
    pass     """     

print(len(li))
print(len(res))
print(res)
print(ser)
print(len(ser))

#li.clear()
#res.clear()
#print(len(li))
#print(len(res))
driver.delete_all_cookies()
for lk in ser:
    print(lk.split('/')[4])             #---------------------->slug


for i in res:
    print(i[1].lower())


for i in res:
    for ji in range(0,50):
        if i[0]==str(ji):
            print("rank:-"+str(ji),"-->"+i[1])             #---------------------------------->ranking
#print("success")


driver.close()