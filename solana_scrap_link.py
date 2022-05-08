#scopex webscraping script using python 

""" 
.........updated on 7/10/2021......

.........@sam dhana seelan.........
 """

#imports
from sys import _clear_type_cache
import time
from selenium import webdriver
import pymongo
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.options import Options  
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import TimeoutException

chrome_options = Options()  
chrome_options.add_argument("--headless") 
# for driver we can download and specifiy the path or we can use the below code  
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)

#driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"), chrome_options=chrome_options)  
driver.get("https://solscan.io/collection/79a99300ed82221e283ac89e6b14bc809811ef2f41a3d57066357ccd0a72bdc7")
#driver.get("https://rarity.tools/thedudes")


#db
client =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')

my_db=client['solscrap']
mycol = my_db["nft_links_new_collection_21"]
info=my_db.sol_test1


driver.maximize_window()
driver.delete_all_cookies()
driver.refresh()

time.sleep(10)

driver.implicitly_wait(2)


def scroll():
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

    #//button[@class='ant-btn sc-kigVQd ZNdwF']

        if new_height == last_height:
            break
        last_height = new_height

li=[]
res=[]
def get_link():    
    obj = driver.find_elements_by_xpath("//div[@class='ant-list-item ant-list-item-no-flex nft-item']/a")
    for w in obj:
        img_src=w.get_attribute("href")
        li.append(img_src)
    if len(li)==1:
        pass
    else:
        pass

def start():
    time.sleep(10)
    scroll()
    get_link()
    element = driver.find_element_by_xpath("//button[@class='ant-btn sc-kigVQd ZNdwF']")
    element.click()


''' def get_clear_browsing_button(driver):
    """Find the "CLEAR BROWSING BUTTON" on the Chrome settings page."""
    return driver.find_element_by_css_selector('* /deep/ #clearBrowsingDataConfirm')
 '''


''' def clear_cache(driver, timeout=60):
    """Clear the cookies and cache for the ChromeDriver instance."""
    # navigate to the settings page
    driver.get('chrome://settings/clearBrowserData')

    # wait for the button to appear
    wait = WebDriverWait(driver, timeout)
    wait.until(get_clear_browsing_button)

    # click the button to clear the cache
    get_clear_browsing_button(driver).click()

    # wait for the button to be gone before returning
    wait.until_not(get_clear_browsing_button)
 '''


for i in range(0,10):
    count=0
    try:
        for i in range(0,10):
            start()   
            count=count+1
            print("---------",count)
            #clear_cache(driver)
        for re in li:
            if re not in res:
                res.append(re)

        print("-------->RES",len(res))
        print("-------->LI",len(li))
        for jk in res:
            dicer={
            "slug":jk
            }
            #info.insert(dicer)       

    except (NoSuchWindowException,TimeoutException):
        scroll()
        time.sleep(5)
        continue
        

    

    
  
    

driver.close()
