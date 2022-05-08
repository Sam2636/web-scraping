
import json
import re
import csv
import pandas as pd
from matplotlib import pyplot as plt


#name
n=[]

#price
Price = re.compile(r'Pri[A-Za-z]e\s')
for i, line in enumerate(open('opensea.txt')):
    for match in re.finditer(Price, line):
        n.append( match.group())
        print( match.group())

#USD PRICE
USD_Price =re.compile(r'U[A-Z]\w+\sP[A-Za-z]\w+')
for i, line in enumerate(open('opensea.txt')):
    for match in re.finditer(USD_Price, line):
        n.append( match.group())
        print( match.group())

#expiration
EXPriration = re.compile(r'Expi[A-Za-z]\w+')
for i, line in enumerate(open('opensea.txt')):
    for match in re.finditer(EXPriration, line):
        n.append( match.group())
        print( match.group())
#from
From = re.compile(r'F[A-Za-z]om')
for i, line in enumerate(open('opensea.txt')):
    for match in re.finditer(From, line):
        n.append( match.group())
        print( match.group())
#name =nam.findall(doc)
#value=
v=[]
value = re.compile(r'6\.21')
From = re.compile(r'F[A-Za-z]om')
for i, line in enumerate(open('opense1.txt')):
    for match in re.finditer(value, line):
        v.append( match.group())
        print( match.group())
#eth
eth=[]
eths = re.compile(r'[$]\d+.\d+.\d+')
for i, line in enumerate(open('opense1.txt')):
    for match in re.finditer(eths, line):
        eth.append( match.group())
        print( match.group())

#expriation
tim = re.compile(r'in\s[0-9]\sh\w+|in\s[0-9]\sm\w+')
t=[]

for i, line in enumerate(open('opense1.txt')):
    for match in re.finditer(tim, line):
        t.append( match.group())
        print( match.group())

#frm val
val_ac= re.compile(r'\d{3}[A-Z]\d{1}[A-Z]')
Ac=[]

for i, line in enumerate(open('opense1.txt')):
    for match in re.finditer(val_ac, line):
        Ac.append( match.group())
        print( match.group())

""" for i, line in enumerate(open('opensea.txt')):
    for match in re.finditer(nam, line):
        n.append( match.group())
        print( match.group()) """
 
print(n)
print(v)
print(eth)
print(t)
print(Ac)


dic ={
  'Price':v[0],
  'USD_price':eth[0],
  'Expiration':t[0],
  'From':Ac[0]

}
e={
  'Price':v[1],
  'USD_price':eth[1],
  'Expiration':t[1],
  'From':Ac[1]


}

print(e)
print(dic)    
with open('seea.csv','w')as f:
    w=csv.DictWriter(f,dic.keys())
    w.writeheader()
    w.writerow(dic)
    w.writerow(e)
"""df =pd.DataFrame(dic)
print(df)
df.to_csv('sea.csv',encoding='utf-8', index=False) """











""" 

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
 """
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