from __future__ import print_function
import time
import pymongo
import json
import csv
import re
import pandas as pd
import sys
import requests
import traceback
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

#s=driver.get('https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/36531988286593147983804448989073758500561332652670036049955868525649979244545')
#s=driver.get('https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/3237216513819739365483939717988508378265798769752999342574546421236663058433')
#case1 testing for favourite
#s=driver.get('https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/36531988286593147983804448989073758500561332652670036049955868630103583883265')
#s=driver.get('https://opensea.io/assets/0x8d04a8c79ceb0889bdd12acdf3fa9d207ed3ff63/14')
#s=driver.get('https://opensea.io/assets/0x8d04a8c79ceb0889bdd12acdf3fa9d207ed3ff63/15')
#s=driver.get('https://opensea.io/assets/0x73107f9044c3d47d2f18157d21c22013ee9a7a75/33100010001')

#s=driver.get('https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/3237216513819739365483939717988508378265798769752999342574546444326407241729')
#s=driver.get('https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/3237216513819739365483939717988508378265798769752999342574546439928360730625')
#s=driver.get('https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/3237216513819739365483939717988508378265798769752999342574546487207360724993')
#https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/3237216513819739365483939717988508378265798769752999342574546423435686313985
#s=driver.get('https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/15895015057330088448162178390783740306176725729680512439011850406868413317121')
#s=driver.get('https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/5752995136057938273346403257999553327357952240033834925002187139107583426561')
#s=driver.get('https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/93469302660462583484690190998346915166105619251926010531368634891344440983553')
#s=driver.get('https://opensea.io/assets/0x25171b354f3e192ea4fb0c1268255d7a64448c91/7898')
#s=driver.get('https://opensea.io/assets/0x3ff1fb7eee1ee9b11e08473c1a59994f6f9a2d39/17800020007')
#s=driver.get('https://opensea.io/assets/0x78994e16f28e784c8f8ef75579b949a87fbcba77/18900030139')
#s=driver.get('https://opensea.io/assets/0x78994e16f28e784c8f8ef75579b949a87fbcba77/18900030019')
#s=driver.get('https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/40482595849772694285173713041642282097106100196042549765489074297924826955777')
#s=driver.get('https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/55575360221028374465659771733000318579577403829328624053715771786946234286081')
#s=driver.get('https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/34085485605809858234645056736246100833627908360907625323341299738449415241729')
#s=driver.get('https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/40482595849772694285173713041642282097106100196042549765489073842727013056513')
#s=driver.get('https://opensea.io/assets/0x9bfa45382268e4bacbd1175395728153dc5248f2/656')
#s=driver.get('https://opensea.io/newrafael?tab=created')

#s=driver.get('https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/80494307024529346018053650490912529916739680814770830097664395700848161718302')
s=driver.get('https://opensea.io/assets/0xc1caf0c19a8ac28c41fe59ba6c754e4b9bd54de9/8670')
#s=driver.get('https://opensea.io/assets/0x9f4292bd05a5c89f007bdef3a95fc32bc1021b99/2519')

#--------------------------->new error
#https://opensea.io/assets/0xa7d8d9ef8d8ce8992df33d8b8cf4aebabd5bd270/9000000  -------->something went wrong vm
#https://opensea.io/assets/0xa7d8d9ef8d8ce8992df33d8b8cf4aebabd5bd270/30000890    ------>error vm
#https://opensea.io/assets/0xa7d8d9ef8d8ce8992df33d8b8cf4aebabd5bd270/138000005 ------->errror   vm
#https://opensea.io/newrafael?tab=created   ------>error  vm
#https://opensea.io/0x46f8b522819a407da64474ca21d28a6b50aeac74?tab=created
#https://opensea.io/assets/0x22ca6c273d2d8be5bb11e762741efd67acdd3315/1619
#https://opensea.io/assets/0x2d0ee46b804f415be4dc8aa1040834f5125ebd2e/8642  ------------------>2 times
#https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/2206774564966433947166689696507183869586471703389774980152760912689758208001
#https://opensea.io/assets/0x15a2d6c2b4b9903c27f50cb8b32160ab17f186e2/9974
#https://opensea.io/assets/0x1897d69cc0088d89c1e94889fbd2efffcefed778/815

