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

from webdriver_manager.chrome import ChromeDriverManager
""" options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors') """
#driver = webdriver.Chrome(chrome_options=options)


driver = webdriver.Chrome(ChromeDriverManager().install())

client =pymongo.MongoClient('mongodb://127.0.0.1:27017/')

my_db=client['webscrap']
info=my_db.scraping

#website 
#driver.get('https://opensea.io/collection/art')
#driver.get('https://opensea.io/assets/0x8d04a8c79ceb0889bdd12acdf3fa9d207ed3ff63/46')
#driver.get('https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/39356350101089816672191633134995271031197112828404960464413394357946738016257')

#trading history check
#case1
#driver.get('https://opensea.io/assets/0x8d04a8c79ceb0889bdd12acdf3fa9d207ed3ff63/1634')

#case2
#
# driver.get('https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/27120191763199976919292215411415012994301152658287878041911990196944347594753')

#case3
#s=driver.get('https://opensea.io/assets/0x8d04a8c79ceb0889bdd12acdf3fa9d207ed3ff63/15')

#https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/39356350101089816672191633134995271031197112828404960464413394357946738016257
#case$
#s=driver.get('https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/3237216513819739365483939717988508378265798769752999342574546422336174686209')
#case5
#s=driver.get('https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/3237216513819739365483939717988508378265798769752999342574546444326407241729')


#case6
#s=driver.get('https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/3237216513819739365483939717988508378265798769752999342574546469615174680577')

#case7

#s=driver.get('https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/3237216513819739365483939717988508378265798769752999342574546438828849102849')
#s=driver.get('https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/12188539606278965682196433845558533184038346738852018567444545279219541737473')
#s=driver.get('https://opensea.io/assets/matic/0x2953399124f0cbb46d2cbacd8a89cf0599974963/112236847829549195725252796510137205911281236528816072847126752522814462361601/')
#s=driver.get('https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/78654339273234277085305339794035921746225215355450310017130332878810424279041')
#s=driver.get('https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/40482595849772694285173713041642282097106100196042549765489081234743686594561')
s=driver.get('https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/2485050474617492253657970371697643944580510880023237115193260124440455282689')
#offer_table bot
#s=driver.get('https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/108937609937296399194171997007219888570303265273129286037198106280101045862401')



#https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/3237216513819739365483939717988508378265798769752999342574546422336174686209


driver.maximize_window()
#get title
time.sleep(3)

""" 
rows=1+len(driver.find_elements_by_xpath("//div[@class='ChainInfo--label']"))

cols=len(driver.find_elements_by_xpath("//div[@class='ChainInfo--label-value']"))
 """
#section= driver.find_elements_by_xpath("/html/body/div[1]/div[1]/main/div/div/div/div[2]/div/section[3]/div/div[3]/div/div/div/div/div/div[2]/div[2]/button")
#section= driver.find_elements_by_xpath("//div[@class='Panel--content-container']")   #------->so any values
#section= driver.find_elements_by_xpath("//div[@class='ChainInforeact__DivContainer-sc-7gbmjn-0 hQkkXF']")
#section= driver.find_elements_by_xpath("//button[@class='UnstyledButtonreact__UnstyledButton-sc-ty1bh0-0 TextCopierreact__StyledContainer-sc-ga2cnk-0 btgkrL']")

#print(len(section))
#sectio= driver.find_elements_by_xpath("//div[@class='Panel--isContentPadded item--details']")
#sectio= driver.find_elements_by_xpath("//div[@class='BasePanel--body Panel--body']")
sectio= driver.find_elements_by_xpath("//header[@class='BasePanel--header Panel--header']") #----->fails


