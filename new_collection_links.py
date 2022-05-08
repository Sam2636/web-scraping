
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
myclient = pymongo.MongoClient("mongodb+srv://aiotylabs:aiotylabs2020!@cluster0.zpris.mongodb.net/test")
mydb = myclient["webscrap"]
mycol = mydb["ranking_collection"]
info=mydb.nft_links_new_collection_21

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
x = mycol.find({},{"_id": 0,"nft_collection_links":1})
   
""" s=[]     #----------->
for x in mycol.distinct("nft_collection_links"):
    p=s.append(x)
    #print(s) """


urls=[]
for lo in s[300:400]:
    s=driver.get(str(lo))
    driver.implicitly_wait(1)
    driver.maximize_window()

    scroll_pause_time = 1# You can set your own pause time. My laptop is a bit slow so I use 1 sec
    screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
    i = 1

    for j in  range(0,50):

        # scroll one screen height each time
        driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
        i += 1 
        time.sleep(scroll_pause_time)
        # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
        scroll_height = driver.execute_script("return document.body.scrollHeight;")  
        # Break the loop when the height we need to scroll to is larger than the total scroll height
        if (screen_height) * i > scroll_height:
            pass       #break 

    ##### Extract Reddit URLs #####
        #urls = []
        """ soup = BeautifulSoup(driver.page_source, "html.parser")
        for parent in soup.find_all(class_="Assetreact__DivContainer-sc-bnjqwy-0 fXNMWi Asset--loaded AssetSearchList--asset "):
        #for parent in soup.find_all(class_="Assetreact__DivContainer-sc-bnjqwy-0 gwTKfX Asset--loaded AssetSearchList--asset"):------->replaced in 10-11-2021
        #Assetreact__DivContainer-sc-bnjqwy-0 fXNMWi Asset--loaded AssetSearchList--asset    ---------->change in 10-11-2021
        #for parent in soup.find_all(class_="Blockreact__Block-sc-1xf18x6-0 ctiaqU AssetsSearchView--assets"):
            #a_tag = parent.find("a", class_="styles__StyledLink-sc-l6elh8-0 cnTbOd Asset--anchor")
            a_tag = parent.find("a", class_="styles__StyledLink-sc-l6elh8-0 ekTmzq Asset--anchor")
            base = "https://opensea.io/assets?search[categories][0]=art"
            link = a_tag.attrs['href']
            url = urljoin(base, link)
            urls.append(url) """
        def assert_crawl():
            driver.implicitly_wait(100000)  
            #time.sleep(1)
            saly=kl.get_attribute("href")
            driver.implicitly_wait(15)
            urls.append(saly)
            driver.implicitly_wait(15)
        
        sectio= driver.find_elements_by_xpath("//a[@class='styles__StyledLink-sc-l6elh8-0 ekTmzq Asset--anchor']")
    
        if len(sectio)!=0:
            for kl in sectio:    
                try:
                    assert_crawl()
                #driver.delete_all_cookies()
                except StaleElementReferenceException: 
                    try:
                        assert_crawl()
                #driver.delete_all_cookies()
                    except StaleElementReferenceException: 
                        pass                   
                #print(len(sales1))
            print(len(urls)) 
        #print(len(urls))    
    #print(urls[0:25])

                
        #time.sleep(5)
        driver.implicitly_wait(5)

        #print ("The original list is : " +  str(urls))
        #print(len(urls))
        # using naive method
        # to remove duplicated 
        # from list 
        
        res = []
        for i in urls:
            if i not in res:
                dicc={
                    "nft_links":i
                }
                info.insert_one(dicc)
                res.append(i)
        if len(res)==0:
            pass    
    print('this is',len(urls))    #--------->newly commited from here
    if len(urls)==0:
        try:       
                    
                def assert_crawl():
                    driver.implicitly_wait(100000)  
                    #time.sleep(1)
                    saly=kl.get_attribute("href")
                    driver.implicitly_wait(15)
                    
                    urls.append(saly)
                    driver.implicitly_wait(15)
                #ime.sleep(1)
                sectio= driver.find_elements_by_xpath("//a[@class='styles__StyledLink-sc-l6elh8-0 ekTmzq CarouselCard--main CollectionCardreact__Card-sc-1b2ne4j-0 fyrXjw']")
                driver.implicitly_wait(15)
                if len(sectio)!=0:
                    for kl in sectio:  
                        
                        try:
                            assert_crawl()
                            #driver.delete_all_cookies()
                        except StaleElementReferenceException: 
                            pass
                            assert_crawl()
                            print("except")
                            
                            
                            
                            #driver.delete_all_cookies()
                                
                        #print(len(sales1))
                    driver.delete_all_cookies()
                    print(len(urls)) 
                #print(len(urls))    
                #print('this is',len(urls))    
            #print(urls[0:25])
            #time.sleep(5)
                driver.implicitly_wait(15)

                res = []
                for i in urls:
                    if i not in res:
                        dic={
                            "nft_popular_links":i
                        }
                        info.insert_one(dic)
                        res.append(i)

        except:
             pass       
    # printing list after removal 
    #print ("The list after removing duplicates : " + str(res))     #------> new commit to here
    print(len(urls))
    print(len(res))
    #print("the difference between them are:{}".format(len(urls)-len(res)))
    #print("the percentage between them:{}%".format(len(res)/(len(urls))*100))
    urls.clear()
    res.clear()
    print("this is empty urls",urls)
    print("this is empty res",res)
    driver.back()

print("done")