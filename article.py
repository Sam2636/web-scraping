import time
import pymongo
import json
import re
import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

client =pymongo.MongoClient('mongodb://127.0.0.1:27017/')

my_db=client['webscrap']
info=my_db.scraping

#website 
driver.get('https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/50716606926351936545989127578619942776318611459452381668329158217369493962753')

driver.maximize_window()
#get title
time.sleep(3)

print("--->title",driver.title) 


""" txt='https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/3237216513819739365483939717988508378265798769752999342574546421236663058433'
val =re.compile(r'.0x.')
name = val.findall(txt)
print(name) """



#header //section[@class='item--header']
#eader=[]
head= driver.find_elements_by_xpath("//section[@class='item--header']")
for i in head:
    #print(i.text)
    header=i.text.splitlines()
    #header.append(i.text.split())
    #print(i.text)
time.sleep(3) 
print(header)
#print(s)
#print(len(header))


#print(header_dic) 
#0----> collection
#5----> nft name

#owend by //section[@class='item--counts']
#owner=[]
own= driver.find_elements_by_xpath("//section[@class='item--counts']")
for i in own:
    owner=i.text.splitlines()
    #print(i.text)
time.sleep(3) 

#while accessing the element using list
#1------> owend by whom
#3-------> no,of views
#5------->no.of favourite



#sales=[]
sal= driver.find_elements_by_xpath("//section[@class='Blockreact__Block-sc-1xf18x6-0 Framereact__Frame-sc-139h1ex-0 fAtwh eoqSMa']")
#//section[@class='Blockreact__Block-sc-1xf18x6-0 Framereact__Frame-sc-139h1ex-0 fAtwh eoqSMa']
#sales=i.text.splitlines()
for i in sal:
    print(i.text)
    sales=i.text.splitlines()
    #print(i.text)
time.sleep(3) 
#print(sales)


#print(sales_dic)
#2----->no.of day sale ends in
#3------>duration
#6----->minimum bid value
#7------>bid in usd


""" #details
#//div[@class='Panel--isContentPadded item--details'
ji=[]
details=driver.find_elements_by_xpath("//div[@class='Scrollboxreact__DivContainer-sc-1b04elr-0 ddtCpj EventHistory--container']")
for j in details:
    ji.append(j.text)
    #print(j.text)
print(ji) """
#image    
obj = driver.find_elements_by_xpath("//img[@class='Image--image']")
li=[]
for w in obj:
    img_src=w.get_attribute("src")
    li.append(img_src)   
    #print(img_src)
#print(li[0])

header_dic={
    "collection_name":header[0],
    "Name_of_NFT":header[5],
    "owned_by":owner[1],
    "views":owner[3],
    "favourite":owner[5],
    "sale_ends_in":sales[2],
    "Duration":sales[3],
    "Minimum_bid_value":sales[6],
    "Bid_value_in_USD":sales[7],
    "NFT_image":li[0]
}

print(header_dic)

info.insert_one(header_dic)


""" owner_dic={
    "owned_by":owner[1],
    "views":owner[3],
    "favourite":owner[5]
}

sales_dic={
    "sale_ends_in":sales[2],
    "Duration":sales[3],
    "Minimum_bid_value":sales[6],
    "Bid_value_in_USD":sales[7]

}
img_dic={
    "NFT_image":li[0]
} """

#print(img_dic)

"""  #table content
table=driver.find_elements_by_xpath("//div[@class='Scrollboxreact__DivContainer-sc-1b04elr-0 ddtCpj EventHistory--container']")
for j in table:
    print(j.text)

#listing
#//div[@class='Blockreact__Block-sc-1xf18x6-0 fPlcKL']
lis=driver.find_elements_by_xpath("//div[@class='Panelreact__DivContainer-sc-1u1w6l0-0 cgdOoN Panel--isOpen item--frame item--orders']")
for k in lis:
    print(k.text) """
  

#article
""" # //article[@class="Assetreact__DivContainer-sc-bnjqwy-0 gwTKfX Asset--loaded AssetSearchList--asset"]
Article = driver.find_elements_by_xpath("//article[@class='Assetreact__DivContainer-sc-bnjqwy-0 gwTKfX Asset--loaded AssetSearchList--asset']")
#print(Article[0].text)
link= driver.find_elements_by_xpath("//div[@class='AssetMediareact__DivContainer-sc-1vbfbdi-0 fOInxz']")
obj = driver.find_elements_by_xpath("//img[@class='Image--image']") """
""" while True:
    driver.execute_script("window.scrollBy(0,50)","")
    for i in Article:
    #Article = driver.find_elements_by_xpath("//article[@class='Assetreact__DivContainer-sc-bnjqwy-0 gwTKfX Asset--loaded AssetSearchList--asset']")

        print(i.text)
        for j in obj:
            img_src=j.get_attribute("src")
            #image_url.append(img_src)
            print(img_src) """
    
        
        


""" for j in link:
        da=j.get_attribute("src")
        print(da)  """


#link= driver.find_elements_by_xpath("//div[@class='Imagereact__DivContainer-sc-dy59cl-0 eWQHeU Image--fade Image--isImageLoaded Image--isImageLoaderVisible AssetMedia--img']")
#link= driver.find_elements_by_class_name('Image--image')


""" p=driver.find_element_by_xpath("//article[@class='Assetreact__DivContainer-sc-bnjqwy-0 gwTKfX Asset--loaded AssetSearchList--asset']")
pp=p
ppp=pp.find_element_by_xpath("")
print(ppp) """
""" for k in p:
    print(k.text) """
#s=p.find_element_by_xpath("//img[@class='Image--image']")
#da=s.get_attribute("src")

#print(link) 
""" li=link.find_element_by_tag_name("img")
s=li.get_attribute('src')
print(s) """
#print(link)
""" for j in link:
        da=j.get_attribute("src")
        print(da) """

#//div[@class='item__DivContainer-sc-3o5may-0 MEuu']        
""" pg_content=driver.find_elements_by_xpath("//div[@class='item__DivContainer-sc-3o5may-0 MEuu']")
for j in pg_content:
    print(j.text)  """

#//div[@class='Imagereact__DivContainer-sc-dy59cl-0 eWQHeU Image--fade Image--isImageLoaded Image--isImageLoaderVisible AssetMedia--img']

""" q = driver.find_elements_by_xpath("//img[@class='Image--image']")
for i in q:
    img_src=i.get_attribute("src") 
    print(img_src)   """


#//a[@class='Linkreact__StyledA-sc-18se2b0-0 iWVmEt']    
#//div[@class='ChainInfo--label-value']

""" #/html/body/div[1]/div[1]/main/div/div/div/div[2]/div/section[3]/div/div[4]/div/div/div/div/div/div[1]/div[2]/a
w=driver.find_elements_by_xpath("/html/body/div[1]/div[1]/main/div/div/div/div[2]/div/section[3]/div/div[4]/div/div/div/div/div/div[1]/div[2]/a")
#da=w.get_attribute("href")
print(w)
#print(da)
for i in w:
        da=i.get_attribute("href")
        print(da) """

tok=[]
for j in range(100):
    #driver.execute_script("window.scrollBy(0,200)","")

    Tk = driver.find_elements_by_xpath("//a[@class='Blockreact__Block-sc-1xf18x6-0 fAtwh AssetsSearchView--assets']")
    #Blockreact__Block-sc-1xf18x6-0 fAtwh AssetsSearchView--assets
    for i in Tk: #Linkreact__StyledA-sc-18se2b0-0 iWVmEt Asset--anchor
        da=i.get_attribute("href")
        tok.append(da)
        print(da)
        
