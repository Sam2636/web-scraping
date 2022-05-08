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
#driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
driver = webdriver.Chrome(ChromeDriverManager().install())

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

#ant-dropdown-trigger ant-dropdown-link
element = driver.find_element_by_xpath("//span[@class='ant-dropdown-trigger ant-dropdown-link']")[1]
element.click()