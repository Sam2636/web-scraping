#scopex webscraping script using python 

""" 
.........updated on 1/10/2021......

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

from webdriver_manager.chrome import ChromeDriverManager

# starting time
start = time.time()

# for driver we can download and specifiy the path or we can use the below code  
driver = webdriver.Chrome(ChromeDriverManager().install())

client =pymongo.MongoClient('mongodb://127.0.0.1:27017/')

my_db=client['webscrap']
info=my_db.scraping



driver.get("https://opensea.io/collection/art")
driver.maximize_window()
driver.implicitly_wait(2)
#time.sleep(2)  # Allow 2 seconds for the web page to open
scroll_pause_time = 1# You can set your own pause time. My laptop is a bit slow so I use 1 sec
screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
i = 1

urls = []

for j in  range(0,100):

    # scroll one screen height each time
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
    i += 1 
    time.sleep(scroll_pause_time)
    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    scroll_height = driver.execute_script("return document.body.scrollHeight;")  
    # Break the loop when the height we need to scroll to is larger than the total scroll height
    if (screen_height) * i > scroll_height:
        break       #break 

##### Extract Reddit URLs #####
    #urls = []
    soup = BeautifulSoup(driver.page_source, "html.parser")
    #for parent in soup.find_all(class_="Blockreact__Block-sc-1xf18x6-0 ctiaqU AssetsSearchView--assets"):
    for parent in soup.find_all(class_="Blockreact__Block-sc-1xf18x6-0 CarouselCardreact__Container-sc-152cap8-0 dBFmez gXWVJK"):
    #for parent in soup.find_all(class_="Assetreact__DivContainer-sc-bnjqwy-0 gwTKfX Asset--loaded AssetSearchList--asset"):
        #a_tag = parent.find("a", class_="styles__StyledLink-sc-l6elh8-0 cnTbOd Asset--anchor")
        a_tag = parent.find("a", class_="styles__StyledLink-sc-l6elh8-0 cnTbOd CarouselCard--main CollectionCardreact__Card-sc-1b2ne4j-0 fyrXjw")
        base = "https://opensea.io/collection/art"
        link = a_tag.attrs['href']
        url = urljoin(base, link)
        urls.append(url)

    print(len(urls))    
print('this is',len(urls))   

res = []
for i in urls:
    if i not in res:
        res.append(i)
  
# printing list after removal 
print ("The list after removing duplicates : " + str(res))
print(len(urls))
print(len(res))
print("the difference between them are:{}".format(len(urls)-len(res)))
print("the percentage between them:{}%".format(len(res)/(len(urls))*100))
print(res)

#class="styles__StyledLink-sc-l6elh8-0 cnTbOd Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 bhqEJb gMiESj

href="/assets?search[categories][0]=art"