#details
#//div[@class='Panel--isContentPadded item--details'
ji=[]
#details=driver.find_elements_by_xpath("//div[@class='Scrollboxreact__DivContainer-sc-1b04elr-0 ddtCpj EventHistory--container']")
#details=driver.find_elements_by_xpath("//div[@class='Panelreact__DivContainer-sc-1uztusg-0 kqWgoM Panel--isOpen Panel--isFramed']")
#details=driver.find_elements_by_xpath("//div[@class='BasePanelreact__DivContainer-sc-1d6z6bk-0 isGqga Panel--panel']")
#details=driver.find_elements_by_xpath("//div[@class='ChainInforeact__DivContainer-sc-7gbmjn-0 hQkkXF']")
#details=driver.find_elements_by_xpath("//div[@class='ChainInfo--label']")  #---------------->empty parameters 

""" 

#wallet address

#//div[@class='AccountHeader--subtitle']

details=driver.find_elements_by_xpath("//div[@class='AccountHeader--subtitle']")  
for j in details:
    a=j.text
    #print(j.text)
print(a) 




#token_standard
elem = driver.find_element_by_xpath("//*")
source_code = elem.get_attribute("outerHTML")

#print(source_code)
sas =re.compile(r'ERC[0-9]+')   #[0-9]+
p = sas.findall(source_code)

#details of blockchain
ash =re.compile(r'polygon|Ethereum')   #[0-9]+
kol = ash.findall(source_code)
print(kol)
print(kol[0])

print(p)
print(p[0])
 """




s='List 0.2 NighThoughts 16 minutes ago'

sa =re.compile(r'List\s[0-9\.\-]+\s[a-zA-Z0-9_\-\.]+\s\w+\s\w+\s\w+')   #[0-9]+
y= sa.findall(s)

print(y)



""" #token_id
sa =re.compile(r'/[0-9]+')   #[0-9]+
y= sa.findall(s)
lk=y[1]

sa =re.compile(r'[0-9]+')   #[0-9]+
m= sa.findall(lk)
print(m) """


""" 
details=driver.find_elements_by_xpath("//div[@class='ChainInfo--label-value']")  
for j in details:
    ji.append(j.text)
    #print(j.text)
print(ji) 

#styles__StyledLink-sc-l6elh8-0 ekTmzq Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 bhqEJb efDGWe ButtonGroupreact__StyledButton-sc-1skvztv-0 dBcbvG"

#links discord ,twitter_link
obj = driver.find_elements_by_xpath("//a[@class='styles__StyledLink-sc-l6elh8-0 ekTmzq Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 bhqEJb efDGWe ButtonGroupreact__StyledButton-sc-1skvztv-0 dBcbvG']")

li=[]
for w in obj:
    link_src=w.get_attribute("href")
    li.append(link_src)

if len(li)==4:
    pass
else:
    li.append(0) 
    li.append(0) 
    li.append(0) 
    li.append(0) 
    

print(li)

print("Activity:",li[0])
print("website:",li[1])
print("discord:",li[2])
print("twitter:",li[3])

 """



""" 

for i in sectio:
    p=i.text
    header=i.text.splitlines()
#time.sleep(1) 
driver.implicitly_wait(1)
print(p)
print(header) """

#driver.quit()














#re for finding the token in weblink
""" txt='https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/3237216513819739365483939717988508378265798769752999342574546421236663058433'
val =re.compile(r'0x[a-zA-Z0-9]+')
name = val.findall(txt)
print(name)
 """
""" sal= driver.find_elements_by_xpath("//div[@class='TradeStation--main']")
#//div[@class='TradeStationreact__DivContainer-sc-o1vm2f-0 iYQJMx']
#//div[@class='item--frame']
#//section[@class='Blockreact__Block-sc-1xf18x6-0 Framereact__Frame-sc-139h1ex-0 fAtwh eoqSMa']
#sales=i.text.splitlines()
#TradeStationreact__DivContainer-sc-o1vm2f-0 iYQJMx
#//div[@class='TradeStationreact__DivContainer-sc-o1vm2f-0 iYQJMx']
for i in sal:
    print(i.text)
    sales=i.text.splitlines()
    #print(i.text)
time.sleep(3)
#print(i.text)
#2----no of sales
#3------duration
#6----value
#7----usd value
print(sales) """


