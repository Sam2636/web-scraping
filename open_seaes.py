
import time
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

#website 
driver.get('https://opensea.io/assets/0x8d04a8c79ceb0889bdd12acdf3fa9d207ed3ff63/46')

driver.maximize_window()
#get title
print("--->title",driver.title)

""" all_links = driver.find_elements_by_tag_name('div')
print(all_links) """


""" time.sleep(5) """

#exploring the data
#/html/body/div[1]/div[1]/main/div/div/div/div[2]/div/div[4]/div
#/html/body/div[1]/div[1]/main/div/div/div/div[2]/div/div[4]
#/html/body/div[1]/div[1]/main/div/div/div/div[2]/div/div[4]/div/div/div/div/div/div/ul/li[1]/div[1]
#row
#/html/body/div[1]/div[1]/main/div/div/div/div[2]/div/div[4]/div/div/div/div/div/div/ul/li[1]
#lisst=[]
""" condition= True

while condition :
    obj = driver.find_elements_by_xpath("/html/body/div[1]/div[1]/main/div/div/div/div[2]/div/div[4]/div/div/div/div/div/div/ul/li[2]/div[1]/div/div/div[2]")
    
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
with open('sea.txt','w') as f:
    f.write(json.dumps(lisst))  """
#table
#1.
#/html/body/div[1]/div[1]/main/div/div/div/div[2]/div/div[4]/div
#2.
#/html/body/div[1]/div[1]/main/div/div/div/div[2]/div/div[4]/div/div/div/div/div/div/ul

#/html/body/div[1]/div[1]/main/div/div/div/div[2]/div/div[4]/div/div/div/div/div/div/ul/li[2]/div[1]/div/div/div[2]/span

#row
#//*[@id="__next"]/div[1]/main/div/div/div/div[2]/div/div[4]/div/div/div/div/div/div/ul/li

#column
#//*[@id="__next"]/div[1]/main/div/div/div/div[2]/div/div[4]/div/div/div/div/div/div/ul/li[1]/div
""" obj = driver.find_elements_by_tag_name("ul")
#driver.SwitchTo().frame(obj)
#for i in range(0,len(obj)):
    #out=obj[-1].text
    #print(out) 
print(len(obj)) 
for i in obj:
    out=obj[0].text
    print(out)
    #print(len(obj))
 """
#/html/body/div[1]/div[1]/main/div/div/div/div[2]/div/div[4]/div/div/div/div/div/div/ul/li[2]
""" obj = driver.find_elements_by_xpath("//*[@id='__next']/div[1]/main/div/div/div/div[2]/div/div[4]/div/div")
rows = driver.find_elements_by_name('div')
cells = driver.find_elements_by_xpath('/html/body/div[1]/div[1]/main/div/div/div/div[2]/div/div[4]/div/div/div/div/div/div/ul/li[1]/div[1]')
print(rows)
print(cells)
for rows in obj:
    print(len(rows))
for cells in obj:
    print(len(cells)) """
#driver.SwitchTo().frame(obj)
#for i in range(0,len(obj)):
    #out=obj[-1].text
    #print(out) 
#rows=WebDriverWait(obj,10).until(presence_of_element_located((By.XPATH,'//*[@id="__next"]/div[1]/main/div/div/div/div[2]/div/div[4]/div/div/div/div/div/div/ul/li')) )  
""" print(obj) 
for i in obj:
    out=obj[0].text """
#print([i.text for i in rows]) 
    #print(len(obj))