#p[0]-------->index out of range
#https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/2206774564966433947166689696507183869586471703389774980152760912689758208001
#https://opensea.io/assets/0x9bfa45382268e4bacbd1175395728153dc5248f2/656

# https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/2206774564966433947166689696507183869586471703389774980152760912689758208001
#pia[0]---------------> error
#https://opensea.io/assets/0x4d3814d4da8083b41861dec2f45b4840e8b72d68/1047741
#https://opensea.io/assets/0x27b4bc90fbe56f02ef50f2e2f79d7813aa8941a7/10376


#selenium.common.exceptions.TimeoutException
#s=driver.get(str(lo))

#apply click()
#https://opensea.io/assets/0x3f4a759e9a11f109c7970cef934d6753c1a5c43e/13000010158

#[25000:27000]:    error


#
try:

    tok=[]
        

    driver.maximize_window()
    #get title
    time.sleep(3)

    print("--->title",driver.title)

    """ 
    val =re.compile(r'0x[a-zA-Z0-9]+')
    name = val.findall(s)
    print(name) """


    #clearAll 
    # #//li[@class='EventHistory--filter-dropdown-clear']---------------------------------------->update
    sp="https://opensea.io/assets/0x9bfa45382268e4bacbd1175395728153dc5248f2/656"


    #token_id
    sa =re.compile(r'/[0-9]+')   #[0-9]+
    y= sa.findall(sp)
    lk=y[1]

    pa =re.compile(r'[0-9]+')   #[0-9]+
    mi= pa.findall(lk)
    print(mi)

    #token_standard
    elem = driver.find_element_by_xpath("//*")
    source_code = elem.get_attribute("outerHTML")
    #print(source_code)
    #print(source_code)
    sas =re.compile(r'ERC[0-9]+|ERC-[0-9]+')   #[0-9]+
    pia= sas.findall(source_code)
    print(pia[0])
    print(len(pia))

    #details of blockchain
    ash =re.compile(r'polygon|Ethereum|Klaytn|klaytn')   #[0-9]+
    kol = ash.findall(source_code)
    print(kol)
    print(kol[0])


    #header //section[@class='item--header']
    #print(header_dic) 
    #0----> collection
    #5----> nft name
    section= driver.find_elements_by_xpath("//section[@class='item--header']")
    for i in section:
        header=i.text.splitlines()
    #time.sleep(3) 
    driver.implicitly_wait(1)
    print(header)


    #created by
    #//section[@class='item--creator']
    #1--------> created by
    try:
        secti= driver.find_elements_by_xpath("//section[@class='item--creator']")

        for i in secti:
            heade=i.text.splitlines()             
        #time.sleep(3) 
            driver.implicitly_wait(1)
        print(heade)
    except :
        heade =['none','none'] 
        pass 





    #owend by //section[@class='item--counts']
    #while accessing the element using list
    #1------> owend by whom
    #3-------> no,of views
    #5------->no.of favourite
    section= driver.find_elements_by_xpath("//section[@class='item--counts']")
    """ for i in section:
        owner=i.text.splitlines()
        fav =re.compile(r'\d+\sfavorite')     #favorite bug fix
        z = fav.findall(owner[-1])
        if len(z)==0:
            owner.append('0 favorite')
        else:
            pass    
        print(z) """
        #section= driver.find_elements_by_xpath("//section[@class='item--counts']")
    for i in section:
        owner=i.text.splitlines()
        print(len(owner))
        print(owner)
        if len(owner)==2:
            owner.append('0')
            owner.append('0')
        else:
            pass 
        print(owner)
        fav =re.compile(r'\d+\sfavorite')     #favorite bug fix
        z = fav.findall(owner[-1])
        
        faaa =re.compile(r'[0-9\.\-]+k|[0-9]+')   #[0-9]+
        v = faaa.findall(owner[-1])

        sas =re.compile(r'[0-9\.\-]+k|[0-9]+')   #[0-9]+
        p = sas.findall(owner[3])
        if len(p)==0:
            p = sas.findall(owner[4])

        print(p)
        """ if len(owner)==2:
            owner.append('0')
        else:
            pass  """   
        #print(p)

        if len(z)==0:
            owner.append('0')
        else:
            pass 
        
        #time.sleep(1)
        driver.implicitly_wait(1) 
    #time.sleep(3) 
    driver.implicitly_wait(1)
    print(owner)



    #print(sales_dic)
    #2----->no.of day sale ends in
    #3------>duration
    #6----->minimum bid value
    #7------>bid in usd

    #this is for 2&3
    sect= driver.find_elements_by_xpath("//div[@class='TradeStation--header']")
    #//div[@class='item--frame']
    #//section[@class='Blockreact__Block-sc-1xf18x6-0 Framereact__Frame-sc-139h1ex-0 fAtwh eoqSMa']
    print(len(sect))
    #sect= driver.find_elements_by_xpath("//div[@class='TradeStation--header']")
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
    print(len(sectio))
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
        #print('this is not workng',) 




    #image    
    obj = driver.find_elements_by_xpath("//img[@class='Image--image']")
    li=[]
    for w in obj:
        img_src=w.get_attribute("src")
        li.append(img_src)

    print('this is image len:{}'.format(len(li)))    
    if len(li)==1:
        pass
    else:
        li.append(0) 

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


    #Trading History


    def Trading_History():
        elems = driver.find_elements_by_xpath("//div[@class='Scrollbox--content']")
        for elem in elems:
            #print(elem.text.replace('\n'," ")) 
            Trading_History.f=elem.text.replace('\n'," ")
            #time.sleep(1)  
            driver.implicitly_wait(1) 
    

        #clear_all
    try:    
        apply=driver.find_element_by_xpath("//div[@class='Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 FlexColumnreact__FlexColumn-sc-1wwz3hp-0 VerticalAlignedreact__VerticalAligned-sc-b4hiel-0 dBFmez jYqxGr ksFzlZ iXcsEj']")
        apply.click()
        # <div class="Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 FlexColumnreact__FlexColumn-sc-1wwz3hp-0 VerticalAlignedreact__VerticalAligned-sc-b4hiel-0 dBFmez jYqxGr ksFzlZ iXcsEj" bis_skin_checked="1"><button type="button" class="UnstyledButtonreact__UnstyledButton-sc-ty1bh0-0 btgkrL"><li class="EventHistory--filter-dropdown-clear">Clear All</li></button></div>
        driver.implicitly_wait(10)
        print("cleared_all")

        #Trading history
        time.sleep(2)
        Trading_History()

    except :
        pass
        print("no_clear_option")
        #Trading history
        Trading_History()

    print(Trading_History.f)
    #######case_2       #[a-zA-Z0-9_\-\.]+    #this is the perfect regex for capturing the id
    #Trading history
    sall =re.compile(r'Sale\s\[a-zA-Z0-9_\-\.]+\s[a-zA-Z0-9_\-\.]+\s[a-zA-Z0-9_\-\.]+\s\w+\s\w+\s\w+')     #sale
    trans =re.compile(r'Transfer\s[a-zA-Z0-9_\-\.]+\s[a-zA-Z0-9_\-\.]+\s\w+\s\w+\s\w+')     #tranfer
    minn =re.compile(r'Minted\sNullAddress\s[a-zA-Z0-9_\-\.]+\s\w+\s\w+\s\w+')     #minted
    bidd = re.compile(r'Bid\s[0-9\.\-]+\s[a-zA-Z0-9_\-\.]+\s[a-zA-Z0-9_\-\.]+\s\w+\s\w+')     #biding details

    lissst=re.compile(r'List\s[0-9\.\-]+\s[a-zA-Z0-9_\-\.]+\s\w+\s\w+\s\w+')     #list details
    bidd_time=re.compile(r'\sday|\smonth|\s[0-9]+\s\w+')

    z = sall.findall(Trading_History.f)
    x = trans.findall(Trading_History.f)
    c = minn.findall(Trading_History.f)
    po= bidd.findall(Trading_History.f)
    sk=lissst.findall(Trading_History.f)

    print(sk[0:-1])
    d=[word for line in po for word in line.split()]

    print(len(po))
    print(d)
    print(len(d))

    if len(po)!=0:
        if len(po)==1:
            ko= bidd_time.findall(po[0])
            kl=[0,0]
        if len(po)==2:
            ko= bidd_time.findall(po[0])
            kl= bidd_time.findall(po[1])
        if len(po)==3:
            ko= bidd_time.findall(po[0])
            kl= bidd_time.findall(po[1])

    else:
        ko=[0,0]  
        kl=[0,0]

    print(ko) 

    if len(po)!=0:
        if len(po)==1:
            lk=d[1]
            pk=d[2]
            lk1=0
            pk1=0
        if len(po)==2:
            lk=d[1]
            pk=d[2]
            lk1=d[7]
            pk1=d[8]
        if len(po)==3:
            lk=d[1]
            pk=d[2]
            lk1=d[7]
            pk1=d[8]    
    else:
        lk=0
        pk='none'
        lk1=0
        pk1='none'  

    print(d[3:6])

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
    #print(name)

    print(z)
    print(x)
    print(c) 
    print(po)    
    print("aii")  #------->check
    header_dic={
        "collection_name":header[0],
        "Name_of_NFT":header[4],
        "created_by":heade[1],
        "owned_by":owner[1],
        "views":p[0],
        "favourite":owner[-1],
        "sale_ends_in":sales[2],
        "Duration":sales[3],
        "Minimum_bid_value":sales1[1],
        "Bid_value_in_USD":sales1[2],
        "Token_standard":pia[0],
        "block_chain":kol[0],
        "NFT_image":li[0],
        "gif_video":si[0],
        "Trading_Sale":z[0],
        "Trading_Transfer":x[0],
        "Trading_Minted":c[0],
        "Trading_list":str(sk[0:-1]),
        "Trading_Bid":po[0],
        "Biding_Acc":pk,
        "Biding_value":lk,
        "Biding_time":ko[0],
        "Biding_Acc_2":pk1,
        "Biding_value_2":lk1,
        "Biding_time_2":kl[0]
        #"Token_id":name
    }

    print(header_dic)

    #info.insert_one(header_dic)

    #right before quitting
    driver.quit()
    
    print("success")