""" from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.get("http://psychoticelites.com/") """

#assert "Artz" in driver.title

""" continue_link = driver.find_element_by_tag_name('a')
#elem = driver.find_elements_by_xpath("//*[@href]")
#x = str(continue_link)
#print(continue_link)
#print(elem)
elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
    print(elem.get_attribute("href")) """


"""
tok=[]
Tk = driver.find_elements_by_class_name('Blockreact__Block-sc-1xf18x6-0 dMJNfS')
#Blockreact__Block-sc-1xf18x6-0 dMJNfS
for j in Tk:
    da=j.get_attribute("href")
    print(da)
 """

#driver.execute_script("window.scrollBy(0,200)","")
""" time.sleep(1)
    s=Tk.get_property('href')
    print(j.text) """
""" for k in Tk:
        s=Tk[0].get_property('href')
        print(s) """

    #article class="Assetreact__DivContainer-sc-bnjqwy-0 gwTKfX Asset--loaded AssetSearchList--asset
    #//div[@class='Blockreact__Block-sc-1xf18x6-0 mFlni']
    #Blockreact__Block-sc-1xf18x6-0 fAtwh AssetsSearchView--assets
"""  for i in Tk: #Linkreact__StyledA-sc-18se2b0-0 iWVmEt Asset--anchor
        da=i.get_attribute("href")
        time.sleep(1)
        tok.append(da)
        print(da)
        try:
            driver.execute_script("window.scrollBy(0,100)","")
            time.sleep(1)
        except:
            pass """
        
tok=[]

    #driver.execute_script("window.scrollBy(0,200)","")

    #Blockreact__Block-sc-1xf18x6-0 fAtwh AssetsSearchView--assets
    #styles__StyledLink-sc-l6elh8-0 cnTbOd Asset--anchor
""" tok=[]
Tk = driver.find_elements_by_xpath("//a[@class='Linkreact__StyledA-sc-18se2b0-0 iWVmEt Asset--anchor']")
for i in Tk: #Linkreact__StyledA-sc-18se2b0-0 iWVmEt Asset--anchor
    da=i.get_attribute("href")
    tok.append(da)
    print(da)

for i in tok:
    s=driver.get(str(i))
    time.sleep(2)
    
    val =re.compile(r'0x[a-zA-Z0-9]+')
    name = val.findall(i)
    print(name)
 """


#offer table working********* in a table.
#//ul[@role='table']
s=[]
elems = driver.find_elements_by_xpath("//ul[@role='table']")
g=['No_offer_yet','No_offer_yet']
for ele in elems:
    #print(ele.text.replace('\n'," "))
    op=(ele.text.replace('\n'," "))
    #print(len(op))
    s.append(ele.text.replace('\n'," "))
    print("this is the offer table",s)
    time.sleep(1)
    print("length of s:",len(s))
    if len(s)<2:
        pass
    if len(op)!=0:
        qad=re.compile(r'\d+.\d+\sWETH\s[$]\d+.\d+.\d+\sin\s\d+\s\w+\s[a-zA-Z0-9_\-\.]+|\d+.\d+\sWETH\s[$]\d+.\d+.\d+\sin\s\d+\s\w+\s\w+\s[a-zA-Z0-9_\-\.]+|\d+\sWETH\s[$]\d+.\d+.\d+\s\d+.\d+%\s\w+\sin\s\d+\s\w+\s[a-zA-Z0-9_\-\.]+')  
        g=qad.findall(op)
         #if g[1]==0:
            #g[1]='0' #have to test a conditon if one g value is missing 
        #print(len(elems))
        #print(g) 
    else:
        g=['No_offer_yet','No_offer_yet']              
        


#/html/body/div[1]/div[1]/main/div/div/div/div[2]/div/div[3]/div/header/i[2]

