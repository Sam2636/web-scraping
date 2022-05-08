from selenium import webdriver
from selenium.webdriver.common.keys import Keys                       
import time

import requests
from bs4 import BeautifulSoup


for page in range(1,10):
    url ="https://api.opensea.io/graphql/"
    response =requests.post(url=url).content
    soup = BeautifulSoup(response,'lxml')
    pl=soup.find('article',{'class':'Assetreact__DivContainer-sc-bnjqwy-0 gwTKfX Asset--loaded AssetSearchList--asset'})
    print(response)
    print(url)

    """ for ji in pl:
        print(ji.find('a',{'class':"styles__StyledLink-sc-l6elh8-0 cnTbOd Asset--anchor"}))
"""  """
def get_selenium():                           
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('headless')                        
    driver = webdriver.Chrome(chrome_options=options)
    return (driver)

selenium = get_selenium()                         
selenium.get("your/url")    
last_elem = '';
while True:
    current_last_elem = "#my-div > ul > li:last-child"
    scroll = "document.querySelector(\'" + current_last_elem + "\').scrollIntoView();"
    selenium.execute_script(scroll) # execute the js scroll
    time.sleep(3) # wait for page to load new content
    if (last_elem == current_elem):
       break
    else:
       last_elem = current_elem         """