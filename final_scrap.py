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
import pyperclip as pc

# starting time
start = time.time()

# for driver we can download and specifiy the path or we can use the below code  
driver = webdriver.Chrome(ChromeDriverManager().install())

client =pymongo.MongoClient('mongodb+srv://aiotylabs:aiotylabs2020!@cluster0.zpris.mongodb.net/test')

my_db=client['webscrap']
info=my_db.scrap_2



driver.get("https://opensea.io/assets?search[categories][0]=art")
#driver.get("https://opensea.io/assets?search[categories][0]=art&search[query]=blitmap")
driver.maximize_window()
driver.implicitly_wait(2)
#time.sleep(2)  # Allow 2 seconds for the web page to open
scroll_pause_time = 1# You can set your own pause time. My laptop is a bit slow so I use 1 sec
screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
i = 1

urls = []

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

    sectio= driver.find_elements_by_xpath("//a[@class='styles__StyledLink-sc-l6elh8-0 ekTmzq Asset--anchor']")
    if len(sectio)!=0:
        for kl in sectio:  
            ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
            driver.implicitly_wait(10000)  
            saly=kl.get_attribute("href")
            """ your_element = WebDriverWait(driver, driver.implicitly_wait(100000),ignored_exceptions=ignored_exceptions)\
                        .until(driver.presence_of_element_located((By.href, saly))) """
            urls.append(saly)
        #print(len(sales1))

        print(len(urls)) 
    #print(len(urls))    
print('this is',len(urls))    
#print(urls[0:25])

#time.sleep(5)
driver.implicitly_wait(5)

print ("The original list is : " +  str(urls))
print(len(urls))
# using naive method
# to remove duplicated 
# from list 
res = []
for i in urls:
    if i not in res:
        res.append(i)
  
# printing list after removal 
print ("The list after removing duplicates : " + str(res))
print(len(urls))
print(len(res))
print("the difference between them are:{}".format(len(urls)-len(res)))
print("the percentage between them:{}%".format(len(res)/(len(urls))*100))

""" driver.quit()


#fine test case

s=driver.get('https://opensea.io/collection/art')
#s=driver.get('https://opensea.io/assets?search[query]=blitmap')
driver.maximize_window() """
""" tok=[] 
       
#tok=[]
#styles__StyledLink-sc-l6elh8-0 cnTbOd Asset--anchor   # 14/9/2021
#Tk = driver.find_elements_by_xpath("//a[@class='Linkreact__StyledA-sc-18se2b0-0 iWVmEt Asset--anchor']")
Tk = driver.find_elements_by_xpath("//a[@class='styles__StyledLink-sc-l6elh8-0 cnTbOd Asset--anchor']")
for i in Tk: #Linkreact__StyledA-sc-18se2b0-0 iWVmEt Asset--anchor
    da=i.get_attribute("href")
    tok.append(da)
    print(da) """