""" apply=driver.find_element_by_xpath("/html/body/div[1]/div[1]/main/div/div/div/div[2]/div/div[5]/div/div/div/div/div/div/div[1]/ul/div/button").click()


time.sleep(2)
apply.click() """

#listing        <li role="row" class="Tablereact__TableRow-sc-120fhmz-1 fwzXIM"><div class="Tablereact__TableCellContainer-sc-120fhmz-2 jKElJJ" role="columnheader" bis_skin_checked="1"><div class="Overflowreact__OverflowContainer-sc-10mm0lu-0 gjwKJf" bis_skin_checked="1">Price</div></div><div class="Tablereact__TableCellContainer-sc-120fhmz-2 jKElJJ" role="columnheader" bis_skin_checked="1"><div class="Overflowreact__OverflowContainer-sc-10mm0lu-0 gjwKJf" bis_skin_checked="1">USD Price</div></div><div class="Tablereact__TableCellContainer-sc-120fhmz-2 jKElJJ" role="columnheader" bis_skin_checked="1"><div class="Overflowreact__OverflowContainer-sc-10mm0lu-0 gjwKJf" bis_skin_checked="1">Expiration</div></div><div class="Tablereact__TableCellContainer-sc-120fhmz-2 jKElJJ" role="columnheader" bis_skin_checked="1"><div class="Overflowreact__OverflowContainer-sc-10mm0lu-0 gjwKJf" bis_skin_checked="1">From</div></div><div class="Tablereact__TableCellContainer-sc-120fhmz-2 jKElJJ" role="columnheader" bis_skin_checked="1"><div class="Overflowreact__OverflowContainer-sc-10mm0lu-0 gjwKJf" bis_skin_checked="1"></div></div></li>
""" rp=[]
#elems = driver.find_elements_by_xpath("//div[@class='BasePanel--body Panel--body']")
elems = driver.find_elements_by_xpath("//ul[@role='table']")
g=['No_offer_yet','No_offer_yet']
for ele in elems:
    print(ele.text.replace('\n'," "))
    op=(ele.text.replace('\n'," "))
    print(len(op))
    rp.append(ele.text.replace('\n',""))
    time.sleep(1)

print(rp)
 """

driver.quit()
""" val =re.compile(r'[$]\d+.\d+.\d+')     #value
fromm =re.compile(r'[0-9a-zA-Z]{6}')     #from
timee =re.compile(r'\d+\shours|\d+\sminutes')     #time
price_w =re.compile(r'\d+.\d+\sWETH')     #price """


""" l = val.findall(o)
k = fromm.findall(o)
j = timee.findall(o)
h = price_w.findall(o) """
""" print(l)  
print(j)  
print(k)  
print(h) """  
################offer table
""" dictt={
    "offer_table_val1":g[0],
    "offer_table_val2":g[1]
}

print(dictt)
 """



#//div[@class='Scrollbox--content']

    #p.append(elem.text)

#print(s)    
#print(f)  
#

#########case_1
#Trading history
""" sall =re.compile(r'Sale\s\d+\s[0-9a-zA-Z]{6}\s[0-9a-zA-Z]{6}\s\w+\s\w+\s\w+')     #sale
trans =re.compile(r'Transfer\s[0-9a-zA-Z]{6}\s[0-9a-zA-Z]{6}\s\w+\s\w+\s\w+')     #tranfer
minn =re.compile(r'Minted\sNullAddress\s[0-9a-zA-Z]{6}\s\w+\s\w+\s\w+')     #minted
z = sall.findall(f)
x = trans.findall(f)
c = minn.findall(f) """
#print(name) """

""" #clear=driver.find_element_by_xpath("//li[@class='EventHistory--filter-dropdown-clear']")
clear=driver.find_element_by_link_text('Clear All')
clear.click() """

