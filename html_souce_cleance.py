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
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import firefox
import pyperclip as pc

# starting time
start = time.time()

# for driver we can download and specifiy the path or we can use the below code  
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://solscan.io/collection/79a99300ed82221e283ac89e6b14bc809811ef2f41a3d57066357ccd0a72bdc7")
#driver.get("https://rarity.tools/thedudes")

""" client =pymongo.MongoClient('mongodb+srv://aiotylabs:aiotylabs2020!@cluster0.zpris.mongodb.net/test')

my_db=client['webscrap']
mycol = my_db["nft_links_new_collection_21"]
info=my_db.scrap_3

"""

driver.maximize_window()
driver.delete_all_cookies()
driver.refresh()

time.sleep(10)

driver.implicitly_wait(2)




""" elem = driver.find_element_by_xpath("//*")
source_code = elem.get_attribute("outerHTML")

print(source_code) """

SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

#//button[@class='ant-btn sc-kigVQd ZNdwF']

#driver.findElement(By.name("submit")).sendKeys(Keys.ENTER);


#image    --------------->test pass
#obj = driver.find_elements_by_xpath("//td[@class='font-bold text-left text-pink-600']/a")
obj = driver.find_elements_by_xpath("//div[@class='ant-list-item ant-list-item-no-flex nft-item']/a")
li=[]
for w in obj:
    img_src=w.get_attribute("href")
    li.append(img_src)
if len(li)==1:
    pass
else:
    li.append(0)


print(li)
print(len(li)) 
#source_code_in = elem.get_attribute("innerHTML")


element = driver.find_element_by_xpath("//button[@class='ant-btn sc-kigVQd ZNdwF']")
element.click()



""" 
source_code.replace(" ","")
source_code.replace("\n","") """

#print(source_code)
#sa = re.sub(r"\s+", "", source_code, flags=re.UNICODE)
#print(sa)
#dc="xweeee"

""" f = open("nxt.txt", "a")
f.write(source_code)
f.close()
 """




#a="""{}""".format(source_code)

#print("dwdwd",a)

s="""</div> <div class="px-2 mx-1 mb-0 text-lg font-extrabold text-green-500 bg-white rounded-md dark:bg-gray-800">
							30940.33
						</div> <div class="px-4 mb-1 mt-0.5 text-xs font-normal text-pink-200">"""


d="""</div></div> <div class="mb-1"><div><div class="flex flex-row items-baseline px-1 overflow-hidden text-sm"><div class="flex-grow font-medium">
			Emission<!----></div> <!----> <div class="pl-1 text-base text-right text-green-500">
				+5952.38
			</div></div> <div class="""


""" fave =re.compile(r'flex flex-row items-baseline px-1 overflow-hidden text-sm"><div class="flex-grow font-medium">(\s*(\w+))|(\s*(\w+).\d+)<!----></div>')
sdf=re.compile(r'pl-1 text-base text-right text-green-500">\s*\+(\d+.\d+)\s*</div></div> <div class=')
#sdf=re.compile(r'pl-1 text-base text-right text-green-500">(.*)</div></div> <div class=')

ze = fave.findall(source_code)
df=sdf.findall(source_code)
print("---->name",ze)
print("---->value",df,type(df)) """



#b=[]
""" fav =re.compile(r'</div> <div class="px-2 mx-1 mb-0 text-lg font-extrabold text-green-500 bg-white rounded-md dark:bg-gray-800">\s*(\d+.\d+)\s*</div>')
z = fav.findall(source_code)
print("veverv",z)
print("cwrevev",type(source_code))

fava =re.compile(r'\d+.\d+')
d = fava.findall(z[0])
print(d) """
#b.append(z)
""" 
for i in b:
    if i== '30940.33':
        print("hgv jhn")
    else:
        print("hell no")
    
print(i[0]) """
#print(z)




#print(li[0]) 









""" secti= driver.find_elements_by_xpath("//div[@class='flex-grow font-extrabold']")
for i in secti:
    heade=i.text.splitlines()

    print(heade)   
 """

""" 
for j in  range(0,200):

    # scroll one screen height each time
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
    i += 1 
    time.sleep(scroll_pause_time)
    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    scroll_height = driver.execute_script("return document.body.scrollHeight;")  
    # Break the loop when the height we need to scroll to is larger than the total scroll height
    if (screen_height) * i > scroll_height:
        pass       #break 
 """

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

""" 
#print(urls[0:25])

    
        #image    --------------->test pass
    obj = driver.find_elements_by_xpath("//div[@class='overflow-hidden rounded-md m-0.5']/a")
    li=[]
    for w in obj:
        img_src=w.get_attribute("href")
        li.append(img_src)
    if len(li)==1:
        pass
    else:
        li.append(0)
    print(li)
print(len(li))     """



""" #image    --------------->test pass
obj = driver.find_elements_by_xpath("//div[@class='relative overflow-hidden rounded-xl']//img")
li=[]
for w in obj:
    img_src=w.get_attribute("href")
    li.append(img_src)
if len(li)==1:
    pass
else:
    li.append(0)
print(li[1])  """

""" 
#contract_details

#//a[@data-bn-type='link']
obj = driver.find_elements_by_xpath("//a[@data-bn-type='link']")
lpi=[]
for w in obj:
    img_src=w.get_attribute("href")
    lpi.append(img_src)
if len(lpi)==1:
    pass
else:
    lpi.append(0)
print(lpi)
#//div[@class='css-2czx7p'] """

""" 

#token_standard
elem = driver.find_element_by_xpath("//*")
source_code = elem.get_attribute("outerHTML")

#css-24c0g9">100300216622</div>
sas =re.compile(r'css-24c0g9">[0-9]+</')   #[0-9]+
pia= sas.findall(source_code)
#--------->
token_id=re.compile(r'[0-9]+') 
sa=token_id.findall(pia[0])
print("Token_id:",sa[-1])



#history

sectir= driver.find_elements_by_xpath("//div[@class='css-65a3ga']")
for i in sectir:
    header=i.text.splitlines()

print(header)    


#description
#//span[@class='short-text']
sectiry= driver.find_elements_by_xpath("//div[@class='css-1sdv4ev']")
for i in sectiry:
    headery=i.text.splitlines()

print(headery) """    
 





#image    --------------->test pass
""" obj = driver.find_elements_by_xpath("//div[@class='overflow-hidden rounded-md m-0.5']/a")
li=[]
for w in obj:
    img_src=w.get_attribute("href")
    li.append(img_src)
if len(li)==1:
    pass
else:
    li.append(0)
print(li[1])  """

time.sleep(4)

driver.close()
