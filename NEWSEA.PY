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
driver.implicitly_wait(10)

print("--->title",driver.title)


#/html/body/div/div[1]/main/div/div/div[2]/div/div/div[1]/aside/div/div[2]/div/div/div/div/div[2]/div[1]/section/div/div/input
driver.execute_script("window.scrollBy(0,300)","")
obj=driver.find_element_by_xpath("//input[@placeholder='Min']")
s=obj.send_keys("1.25")
obj=driver.find_element_by_xpath("//input[@placeholder='Max']")
s=obj.send_keys("3.25")

#button
#//button[@class='Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 cWgiBW kaikhX ActionButtonreact__StyledButton-sc-7jpoey-0 bwNKOH']
apply=driver.find_element_by_xpath("//button[@class='Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 fAtwh kaikhX ActionButtonreact__StyledButton-sc-7jpoey-0 bwNKOH']")
s=apply.click()

time.sleep(3)

#aricle
# //article[@class="Assetreact__DivContainer-sc-bnjqwy-0 gwTKfX Asset--loaded AssetSearchList--asset"]



#image url data
image_url=[]
while True:
    driver.execute_script("window.scrollBy(0,300)","")

    obj = driver.find_elements_by_xpath("//img[@class='Image--image']")
    for i in obj:
        img_src=i.get_attribute("src")
        image_url.append(img_src)
        print(img_src)
        

    if len(img_src)<5000:
        break 

""" 
<img class="Image--image" src="https://lh3.googleusercontent.com/xUgm8yFV61OGAtdBz73D5TZpNXsZJTYXjfjHKYZuW9poum0aChIxu6W1LquWXsj5JqCSuLuqfI1ypVau5byDWduhEdOZveDn7PKx=w333" style="object-fit: contain; width: auto; height: auto; border-radius: 5px; max-width: 100%; max-height: 100%;">    
 """
""" 
lisst=[]
condition= True

while condition :
    obj = driver.find_elements_by_xpath("//*[@id='__next']/div[1]/main/div/div/div/div[2]/div/div[5]/div/div/div/div/div/div/div[2]/div/div[2]/div[3]/div/a/self::a")
    
    for ai in obj:
        #print(obj)
        out = obj.text
        lisst.append(out)
        print(lisst)  """
#1.collection
#//div[@class='AssetCardFooter--collection']
#//a[@class='Linkreact__StyledA-sc-18se2b0-0 iWVmEt AssetCardFooter--collection-name']
li=[]
txt=i.text
while True:
    driver.execute_script("window.scrollBy(0,200)","")

    col = driver.find_elements_by_xpath("//a[@class='Linkreact__StyledA-sc-18se2b0-0 iWVmEt AssetCardFooter--collection-name']")
    for i in col:
        txt=i.text
        li.append(txt)
        print(txt)
        

    if len(txt)<5000:
        #print(len(text1))
        break  



#2.name
#//div[@class='AssetCardFooter--name']
name=[]
name1=i.text
while True:
    driver.execute_script("window.scrollBy(0,200)","")

    nam = driver.find_elements_by_xpath("//div[@class='AssetCardFooter--name']")
    for i in nam:
        name1=i.text
        name.append(name1)
        print(name1)
        

    if len(name1)<5000:
        #print(len(name1))
        break 

#3.bid value
# //div[@class='Overflowreact__OverflowContainer-sc-10mm0lu-0 fqMVjm Price--amount']
bid_value=[]    
while True:
    driver.execute_script("window.scrollBy(0,200)","")

    bid_ = driver.find_elements_by_xpath("//div[@class='Overflowreact__OverflowContainer-sc-10mm0lu-0 fqMVjm Price--amount']")
    for i in bid_:
        sad=i.text
        bid_value.append(sad)
        print(sad)
        

    if len(sad)<5000:
        #print(len(sad))
        break 

#4.type of bid
# //div[@class='AssetCardFooter--price-header']  
type_bid=[]  
while True:
    driver.execute_script("window.scrollBy(0,200)","")

    type_bi = driver.find_elements_by_xpath("//div[@class='AssetCardFooter--price-header']")
    for i in type_bi:
        na=i.text
        type_bid.append(na)
        print(na)
        

    if len(na)<5000:
        #print(len(na))
        break 

#5.favorite
#//div[@class="Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 FlexVerticalreact__FlexVertical-sc-x35rw8-0 VerticalAlignedreact__VerticalAligned-sc-1v4gkkl-0 beUSAq jYqxGr gXnSUK gJMdLt"]
#//span[@class='Blockreact__Block-sc-1xf18x6-0 Textreact__Text-sc-1w94ul3-0 jEeFPO gwsEKa']


#//div[@class='Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 FlexVerticalreact__FlexVertical-sc-x35rw8-0 VerticalAlignedreact__VerticalAligned-sc-1v4gkkl-0 beUSAq jYqxGr gXnSUK gJMdLt'] 
#//div[@class='Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 FlexVerticalreact__FlexVertical-sc-x35rw8-0 VerticalAlignedreact__VerticalAligned-sc-1v4gkkl-0 fAzvQd jYqxGr gXnSUK gJMdLt']
fav=[]
while True:
    driver.execute_script("window.scrollBy(0,200)","")

    fA = driver.find_elements_by_xpath("//div[@class='Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 FlexVerticalreact__FlexVertical-sc-x35rw8-0 VerticalAlignedreact__VerticalAligned-sc-1v4gkkl-0 fAzvQd jYqxGr gXnSUK gJMdLt']")
    for i in fA:
        s=i.text
        fav.append(s)
        print(s)
        

    if len(s)<1000:
        #print(len(s))
        break    

#token

# //a[@class='Linkreact__StyledA-sc-18se2b0-0 iWVmEt Asset--anchor']
tok=[]
for j in range(100):
    #driver.execute_script("window.scrollBy(0,200)","")

    Tk = driver.find_elements_by_xpath("//a[@class='Blockreact__Block-sc-1xf18x6-0 fAtwh AssetsSearchView--assets']")
    #Blockreact__Block-sc-1xf18x6-0 fAtwh AssetsSearchView--assets
    for i in Tk: #Linkreact__StyledA-sc-18se2b0-0 iWVmEt Asset--anchor
        da=i.get_attribute("href")
        tok.append(da)
        print(da)
        

    


""" dic={
    'image':image_url[0:4],
    'collection':li[0:4],
    'name':name[0:4],
    'type_of_bid':type_bid[0:4],
    'favourite':fav[0:4],
    'eth_value':bid_value[0:4],
    'token_id':tok[0:4]



}

print(dic)

 with open('openseaee.csv','w')as f:
    w=csv.DictWriter(f,dic.keys())
    w.writeheader() 
    
df =pd.DataFrame(dic)
print(df)
df.to_csv('sasea.csv',encoding='utf-8', index=False)      """