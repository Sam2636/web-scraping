
import re
import time
import pymongo
import json
import re
import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import pyperclip as pc

from webdriver_manager.chrome import ChromeDriverManager
""" options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors') """
#driver = webdriver.Chrome(chrome_options=options)


driver = webdriver.Chrome(ChromeDriverManager().install())

client =pymongo.MongoClient('mongodb://127.0.0.1:27017/')

my_db=client['webscrap']
info=my_db.scraping






#https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/3237216513819739365483939717988508378265798769752999342574546422336174686209


driver.maximize_window()
#get title
time.sleep(3)

#s=driver.get('https://opensea.io/Tidyyy')
s=driver.get('https://opensea.io/assets/matic/0x2953399124f0cbb46d2cbacd8a89cf0599974963/112236847829549195725252796510137205911281236528816072847126752522814462361601/')

llii=[]
apply=driver.find_element_by_xpath("//a[@class='styles__StyledLink-sc-l6elh8-0 ekTmzq AccountLink--ellipsis-overflow']")
img_src=apply.get_attribute("href")
llii.append(img_src)




for llo in llii:
    s=driver.get(str(llo))
    #time.sleep(2)
    driver.implicitly_wait(1)
        
    driver.maximize_window()

    apply=driver.find_element_by_xpath("//button[@class='UnstyledButtonreact__UnstyledButton-sc-ty1bh0-0 TextCopierreact__StyledContainer-sc-ga2cnk-0 btgkrL AccountHeader--address']")
    s=apply.click()
    
    wallet_address=pc.paste()
    print(pc.paste())
    print(s) 

    driver.implicitly_wait(10)

    driver.back()



#wallet address

#//div[@class='AccountHeader--subtitle']

