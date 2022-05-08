# -*- coding: utf-8 -*-
"""
Created on Thru Aug  18 12:05:01 2021

@author: SAM DHANA SEELAN K
"""
import json
import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

#getting the web page  
driver.get('https://rarible.com/')

driver.maximize_window()
#get title
print("--->title",driver.title)
#all_links = driver.find_elements_by_class_name('sc-gXZlLH gpYwNk is-selected')
all_links = driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div/div/div[1]")
a= driver.find_elements_by_tag_name("a")
#print(all_links)
for a in all_links:
   print(a.text)
time.sleep(5)

#<div class="sc-gXZlLH gpYwNk is-selected"><div data-media-type="IMAGE" data-collection-id="0x60f80121c31a0d46b5279700f9df786054aa5ee5" data-token-id="1189164" class="sc-bdnxRM sc-gtsrHT sc-dlnjwi sc-hGwcmR fIPEUP cijSUD DdpMc sc-cfARRi kJkgol" data-marker="root/appPage/marketplace/hotBids/cards/Woof Bulldog #003/card"><div class="sc-EhTUr iLoerT"></div><div class="sc-bdnxRM sc-gtsrHT sc-dlnjwi sc-iuImSO fIPEUP cijSUD tvwgW"><div class="sc-bdnxRM sc-gtsrHT sc-bKoJNE kRuSvk hTFgFD"><div class="sc-bdnxRM sc-gtsrHT sc-eKaNGd kRuSvk cMApHi"><a href="/collection/0x60f80121c31a0d46b5279700f9df786054aa5ee5?tab=onsale" class="sc-bdnxRM sc-fKgJPI sc-bCwfaz sc-iwajpm kRuSvk jgjym gtWlEp sc-fGgQJw evxdpL"><img src="https://img.rarible.com/prod/image/upload/t_avatar_preview/prod-collections/0x60f80121c31a0d46b5279700f9df786054aa5ee5/avatar/QmfNA7QWXzSp5G7qwkR9DxR225AGbtxjtfGDKrX2s9TV2N" loading="lazy" class="sc-bdnxRM sc-dvXYtj sc-hmvkKb kRuSvk cGSLcz"></a><a href="/xalvador_nft?tab=onsale" class="sc-bdnxRM sc-fKgJPI sc-bCwfaz sc-iwajpm kRuSvk jgjym gtWlEp sc-fGgQJw evxdpL"><img src="https://img.rarible.com/prod/image/upload/t_avatar_preview/prod-users/0x6f71a9aa1bf1cc885b5b9d73852dd0ea79d27b6e/avatar/QmYkCkiADyY9yr2mYaZu669ZUedA48S1FmrKE41ZgB7aTo" loading="lazy" class="sc-bdnxRM sc-dvXYtj sc-hmvkKb kRuSvk cGSLcz"><div class="sc-bdnxRM sc-gtsrHT sc-jQAxuV kRuSvk hsWAsh"><svg width="14" height="14" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M4.78117 0.743103C5.29164 -0.247701 6.70826 -0.247701 7.21872 0.743103C7.52545 1.33846 8.21742 1.62509 8.8553 1.42099C9.91685 1.08134 10.9186 2.08304 10.5789 3.1446C10.3748 3.78247 10.6614 4.47445 11.2568 4.78117C12.2476 5.29164 12.2476 6.70826 11.2568 7.21872C10.6614 7.52545 10.3748 8.21742 10.5789 8.8553C10.9186 9.91685 9.91685 10.9186 8.8553 10.5789C8.21742 10.3748 7.52545 10.6614 7.21872 11.2568C6.70826 12.2476 5.29164 12.2476 4.78117 11.2568C4.47445 10.6614 3.78247 10.3748 3.1446 10.5789C2.08304 10.9186 1.08134 9.91685 1.42099 8.8553C1.62509 8.21742 1.33846 7.52545 0.743103 7.21872C-0.247701 6.70826 -0.247701 5.29164 0.743103 4.78117C1.33846 4.47445 1.62509 3.78247 1.42099 3.1446C1.08134 2.08304 2.08304 1.08134 3.1446 1.42099C3.78247 1.62509 4.47445 1.33846 4.78117 0.743103Z" fill="#feda03"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M8.43961 4.23998C8.64623 4.43922 8.65221 4.76823 8.45297 4.97484L5.40604 8.13462L3.54703 6.20676C3.34779 6.00014 3.35377 5.67113 3.56039 5.47189C3.76701 5.27266 4.09602 5.27864 4.29526 5.48525L5.40604 6.63718L7.70475 4.25334C7.90398 4.04672 8.23299 4.04074 8.43961 4.23998Z" fill="#000000"></path></svg></div></a><a href="/xalvador_nft?tab=onsale" class="sc-bdnxRM sc-fKgJPI sc-bCwfaz sc-iwajpm kRuSvk jgjym gtWlEp sc-fGgQJw evxdpL"><img src="https://img.rarible.com/prod/image/upload/t_avatar_preview/prod-users/0x6f71a9aa1bf1cc885b5b9d73852dd0ea79d27b6e/avatar/QmYkCkiADyY9yr2mYaZu669ZUedA48S1FmrKE41ZgB7aTo" loading="lazy" class="sc-bdnxRM sc-dvXYtj sc-hmvkKb kRuSvk cGSLcz"><div class="sc-bdnxRM sc-gtsrHT sc-jQAxuV kRuSvk hsWAsh"><svg width="14" height="14" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M4.78117 0.743103C5.29164 -0.247701 6.70826 -0.247701 7.21872 0.743103C7.52545 1.33846 8.21742 1.62509 8.8553 1.42099C9.91685 1.08134 10.9186 2.08304 10.5789 3.1446C10.3748 3.78247 10.6614 4.47445 11.2568 4.78117C12.2476 5.29164 12.2476 6.70826 11.2568 7.21872C10.6614 7.52545 10.3748 8.21742 10.5789 8.8553C10.9186 9.91685 9.91685 10.9186 8.8553 10.5789C8.21742 10.3748 7.52545 10.6614 7.21872 11.2568C6.70826 12.2476 5.29164 12.2476 4.78117 11.2568C4.47445 10.6614 3.78247 10.3748 3.1446 10.5789C2.08304 10.9186 1.08134 9.91685 1.42099 8.8553C1.62509 8.21742 1.33846 7.52545 0.743103 7.21872C-0.247701 6.70826 -0.247701 5.29164 0.743103 4.78117C1.33846 4.47445 1.62509 3.78247 1.42099 3.1446C1.08134 2.08304 2.08304 1.08134 3.1446 1.42099C3.78247 1.62509 4.47445 1.33846 4.78117 0.743103Z" fill="#feda03"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M8.43961 4.23998C8.64623 4.43922 8.65221 4.76823 8.45297 4.97484L5.40604 8.13462L3.54703 6.20676C3.34779 6.00014 3.35377 5.67113 3.56039 5.47189C3.76701 5.27266 4.09602 5.27864 4.29526 5.48525L5.40604 6.63718L7.70475 4.25334C7.90398 4.04672 8.23299 4.04074 8.43961 4.23998Z" fill="#000000"></path></svg></div></a></div><div class="sc-bdnxRM sc-gtsrHT kRuSvk"><div class="sc-bdnxRM sc-gtsrHT sc-eJocfa kRuSvk jARayQ" aria-expanded="false"><button class="sc-bdnxRM sc-jrsJWt sc-kEqXSa sc-giAqHp jOsQKY bAVzgZ fWHFlw sc-gJjCVn gGQnXL" type="button" data-marker="root/appPage/marketplace/hotBids/cards/Woof Bulldog #003/card/actions/trigger"><svg viewBox="0 0 14 4" fill="none" width="16" height="16" xlmns="http://www.w3.org/2000/svg" class="sc-bdnxRM sc-hKFxyN hOiKLt"><path fill-rule="evenodd" clip-rule="evenodd" d="M3.5 2C3.5 2.82843 2.82843 3.5 2 3.5C1.17157 3.5 0.5 2.82843 0.5 2C0.5 1.17157 1.17157 0.5 2 0.5C2.82843 0.5 3.5 1.17157 3.5 2ZM8.5 2C8.5 2.82843 7.82843 3.5 7 3.5C6.17157 3.5 5.5 2.82843 5.5 2C5.5 1.17157 6.17157 0.5 7 0.5C7.82843 0.5 8.5 1.17157 8.5 2ZM11.999 3.5C12.8274 3.5 13.499 2.82843 13.499 2C13.499 1.17157 12.8274 0.5 11.999 0.5C11.1706 0.5 10.499 1.17157 10.499 2C10.499 2.82843 11.1706 3.5 11.999 3.5Z" fill="currentColor"></path></svg></button></div></div></div><div class="sc-bdnxRM sc-gtsrHT sc-dlnjwi hqAiOT cijSUD"><div class="sc-bdnxRM sc-gtsrHT sc-havuDZ kRuSvk BFpLM"><div class="sc-bdnxRM sc-gtsrHT sc-enrZtP sc-ekA-drt kRuSvk ihJIQH dUxFWE"><div class="sc-bdnxRM sc-gtsrHT sc-dYXZXt kRuSvk jzZUwL"><a href="/token/0x60f80121c31a0d46b5279700f9df786054aa5ee5:1189164?" class="sc-bdnxRM sc-fKgJPI sc-bCwfaz sc-iwajpm kRuSvk jgjym gtWlEp sc-iiBnNu jFPctD" data-marker="root/appPage/marketplace/hotBids/cards/Woof Bulldog #003/card/link"><img src="https://img.rarible.com/prod/image/upload/t_preview/prod-itemImages/0x60f80121c31a0d46b5279700f9df786054aa5ee5:1189164" alt="Woof Bulldog #003" title="Woof Bulldog #003" class="sc-bdnxRM sc-dvXYtj sc-TtZnY joHyKy gnBPmJ sc-amiJK bvMJFo" loading="lazy" style="opacity: 1; position: relative;"></a><div class="sc-bdnxRM sc-gtsrHT sc-eVedaM kRuSvk bzdSnS"><button class="sc-bdnxRM sc-jrsJWt sc-kEqXSa sc-cTJkRt jOsQKY bAVzgZ jLFIvt sc-knSFqH iwmrPd" type="button"><span class="sc-bdnxRM sc-hKFxyN sc-eCApnc bbbkjq"><span class="sc-bdnxRM sc-hKFxyN sc-eCApnc dkjSSg"><span class="sc-bdnxRM sc-hKFxyN sc-eCApnc sc-cQDFzS iAEatC hUkpYz">03</span><span class="sc-bdnxRM sc-hKFxyN sc-eCApnc sc-cQDFzS iAEatC hUkpYz">14</span> <span class="sc-bdnxRM sc-hKFxyN sc-eCApnc sc-hLyimJ iAEatC iZqImD">left</span> <span aria-label="Fire" class="sc-bdnxRM sc-hKFxyN kRuSvk"><span class="emoji emoji-sizer" style="background-image:url(https://cdn.jsdelivr.net/npm/emoji-datasource-apple@6.0.1/img/apple/64/1f525.png)" data-codepoints="1f525"></span></span></span></span></button></div></div></div><div class="sc-bdnxRM sc-gtsrHT sc-enrZtP sc-bwcZwS kRuSvk ihJIQH lgoedk"><a href="/token/0x60f80121c31a0d46b5279700f9df786054aa5ee5:1189164?" class="sc-bdnxRM sc-fKgJPI sc-bCwfaz sc-iwajpm iWKXLy jgjym gFmBWu">Woof Bulldog #003</a></div><div class="sc-bdnxRM sc-gtsrHT sc-jhDJEt kRuSvk ciiXUl"><span data-marker="root/appPage/marketplace/hotBids/cards/Woof Bulldog #003/card/priceInfo" class="sc-bdnxRM sc-hKFxyN sc-eCApnc eoFEFh"><span class="sc-bdnxRM sc-hKFxyN sc-eCApnc sc-hcmsbg kyHBfZ dzgbrA">Highest bid <span class="sc-bdnxRM sc-hKFxyN sc-eCApnc sc-ojivU iAEatC jjQalL"><span data-supply="1" data-stock="1" class="sc-bdnxRM sc-hKFxyN sc-eCApnc ETmFj">1/1</span></span></span><span class="sc-bdnxRM sc-hKFxyN sc-eCApnc ljCPJp"><span class="sc-bdnxRM sc-hKFxyN sc-eCApnc kAFpxS"><span title="0.016 wETH" data-currency-symbol="wETH" data-currency-address="0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2" data-price="0.016" class="sc-bdnxRM sc-hKFxyN sc-eCApnc iAEatC">0.016 wETH</span></span></span></span></div><button class="sc-bdnxRM sc-jrsJWt sc-kEqXSa sc-gggoXN jOsQKY bAVzgZ hCFFZD sc-jCPRHX htTRuv" type="button" data-marker="root/appPage/marketplace/hotBids/cards/Woof Bulldog #003/card/actions/like"><div class="sc-bdnxRM sc-gtsrHT sc-gBsxbr kRuSvk gvnsnr" style="opacity: 0.5;"><svg viewBox="0 0 17 16" fill="none" width="16" height="16" xlmns="http://www.w3.org/2000/svg" class="sc-bdnxRM sc-hKFxyN cdczth"><path d="M8.2112 14L12.1056 9.69231L14.1853 7.39185C15.2497 6.21455 15.3683 4.46116 14.4723 3.15121V3.15121C13.3207 1.46757 10.9637 1.15351 9.41139 2.47685L8.2112 3.5L6.95566 2.42966C5.40738 1.10976 3.06841 1.3603 1.83482 2.97819V2.97819C0.777858 4.36443 0.885104 6.31329 2.08779 7.57518L8.2112 14Z" stroke="currentColor" stroke-width="2"></path></svg></div><div class="sc-bdnxRM sc-gtsrHT sc-hxyAeK kRuSvk bmoOeD" style="opacity: 0.5;"><span data-value="21" class="sc-bdnxRM sc-hKFxyN sc-eCApnc kvViGK">21</span></div></button></div></div></div></div></div>

#si=[]
#condition= True
""" a= driver.find_elements_by_tag_name("a")
out=a.text """
#while condition :
    #obj = driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[3]  ")
#    all_links = driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[3]")
#    a= driver.find_elements_by_tag_name("img")
#    p=a.get_attribute('src')
#    #for image in images:
    #print(image.get_attribute('src'))

"""    for p in all_links:
        #print(obj)
        out = a.text
        si.append(out)
        #print(lisst) 
        print(out)
        
    if len(si)<10000:
        break  
    try:
        driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[3]/div[2]/div/button") 
    except:
        Condition = False     
with open('1.txt','w') as f:
    f.write(json.dumps(si))  """ 


li=[]
all_links = driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/div/a/img")
""" a= driver.find_elements_by_tag_name("img")
p=a.get_attribute[0]('src') 
li.append(p)
print(li)    """

#txt = "//body//div//span[@class='Jv7Aj mArmR MqpiF  ']//a[@class='FPmhX notranslate MBL3Z']"
#elems = browser.find_elements_by_xpath(txt)
elm_list = []

for item in all_links:
    elm_list.append(item.get_attribute('src'))

print(item)   