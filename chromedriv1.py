import time
import json
from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())



driver.get('https://rarible.com/')

driver.maximize_window()
#get title
print("--->title",driver.title)

all_links = driver.find_elements_by_tag_name('div')
print(all_links)


time.sleep(5)

""" #top seller details
condition= True
while condition :
    obj = driver.find_elements_by_xpath(" /html/body/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div ")
    
    for ai in obj:
        #print(obj)
        out = obj[0].text
        li.append(out)
        print(li)
        
    if len(li)<10000:
        break """

""" with open('top_seller.txt','w') as f:
    f.write(json.dumps(out)) """

#live action
lisst=[]
condition= True

while condition :
    obj = driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[3]  ")
    
    for ai in obj:
        #print(obj)
        out = obj[0].text
        lisst.append(out)
        print(lisst)
        
    if len(lisst)<10000:
        break
    try:
        driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[3]/div[2]/div/button[2]") 
    except:
        Condition = False     
with open('live_action.txt','w') as f:
    f.write(json.dumps(lisst))     

#hot bids
#/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[4]

lissst=[]
condition= True
while condition:
    obj = driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[4]  ")
    for ai in obj:
        #print(obj)
        out = obj[0].text
        lissst.append(out)
        print(lisst)

    if len(lissst)<10000:
        break   

    try:
        driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[4]/div[2]/div/button") 
    except:
        Condition = False

with open('hot_bids.txt','w') as f:
    f.write(json.dumps(lissst)) 

