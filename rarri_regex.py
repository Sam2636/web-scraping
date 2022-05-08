# -*- coding: utf-8 -*-
"""
Created on Thru Aug  5 12:05:01 2021

@author: SAM DHANA SEELAN K
"""


""" import re
import requests
# Make the GET request to a url
r = requests.get('https://rarible.com/hoppergang')
# Extract the content
c = r.content
from bs4 import BeautifulSoup
# Create a soup object
soup = BeautifulSoup(c, "html.parser")
#print(soup)
print(soup.title)
warning = soup.find_all('div')
#//*[@id="root"]
print(warning) """


#<div class="sc-bdnxRM sc-gtsrHT sc-iklJeh jvCTkj fxkfYI dSfeOH"></div>
#<div class="sc-bdnxRM sc-clGGWX jvCTkj haBcpE"><div class="sc-bdnxRM sc-oeezt sc-hndLF jvCTkj cObiVj iWOYzY"><img src="https://img.rarible.com/prod/image/upload/t_preview/prod-itemImages/0xc34c39aa3a83afdd35cb65351710cfc56a85c9f5:45" alt="#39 HOPPER - POLYMER SPLIT" title="#39 HOPPER - POLYMER SPLIT" class="sc-gGLxEB sc-ckTSus sc-fbIWvP sc-FRrlG dGJRan gStCxK jREztg cIjgB sc-dvXYtj iduHXF" loading="lazy" style="width: 205px; opacity: 1; visibility: visible; position: relative;"><div class="sc-bdnxRM sc-fXazdy jvCTkj UjHkE" style="display: none;"><div class="sc-bdnxRM sc-hOPeYd jvCTkj eXirsP" style="width: 351px; height: 230px;"><div class="sc-bdnxRM sc-gtsrHT sc-eKYRIR jvCTkj dSYgDb bzGwbY" style="width: 205px; height: 230px;"></div></div></div></div></div>


""" images = container.findAll('img')
example = images[0]
print(example) 
 """
# Find the element on the webpage
#main_content = soup.find('div',{'id': "root"})
""" main_content = soup.find('div',{'id':'root'})
print(main_content) """

#matches = soup.title.text
""" matches = soup.find('div')
print(matches) """
""" content = main_content.find('Img')

regex = re.compile('.*listing-col-.*')
for EachPart in soup.find_all("div", {"class" : regex}):
        print (EachPart.get_text())

print(content) """  
""" for EachPart in soup.select('div[class*="listing-col-"]'):
    print (EachPart.get_text()) """
#<div class="sc-bdnxRM sc-gtsrHT sc-iklJeh jvCTkj fxkfYI dSfeOH"></div>

""" from bs4 import BeautifulSoup
import urllib2
import re

html_page = urllib.urlopen("http://imgur.com")
soup = BeautifulSoup(html_page)
images = []
for img in soup.findAll('img'):
    images.append(img.get('src'))

print(images) """

#//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div/img  #xpath of an image

#/html/body/div/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div/img    #full xpath of the image


import time
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


#topseller 
""" li =[]

nameoftheart = driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/div[1]/div/div/div[1]/div[1]/div/div[3]/a/span").text
#out = nameoftheart[1].text
priceofart=driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/div[1]/div/div/div[1]/div[1]/div/div[3]/span/span/span").text
#inn = priceofart[1].text

temp= {'nameoftheart':out,
        'priceofart':inn}

print(temp)      """   
""" obj = driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div  ")
print(obj)
out = obj[0].text
li.append(out)
print(len(out))
print(li)

with open('top_seller.txt','w',encoding="utf-8) as f:
    f.write(json.dumps(li)) """

""" import csv
def make_csv(data):
    fields = ['Titles', 'Authors', 'Comments']
    filename = "records.csv"
    # writing to csv file
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(data) """

import json        
li=[]      
obj = driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div  ")
print(obj)
out = obj[0].text
li.append(out)
#print(make_csv(out))
print(len(out))
print(li)      

with open('top_seller.txt','w',encoding="utf-8") as f:
    f.write(json.dumps(li))