for lo in res:
    s=driver.get(str(lo))
    #time.sleep(2)
    driver.implicitly_wait(1)
        
    driver.maximize_window()
    
    Llink_of_Nft = lo

    print(lo)

    val =re.compile(r'0x[a-zA-Z0-9]+')
    name = val.findall(lo)
    print(name)
    
    #token_id
    sa =re.compile(r'/[0-9]+')   #[0-9]+
    y= sa.findall(lo)
    lk=y[1]

    pa =re.compile(r'[0-9]+')   #[0-9]+
    mi= pa.findall(lk)
    print(mi)

    #token_standard
    elem = driver.find_element_by_xpath("//*")
    source_code = elem.get_attribute("outerHTML")

    #print(source_code)
    sas =re.compile(r'ERC[0-9]+')   #[0-9]+
    pia= sas.findall(source_code)
    print(pia[0])
    print(len(pia))

    #details of blockchain
    ash =re.compile(r'polygon|Ethereum')   #[0-9]+
    kol = ash.findall(source_code)
    print(kol)
    print(kol[0])

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
    

        
    #links discord ,twitter_link
    obj = driver.find_elements_by_xpath("//a[@class='styles__StyledLink-sc-l6elh8-0 ekTmzq Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 bhqEJb efDGWe ButtonGroupreact__StyledButton-sc-1skvztv-0 dBcbvG']")

    lli=[]
    for w in obj:
        link_src=w.get_attribute("href")
        lli.append(link_src)

    if len(lli)==0:
        lli.append(0) 
    else:
        pass
         
        

    print(lli)

    print("links",lli[0])
    


    #image    
    obj = driver.find_elements_by_xpath("//img[@class='Image--image']")
    li=[]
    for w in obj:
        img_src=w.get_attribute("src")
        li.append(img_src)

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
        """ apply=driver.find_element_by_xpath("//div[@class='Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 FlexColumnreact__FlexColumn-sc-1wwz3hp-0 VerticalAlignedreact__VerticalAligned-sc-b4hiel-0 dBFmez jYqxGr ksFzlZ iXcsEj']")
        apply.click()
        # <div class="Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 FlexColumnreact__FlexColumn-sc-1wwz3hp-0 VerticalAlignedreact__VerticalAligned-sc-b4hiel-0 dBFmez jYqxGr ksFzlZ iXcsEj" bis_skin_checked="1"><button type="button" class="UnstyledButtonreact__UnstyledButton-sc-ty1bh0-0 btgkrL"><li class="EventHistory--filter-dropdown-clear">Clear All</li></button></div>
        #driver.implicitly_wait(10) """
        apply=driver.find_element_by_xpath("//div[@class='Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 FlexColumnreact__FlexColumn-sc-1wwz3hp-0 VerticalAlignedreact__VerticalAligned-sc-b4hiel-0 dBFmez jYqxGr ksFzlZ iXcsEj']")
        action =ActionChains(driver)
        action.click(on_element = apply)
        print("cleared_all")
        #print("cleared_all")

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
    sall =re.compile(r'Sale\s\d+.\d+\s[a-zA-Z0-9_\-\.]+\s[a-zA-Z0-9_\-\.]+\s\w+\s\w+\s\w+')     #sale
    trans =re.compile(r'Transfer\s[a-zA-Z0-9_\-\.]+\s[a-zA-Z0-9_\-\.]+\s\w+\s\w+\s\w+')     #tranfer
    minn =re.compile(r'Minted\sNullAddress\s[a-zA-Z0-9_\-\.]+\s\w+\s\w+\s\w+')     #minted
    bidd = re.compile(r'Bid\s[0-9\.\-]+\s[a-zA-Z0-9_\-\.]+\s[a-zA-Z0-9_\-\.]+\s\w+\s\w+')     #biding details
    lissst=re.compile(r'List\s[0-9\.\-]+\s[a-zA-Z0-9_\-\.]+\s\w+\s\w+\s\w+')     #list details  ----> 10/11/2021
    bidd_time=re.compile(r'\sday|\smonth|\s[0-9]+\s\w+')

    z = sall.findall(Trading_History.f)
    x = trans.findall(Trading_History.f)
    c = minn.findall(Trading_History.f)
    po= bidd.findall(Trading_History.f)
    sk=lissst.findall(Trading_History.f)

    print(z[0:-1])
    print(x[0:-1])
    print(c[0:-1])
    print(po[0:-1])
    print(sk[0:-1])
    #print(po)
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


    #print(len(z))    #whether we have to use the try expect method or not.
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
    if len(sk)==0:
        po=['no-value']
    else:  
        pass 

    for yu in range(len(z)):
        print(str(z[yu]))

       
    
    #wallet_details
    
    llii=[]
    #styles__StyledLink-sc-l6elh8-0 hubhNL AccountLink--ellipsis-overflow  --------------->new update on 13/10/2021
    #apply=driver.find_element_by_xpath("//a[@class='styles__StyledLink-sc-l6elh8-0 ekTmzq AccountLink--ellipsis-overflow']")
    apply=driver.find_element_by_xpath("//a[@class='styles__StyledLink-sc-l6elh8-0 hubhNL AccountLink--ellipsis-overflow']")
    img_src=apply.get_attribute("href")
    llii.append(img_src)

    for llo in llii:
        s=driver.get(str(llo))
        #time.sleep(2)
        driver.implicitly_wait(1)
            
        driver.maximize_window()

        applyy=driver.find_element_by_xpath("//button[@class='UnstyledButtonreact__UnstyledButton-sc-ty1bh0-0 TextCopierreact__StyledContainer-sc-ga2cnk-0 btgkrL AccountHeader--address']")
        applyy.click()
        
        wallet_address=pc.paste()
        print(pc.paste())
        print(s) 

        driver.implicitly_wait(10)

        driver.back()

    header_dic={
        "NFt_link":lo,
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
        "contract_address":name[0],
        "wallet_address":wallet_address,
        "Token_id":mi[0],
        "Token_standard":pia[1],
        "Blockchain":kol[0],
        "links":str(lli[0:-1]),
        #"website":li[1],
        #"discord":li[2],
        #"twitter":li[3], 
        "Trading_Sale":str(z[0:-1]),
        "Trading_Transfer":str(x[0:-1]),
        "Trading_Minted":c[0],
        "Trading_Bid":str(po[0:-1]),
        "Trading_list":str(sk[0:-1])
        #"Trading_Bid":po[1],
        #"1st Bid":pk,
        #"2nd Bid":pk1,
        #"1st Bid value_eth":lk,
        #"2nd Bid value_eth":lk1,
        #"1st Bid_time":ko[0],
        #"2nd Bid_time_2":kl[0]
    }

    print(header_dic)

    #info.insert_one(header_dic)

    info.onlyInsertIfValueIsUniqueDemo.insert_one(header_dic)

#right before quitting
#time.sleep(1)
print(len(urls))
print(len(res))
print("the difference between them are:{}".format(len(urls)-len(res)))
print("the percentage between them:{}%".format(len(res)/(len(urls))*100))
driver.implicitly_wait(1)
driver.quit()

# end time
end = time.time()

tim= end - start
# total time taken
#print(f"Runtime of the program is {(end - start)/60} minutes")
def run_time(seconds):
    seconds_in_day = 86400
    seconds_in_hour = 3600
    seconds_in_minute = 60


    days = seconds // seconds_in_day
    seconds = seconds - (days * seconds_in_day)

    hours = seconds // seconds_in_hour
    seconds = seconds - (hours * seconds_in_hour)

    minutes = seconds // seconds_in_minute
    seconds = seconds - (minutes * seconds_in_minute)

    print("{0:.0f} days, {1:.0f} hours, {2:.0f} minutes, {3:.0f} seconds.".format(days, hours, minutes, seconds))

run_time (float(tim))            #(input("Enter a number of seconds: "))