#Hot collections
#/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[5]
#/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[5]/div[2]/div/button
#<div class="sc-bdnxRM sc-gtsrHT sc-havuDZ kRuSvk BFpLM"><div class="sc-bdnxRM sc-gtsrHT sc-enrZtP sc-ekA-drt kRuSvk ihJIQH dUxFWE"><div class="sc-bdnxRM sc-gtsrHT sc-dYXZXt kRuSvk jzZUwL"><a href="/token/0x98bc63911792bc90f3bd0ad532258d8a0fe51cb6:11?" class="sc-bdnxRM sc-fKgJPI sc-bCwfaz sc-iwajpm kRuSvk jgjym gtWlEp sc-iiBnNu jFPctD" data-marker="root/appPage/marketplace/hotBids/cards/Winter#/card/link"><img src="https://img.rarible.com/prod/image/upload/t_preview/prod-itemImages/0x98bc63911792bc90f3bd0ad532258d8a0fe51cb6:11" alt="Winter#" title="Winter#" class="sc-bdnxRM sc-dvXYtj sc-TtZnY joHyKy gnBPmJ sc-amiJK bvMJFo" loading="lazy" style="opacity: 1; position: relative;"><div class="sc-bdnxRM sc-gtsrHT sc-jHNicF kRuSvk bMmwdY" style="display: none;"><div class="sc-bdnxRM sc-gtsrHT sc-jSFjdj kRuSvk iWBFmx" style="width: 32px; height: 32px; border-radius: 32px; border-width: 3px;"></div></div></a><div class="sc-bdnxRM sc-gtsrHT sc-eVedaM kRuSvk bzdSnS"><button class="sc-bdnxRM sc-jrsJWt sc-kEqXSa sc-cTJkRt jOsQKY bAVzgZ jLFIvt sc-knSFqH iwmrPd" type="button"><span class="sc-bdnxRM sc-hKFxyN sc-eCApnc bbbkjq"><span class="sc-bdnxRM sc-hKFxyN sc-eCApnc dkjSSg"><span class="sc-bdnxRM sc-hKFxyN sc-eCApnc sc-cQDFzS iAEatC hUkpYz">04</span><span class="sc-bdnxRM sc-hKFxyN sc-eCApnc sc-cQDFzS iAEatC hUkpYz">12</span> <span class="sc-bdnxRM sc-hKFxyN sc-eCApnc sc-hLyimJ iAEatC iZqImD">left</span> <span aria-label="Fire" class="sc-bdnxRM sc-hKFxyN kRuSvk"><span class="emoji emoji-sizer" style="background-image:url(https://cdn.jsdelivr.net/npm/emoji-datasource-apple@6.0.1/img/apple/64/1f525.png)" data-codepoints="1f525"></span></span></span></span></button></div></div></div><div class="sc-bdnxRM sc-gtsrHT sc-enrZtP sc-bwcZwS kRuSvk ihJIQH lgoedk"><a href="/token/0x98bc63911792bc90f3bd0ad532258d8a0fe51cb6:11?" class="sc-bdnxRM sc-fKgJPI sc-bCwfaz sc-iwajpm iWKXLy jgjym gFmBWu">Winter#</a></div><div class="sc-bdnxRM sc-gtsrHT sc-jhDJEt kRuSvk ciiXUl"><span data-marker="root/appPage/marketplace/hotBids/cards/Winter#/card/priceInfo" class="sc-bdnxRM sc-hKFxyN sc-eCApnc eoFEFh"><span class="sc-bdnxRM sc-hKFxyN sc-eCApnc sc-hcmsbg kyHBfZ dzgbrA">Highest bid <span class="sc-bdnxRM sc-hKFxyN sc-eCApnc sc-ojivU iAEatC jjQalL"><span data-supply="1" data-stock="1" class="sc-bdnxRM sc-hKFxyN sc-eCApnc ETmFj">1/1</span></span></span><span class="sc-bdnxRM sc-hKFxyN sc-eCApnc ljCPJp"><span class="sc-bdnxRM sc-hKFxyN sc-eCApnc kAFpxS"><span title="0.0441 wETH" data-currency-symbol="wETH" data-currency-address="0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2" data-price="0.0441" class="sc-bdnxRM sc-hKFxyN sc-eCApnc iAEatC">0.044 wETH</span></span></span></span></div><button class="sc-bdnxRM sc-jrsJWt sc-kEqXSa sc-gggoXN jOsQKY bAVzgZ hCFFZD sc-jCPRHX htTRuv" type="button" data-marker="root/appPage/marketplace/hotBids/cards/Winter#/card/actions/like"><div class="sc-bdnxRM sc-gtsrHT sc-gBsxbr kRuSvk gvnsnr" style="opacity: 0.5;"><svg viewBox="0 0 17 16" fill="none" width="16" height="16" xlmns="http://www.w3.org/2000/svg" class="sc-bdnxRM sc-hKFxyN cdczth"><path d="M8.2112 14L12.1056 9.69231L14.1853 7.39185C15.2497 6.21455 15.3683 4.46116 14.4723 3.15121V3.15121C13.3207 1.46757 10.9637 1.15351 9.41139 2.47685L8.2112 3.5L6.95566 2.42966C5.40738 1.10976 3.06841 1.3603 1.83482 2.97819V2.97819C0.777858 4.36443 0.885104 6.31329 2.08779 7.57518L8.2112 14Z" stroke="currentColor" stroke-width="2"></path></svg></div><div class="sc-bdnxRM sc-gtsrHT sc-hxyAeK kRuSvk bmoOeD" style="opacity: 0.5;"><span data-value="87" class="sc-bdnxRM sc-hKFxyN sc-eCApnc kvViGK">87</span></div></button></div>
lit=[]
condition= True
while condition:
    obj = driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[5]")
    #polist=driver.find_elements_by_class_name('sc-bdnxRM sc-gtsrHT sc-havuDZ kRuSvk BFpLM')
    for ai in obj:
        #print(obj)
        #ppp=ai.find_elements_by_tag_name('a')
        out = obj[0].text
        #lit.append(ppp.get_property('href')).text
        lit.append(out)
        print(lit)

    if len(lit)<10000:
        break   

    try:
        driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[5]/div[2]/div/button") 
    except:
        Condition = False
with open('hot_collections.txt','w') as f:
    f.write(json.dumps(lit))

#Explore
lis=[]
condition= True
while condition:
    obj = driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[7]/div[2]/div/div[2]/div  ")
    for el in obj:
        #print(obj)
        out = obj[0].text
        lis.append(out)
        #print(len(out))
        print(lis)

    if len(lis)<10000:
        break    

    try:
        driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[7]/div[2]/div/div[3]/button") 
    except:
        Condition = False      
with open('explore.txt','w') as f:
    f.write(json.dumps(lis))