""" 
elems = driver.find_elements_by_xpath("//div[@class='Scrollbox--content']")
for elem in elems:
    print(elem.text.replace('\n'," ")) 
    f=elem.text.replace('\n'," ")
    time.sleep(1)  

#######case_2       #[a-zA-Z0-9_\-\.]+    #this is the perfect regex for capturing the id
#Trading history
sall =re.compile(r'Sale\s\d+.\d+\s[a-zA-Z0-9_\-\.]+\s[a-zA-Z0-9_\-\.]+\s\w+\s\w+\s\w+')     #sale
trans =re.compile(r'Transfer\s[a-zA-Z0-9_\-\.]+\s[a-zA-Z0-9_\-\.]+\s\w+\s\w+\s\w+')     #tranfer
minn =re.compile(r'Minted\sNullAddress\s[a-zA-Z0-9_\-\.]+\s\w+\s\w+\s\w+')     #minted
bidd = re.compile(r'Bid\s[0-9\.\-]+\s[a-zA-Z0-9_\-\.]+\s[a-zA-Z0-9_\-\.]+\s\w+\s\w+')     #biding details
bidd_time=re.compile(r'\s[0-9]+\s\w+|\w+\smonth')

z = sall.findall(f)
x = trans.findall(f)
c = minn.findall(f)
po= bidd.findall(f)

d=[word for line in po for word in line.split()]

print(len(po))
print(d)
print(len(d))
if len(po)!=0:
    if len(po)==1:
        ko= bidd_time.findall(po[0])
    if len(po)==2:
        ko= bidd_time.findall(po[0])
        kl= bidd_time.findall(po[1])

else:
    ko=[0,0]
    kl=[0,0]    

print(ko) 

if len(po)!=0:
    lk=d[1]
    pk=d[2]
    if len(po)==2:
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


dictt={
    "Trading_Sale":z[0],
    "Trading_Transfer":x[0],
    "Trading_Minted":c[0],
    "Trading_Bid_1":po[0],
    "Trading_Bid_2":po[1],
    "Biding_Acc_1":pk,
    "Biding_value_1":lk,
    "Biding_time_1":ko[0],
    "Biding_Acc_2":pk1,
    "Biding_value_2":lk1,
    "Biding_time_2":kl[0]
}
print(dictt)  """  

#current_price   

#test failed ------------------17/9/2021
""" #current_pric= driver.find_elements_by_xpath("//div[@class='TradeStation--main']")
#current_pric= driver.find_elements_by_xpath("//div[@class='Overflowreact__OverflowContainer-sc-10mm0lu-0 fqMVjm Price--amount']")
current_pric= driver.find_elements_by_xpath("//div[@class='Overflowreact__OverflowContainer-sc-10mm0lu-0 fqMVjm Price--fiat-amount Price--fiat-amount-secondary']")
if len(current_pric)!=0:
    if  len(current_pric)<2:
        sales1=[0,0,0,0]     #this is executed initally so it the script tends to fails
    else: 
        for i in current_pric:
            curt_pr=i.text.splitlines()
            #print(i.text)
        time.sleep(3) 
        print(curt_pr)
else:
    sales1=[0,0,0,0]    """
""" 
section= driver.find_elements_by_xpath("//section[@class='item--counts']")
for i in section:
    owner=i.text.splitlines()
    fav =re.compile(r'\d+\sfavorite')     #favorite bug fix
    z = fav.findall(owner[-1])
    if len(z)==0:
        owner.append('0 favorite')
    else:
        pass 
time.sleep(1) 

print(owner) """
""" ds=['256 views']
sall =re.compile(r'[0-9\.\-]+k|[0-9]+')   #[0-9]+
z = sall.findall(ds[0])
print(z) """

""" ds=['256 favorites']
sall =re.compile(r'[0-9\.\-]+k|[0-9]+')   #[0-9]+
z = sall.findall(ds[0])
print(z) """


""" #//script[@id='__NEXT_DATA__']

obj = driver.find_elements_by_xpath("//script[@id='__NEXT_DATA__']")
li=[]
for w in obj:
    img_src=w.get_attribute("src")
    li.append(img_src)

print(li) """


#//li[@class='EventHistory--filter-dropdown-clear']