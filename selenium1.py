# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 13:21:19 2021

@author: MANIMEGALAI P
"""

from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome(executable_path=r'c:\chromedriver.exe')

driver.get('https://rarible.com/')

driver.maximize_window()
#get title
print("--->title",driver.title)

all_links = driver.find_elements_by_tag_name('div').click()
print(all_links)


time.sleep(5)

obj = driver.find_elements_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/a[1]")
print(obj)
out = obj[0].text
print(out)
#print(all_links[0].find_elements_by_tag_name('a'))
img=all_links[0].find_elements_by_tag_name('img')
print(img[1].text)




