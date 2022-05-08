#scopex webscraping script using python 

""" 
.........updated on 28/9/2021......

.........@sam dhana seelan.........
 """
import time
import pymongo
import json
import csv
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

client =pymongo.MongoClient('mongodb://127.0.0.1:27017/')

my_db=client['webscrap']
info=my_db.scraping

#linkh
#ttps://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/50716606926351936545989127578619942776318611459452381668329158217369493962753
#https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/3237216513819739365483939717988508378265798769752999342574546421236663058433
#https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/50716606926351936545989127578619942776318611459452381668329158309728470695937
#https://opensea.io/assets?search[query]=blitmap
#s=driver.get('https://opensea.io/collection/art')

#fine test case
s=driver.get('https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/3237216513819739365483939717988508378265798769752999342574546421236663058433')
#s=driver.get('https://opensea.io/assets?search[query]=blitmap')
driver.maximize_window()
tok=[] 
       
#tok=[]
#styles__StyledLink-sc-l6elh8-0 cnTbOd Asset--anchor   # 14/9/2021
#Tk = driver.find_elements_by_xpath("//a[@class='Linkreact__StyledA-sc-18se2b0-0 iWVmEt Asset--anchor']")
Tk = driver.find_elements_by_xpath("//a[@class='styles__StyledLink-sc-l6elh8-0 cnTbOd Asset--anchor']")
for i in Tk: #Linkreact__StyledA-sc-18se2b0-0 iWVmEt Asset--anchor
    da=i.get_attribute("href")
    tok.append(da)
    print(da)

