#scopex webscraping script using python 

""" 
.........updated on 7/10/2021......

.........@sam dhana seelan.........
 """


import time
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pymongo
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

from webdriver_manager.chrome import ChromeDriverManager
import pyperclip as pc

# starting time
start = time.time()

# for driver we can download and specifiy the path or we can use the below code  
driver = webdriver.Chrome(ChromeDriverManager().install())

client =pymongo.MongoClient('mongodb://127.0.0.1:27017/')

my_db=client['webscrap']
info=my_db.links



driver.get("https://opensea.io/assets?search[categories][0]=art")
#driver.get("https://opensea.io/assets?search[categories][0]=art&search[query]=blitmap")
driver.maximize_window()
driver.implicitly_wait(2)
#time.sleep(2)  # Allow 2 seconds for the web page to open
scroll_pause_time = 1# You can set your own pause time. My laptop is a bit slow so I use 1 sec
screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
i = 1

urls = []

for j in  range(0,2):

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

    sectio= driver.find_elements_by_xpath("//a[@class='styles__StyledLink-sc-l6elh8-0 ekTmzq Asset--anchor']")
    if len(sectio)!=0:
        for kl in sectio:    
            saly=kl.get_attribute("href")
            urls.append(saly)
            #print(len(sales1))
        print(len(urls)) 
    #print(len(urls))    
print('this is',len(urls))    
#print(urls[0:25])

#time.sleep(5)
driver.implicitly_wait(5)

print ("The original list is : " +  str(urls))
print(len(urls))
# using naive method
# to remove duplicated 
# from list 
res = []
for jk in urls:
    if jk not in res:
        res.append(jk)
        #info.insert_one(jk)



        

""" for i in res:
    info.insert_one(i)   """   

""" dic={
    
    "links":str(res[0:-1])
}     


info.insert_one(dic)  """
  
# printing list after removal 
print ("The list after removing duplicates : " + str(res))
print(len(urls))
print(len(res))
print("the difference between them are:{}".format(len(urls)-len(res)))
print("the percentage between them:{}%".format(len(res)/(len(urls))*100))


for lo in res:
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

    if len(li)==1:
        pass
    else:
        li.append(0)  

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
        "gif_video":si[0]
    }        

    info.insert_one(dic)