except Exception as e:
    print(e)
    #print(repr(e))
    #print(e.args)
    #print(Exception)
    #traceback.print_exc()
    #to send a mail
    #s=requests.get("http://www.thewhizly.co.in/sendinblue/scopex_email.php?email=samdhanaseelan2636@gmail.com&name=mahesh&error={}&vm_id=01".format(repr(e)))
    pass


#time.sleep(1)

#driver.implicitly_wait(3)

#--------> failed by some case
#this is for 2&3
""" sect= driver.find_elements_by_xpath("//div[@class='TradeStation--header']")
    if len(sect)!=0: 
    #print(sales)
        if  len(sect)<2:
            sales=[0,0,0,0] #this line cause the error
        else:  
            for i in sect:
                sales=i.text.splitlines()
                print(sales)
            #print(i.text)
            time.sleep(3)  
    else:
        sales=[0,0,0,0]  """


#1 &2 failed----------->by some case
"""    sectio= driver.find_elements_by_xpath("//div[@class='TradeStation--main']")
    #//div[@class='item--frame']
    #//section[@class='Blockreact__Block-sc-1xf18x6-0 Framereact__Frame-sc-139h1ex-0 fAtwh eoqSMa']
    if len(sectio)!=0:
        if  len(sectio)<2:
            sales1=[0,0,0,0]             # this line cause the error
        else: 
            for i in sectio:
                sales1=i.text.splitlines()
                #print(i.text)
            time.sleep(3) 
            print(sales1)
    else:
        sales1=[0,0,0,0]  """