for i in tok:
    s=driver.get(str(i))
    #time.sleep(1)
    driver.implicitly_wait(1)
        
    driver.maximize_window()
    

    val =re.compile(r'0x[a-zA-Z0-9]+')
    name = val.findall(i)
    print(name)


    #get title
    #time.sleep(1)
    driver.implicitly_wait(1)
    T=driver.title
    print("--->title",driver.title)

    """ 
    val =re.compile(r'0x[a-zA-Z0-9]+')
    name = val.findall(s)
    print(name) """

    #header //section[@class='item--header']
    #print(header_dic) 
    #0----> collection
    #5----> nft name
    section= driver.find_elements_by_xpath("//section[@class='item--header']")
    for i in section:
        header=i.text.splitlines()
    #time.sleep(1) 
    driver.implicitly_wait(1)

    #created by
    #//section[@class='item--creator']
    #1--------> created by
    secti= driver.find_elements_by_xpath("//section[@class='item--creator']")
    for i in secti:
        heade=i.text.splitlines()
    #time.sleep(3) 
    driver.implicitly_wait(1)
    #print(heade)


    #owend by //section[@class='item--counts']
    #while accessing the element using list
    #1------> owend by whom
    #3-------> no,of views
    #5------->no.of favourite
    section= driver.find_elements_by_xpath("//section[@class='item--counts']")
    for i in section:
        owner=i.text.splitlines()
        
        fav =re.compile(r'\d+\sfavorite')     #favorite bug fix
        z = fav.findall(owner[-1])
        
        faaa =re.compile(r'[0-9\.\-]+k|[0-9]+')   #[0-9]+
        v = faaa.findall(owner[-1])

        sas =re.compile(r'[0-9\.\-]+k|[0-9]+')   #[0-9]+
        p = sas.findall(owner[3])


        if len(z)==0:
            owner.append('0')
        else:
            pass 
    #time.sleep(1) 
    driver.implicitly_wait(1)



    #print(sales_dic)
    #2----->no.of day sale ends in
    #3------>duration
    #6----->minimum bid value
    #7------>bid in usd

    #this is for 2&3
    sect= driver.find_elements_by_xpath("//div[@class='TradeStation--header']")
    if len(sect)!=0: 
    #print(sales)
        for i in sect:
            sales=i.text.splitlines()
            print(sales)
        #print(i.text)
        #time.sleep(3)
        driver.implicitly_wait(1)  
    else:
        sales=[0,0,0,0]   

    #1 &2
    sectio= driver.find_elements_by_xpath("//div[@class='TradeStation--main']")
    #//div[@class='item--frame']
    #//section[@class='Blockreact__Block-sc-1xf18x6-0 Framereact__Frame-sc-139h1ex-0 fAtwh eoqSMa']
    if len(sectio)!=0:
        for i in sectio:    
            sales1=i.text.splitlines()
            #print(i.text)
            #time.sleep(3) 
            driver.implicitly_wait(1)
            print(sales1)
            if sales[2]!="sa":
                sales1.append('no_value')
    else:
        sales1=[0,0,0,0]   


    #image    
    obj = driver.find_elements_by_xpath("//img[@class='Image--image']")
    li=[]
    for w in obj:
        img_src=w.get_attribute("src")
        li.append(img_src)
    
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


    #trading history
        
    elems = driver.find_elements_by_xpath("//div[@class='Scrollbox--content']")
    for elem in elems:
        print(elem.text.replace('\n'," ")) 
        f=elem.text.replace('\n'," ")
        #time.sleep(1) 
        driver.implicitly_wait(1) 

    #######case_2       #[a-zA-Z0-9_\-\.]+    #this is the perfect regex for capturing the id
    #Trading history
    sall =re.compile(r'Sale\s\d+.\d+\s[a-zA-Z0-9_\-\.]+\s[a-zA-Z0-9_\-\.]+\s\w+\s\w+\s\w+')     #sale
    trans =re.compile(r'Transfer\s[a-zA-Z0-9_\-\.]+\s[a-zA-Z0-9_\-\.]+\s\w+\s\w+\s\w+')     #tranfer
    minn =re.compile(r'Minted\sNullAddress\s[a-zA-Z0-9_\-\.]+\s\w+\s\w+\s\w+')     #minted
    bidd = re.compile(r'Bid\s[0-9\.\-]+\s[a-zA-Z0-9_\-\.]+\s[a-zA-Z0-9_\-\.]+\s\w+\s\w+')     #biding details
    bidd_time=re.compile(r'\sday|\smonth|\s[0-9]+\s\w+')

    z = sall.findall(f)
    x = trans.findall(f)
    c = minn.findall(f)
    po= bidd.findall(f)
    print(po)
    d=[word for line in po for word in line.split()]

    if len(po)!=0:
        ko= bidd_time.findall(po[0])
        if len(po)==1:
            kl= [0,0]
        if len(po)==2:
            kl= bidd_time.findall(po[1])
        if len(po)==3:
            kl= bidd_time.findall(po[1])    
    else:
        ko=[0,0]  
        kl=[0,0]
    #ko= bidd_time.findall(po[0])

    if len(po)!=0:
        lk=d[1]
        pk=d[2]
        if len(po)==1:
            lk1=0
            pk1='none'
        if len(po)==2:
            lk1=d[7]
            pk1=d[8]
        if len(po)==3:
            """ lk=d[1]
            pk=d[2] """
            lk1=d[7]
            pk1=d[8]     
    else:
        lk=0
        pk='none' 
        lk1=0
        pk1='none'


    print(len(z))    #whether we have to use the try expect method or not.
    if len(z)==0:
        z=['no-value','no_value']
    else:  
        pass 
    if len(x)==0:
        x=['no-value','no_value']
    else:  
        pass
    if len(c)==0:
        c=['no-value','no_value']
    else:  
        pass 
    if len(po)==0:
        po=['no-value','no_value']
    else:  
        pass 


    header_dic={
        "collection_name":header[0],
        "Name_of_NFT":T,
        "Created_by":heade[1],
        "owned_by":owner[1],
        "views":p[0] ,#owner[3],
        "favorite":v[0],#owner[-1],
        "sale_ends_in":sales[2],
        "Duration":sales[3],
        "Minimum_bid_value":sales1[1],
        "Bid_value_in_USD":sales1[2],
        "NFT_image":li[0],
        "Gif_video":si[0],
        "Token_id":name[0],
        "Trading_Sale":z[0],
        "Trading_Transfer":x[0],
        "Trading_Minted":c[0],
        "Trading_Bid":po[0],
        #"Trading_Bid":po[1],
        "1st Bid":pk,
        "2nd Bid":pk1,
        "1st Bid value_eth":lk,
        "2nd Bid value_eth":lk1,
        "1st Bid_time":ko[0],
        "2nd Bid_time_2":kl[0]
    }

    print(header_dic)

    info.insert_one(header_dic)


#right before quitting
#time.sleep(1)
driver.implicitly_wait(1)
driver.quit()
