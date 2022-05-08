import time
import json
import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

#website 
driver.get('https://opensea.io/collection/art')
driver.maximize_window()
#get title
time.sleep(5)

print("--->title",driver.title)

#bot automation process
driver.execute_script("window.scrollBy(0,300)","")
#min value
obj=driver.find_element_by_xpath("//input[@placeholder='Min']")
s=obj.send_keys("1.25")
#max value
obj=driver.find_element_by_xpath("//input[@placeholder='Max']")
s=obj.send_keys("3.25")

#button
#//button[@class='Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 cWgiBW kaikhX ActionButtonreact__StyledButton-sc-7jpoey-0 bwNKOH']
apply=driver.find_element_by_xpath("//button[@class='Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 fAtwh kaikhX ActionButtonreact__StyledButton-sc-7jpoey-0 bwNKOH']")
s=apply.click()

time.sleep(5)


#list creation        
image_url=[]      #1.image url data
collection=[]     #2.collection
name=[]           #3.name
bid_value=[]      #4.bid value
type_bid=[]       #5.type_of_bid
fav=[]            #6.favorite
tok=[]            #7.token

#relative x-path
img= driver.find_elements_by_xpath("//img[@class='Image--image']")    #1.image
col = driver.find_elements_by_xpath("//a[@class='Linkreact__StyledA-sc-18se2b0-0 iWVmEt AssetCardFooter--collection-name']") #2.collection
nam = driver.find_elements_by_xpath("//div[@class='AssetCardFooter--name']")                                                 #3.name
bid_ = driver.find_elements_by_xpath("//div[@class='Overflowreact__OverflowContainer-sc-10mm0lu-0 fqMVjm Price--amount']")   #4.bid value
type_bi = driver.find_elements_by_xpath("//div[@class='AssetCardFooter--price-header']")                                     #5.type of bid
fA = driver.find_elements_by_xpath("//div[@class='Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 FlexVerticalreact__FlexVertical-sc-x35rw8-0 VerticalAlignedreact__VerticalAligned-sc-1v4gkkl-0 fAzvQd jYqxGr gXnSUK gJMdLt']")  #6.favorite
Tk = driver.find_elements_by_xpath("//a[@class='Linkreact__StyledA-sc-18se2b0-0 iWVmEt Asset--anchor']")  #7.token

""" #converting into text
img_src=img.get_attribute("src")
txt=col.text
NamA=nam.text
Bi_V=bid.text
Bit_TY=type_bi.text
FAV=fA.text
da=Tk.get_attribute("href") """


n=50,000
while True:
    driver.execute_script("window.scrollBy(0,100)","")
    
    for i in img:
        img_src=img.get_attribute("src")
        image_url.append(img_src)
    for j in col:
        txt=col.text
        collection.append(txt)
    for k in nam: 
        NamA=nam.text  
        name.append(NamA)
    for l in bid_:
        Bi_V=bid.text
        bid_value.append(Bi_v)
    for m in type_bi:
        Bit_TY=type_bi.text
        type_bid.append(Bit_TY)
    for o in  fA:
        FAV=fA.text
        fav.append(FAV)
    for p in Tk:
        da=Tk.get_attribute("href")
        tok.append(da)       


"""  for i in img:        
        #appending to the list
        image_url.append(img_src)
        collection.append(txt)
        name.append(NamA)
        bid_value.append(Bi_v)
        type_bid.append(Bit_TY)
        fav.append(FAV)
        tok.append(da)
        

    if len(image_url,txt,NamA,Bi_V,Bit_TY,FAV,da)<n:
        break """


dic={
    'image':image_url,
    'collection':collection,
    'name':name,
    'type_of_bid':type_bid,
    'favourite':fav,
    'eth_value':bid_value,
    'token_id':tok

}        
 
print(dic)




