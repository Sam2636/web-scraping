import time
import json
import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
 
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
#website 
driver.get('https://opensea.io/')

driver.maximize_window()

#driver.implicitly_wait(10)

#//span[contains(text(),'Art')]
action = ActionChains(driver)
 
time.sleep(3)
#obj=driver.find_element_by_xpath("/html/body/div[1]/div[1]/main/div/div/div[3]/div/div[2]/div[1]/a")
obj=driver.find_element_by_link_text('Art')
a=obj.click()
time.sleep(3)


""" for i in range(10):
    s=driver.execute_script("window.scrollBy(0,300)","")
    time.sleep(2) """
   
#contains the every article
""" s=driver.find_element_by_xpath("//div[@class='Blockreact__Block-sc-1xf18x6-0 fAtwh AssetsSearchView--assets']")
s.click() """

#contain particular article
#//article[@class='Assetreact__DivContainer-sc-bnjqwy-0 gwTKfX Asset--loaded AssetSearchList--asset']

for i in range(3):  
    first_image=driver.find_element_by_xpath("//article[@class='Assetreact__DivContainer-sc-bnjqwy-0 gwTKfX Asset--loaded AssetSearchList--asset']") #inside each nft
    first_image.click()  
    time.sleep(3)
    """ for j in range(3):
        driver.execute_script("window.scrollBy(0,100)","")
        time.sleep(3)  #wait to read the nft

    driver.execute_script("window.history.go(-1)") #come backs to the original page
    time.sleep(2)
    driver.execute_script("window.scrollBy(0,300)","")
    time.sleep(5)  #waits for 5 seconnd   """




""" tok=[]
Tk = driver.find_elements_by_xpath("//a[@class='Linkreact__StyledA-sc-18se2b0-0 iWVmEt Asset--anchor']")
for i in Tk:
    da=i.get_attribute("href")
    tok.append(da)  

print(tok) """

tok=[]
while True:
    driver.execute_script("window.scrollBy(0,200)","")

    Tk = driver.find_elements_by_xpath("//a[@class='Linkreact__StyledA-sc-18se2b0-0 iWVmEt Asset--anchor']")
    for i in Tk: #Linkreact__StyledA-sc-18se2b0-0 iWVmEt Asset--anchor
        da=i.get_attribute("href")
        tok.append(da)
        print(da)
        

    if len(da)<5000:
        #print(len(da))
        break 