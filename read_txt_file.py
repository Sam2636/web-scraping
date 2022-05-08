# -*- coding: utf-8 -*-
"""
Created on Thru Aug  5 12:05:01 2021

@author: SAM DHANA SEELAN K
"""

import json
import re
import csv
import pandas as pd
from matplotlib import pyplot as plt
with open('top_seller.txt','r') as f:
    b=f.read()
    
    s=re.compile(r'[$]\d{1}.\d{3}.\d{2}')
    name= re.compile(r'[^.\\n]...[A-Za-z].[A-Za-z]')
    salaries = s.findall(b)
    author = name.findall(b)
    print(salaries)
    print(author)

def make_csv(data):
    fields = ['Comments']
    filename = "records.csv"
    # writing to csv file
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(data)

def lsit_to_string(s):
  str1=' '
  return (str1.join(s))

doc ='''Top\nsellers\nin\n1 day\n1\nSavage Dogs\n$22,073.64\n2\nMazanovsky\n$11,908.93\n3\nValkyr-\u039e\n$11,205.09\n4\nRedlioneye Gazette\n$7,153.78\n5\nhawksnest\n$6,492.97\n6\nverticalcryptoart\n$6,254.45\n7\nLOSC\n$6,141.01\n8\nGeorgijevic\n$4,248.66\n9\nLux Expression\n$4,004.73\n10\nDojo Rawski\n$3,814.53\n11\n\u26a1\ufe0f Crypto Geisha \u26a1\ufe0f\n$3,733.46\n12\nGary Cartlidge\n$3,199.28\n13\nTuomo Korhonen\n$2,272.54\n14\nTake My Muffin\n$1,944.83\n15\nBankless DAO\n$1,875.80'''
doc = doc.replace('\n', ' ')
print(doc)
doct =re.compile(r'\d{1,2}\s[A-Za-z]\w+\s[$]\d{1,2}.\d{3}.\d{2}|\d{1,2}\s[A-Za-z]\w+\s[A-Z]\w+\s[$]\d{1,2}.\d{3}.\d{2}') #[A-Z]\w+.[A-Z]\w+?\s[$]\d{1}?d{2}.\d{3}.\d{2}')
name = doct.findall(doc)
print(lsit_to_string(name))
with open('top_seller1.txt','w',encoding="utf-8") as f:
  f.write(lsit_to_string(name)) 

#sno
s=[]
sn= re.compile(r'\b([1-9]|1[0-6])\b\s')
#sno = sn.findall('top_seller1.txt')
#print(sno) 

#pattern = re.compile("<(\d{4,5})>")

for i, line in enumerate(open('top_seller1.txt')):
    for match in re.finditer(sn, line):
        s.append( match.group())
        print( match.group())

#name
n=[]
nam =re.compile(r'\s[A-Za-z]\w+\s[A-Za-z]\w+\s|\s[A-Za-z]\w+')
#name =nam.findall(doc)
for i, line in enumerate(open('top_seller1.txt')):
    for match in re.finditer(nam, line):
        n.append( match.group())
        print( match.group())


#value
val =re.compile(r'\s[$]\d+.\d+.\d+')
#value =val.findall(doc)
li=[]
for i,line in enumerate(open('top_seller1.txt')):
    for match in re.finditer(val, line):
      
      print( match.group())
      li.append( match.group())
print(li)
      
dic ={
  'sno':s,
  'name':n,
  'value':li

}
print(dic)    
df =pd.DataFrame(dic)
print(df)
df.to_csv('mag1.csv',encoding='utf-8', index=False)

#data visulization of csv file

plt.plot(n,li,marker="o")
plt.xlabel("author")
plt.ylabel("value")
plt.title("top seller in 1 day")
plt.show() 

""" # importing the required library
import seaborn as sns

 
# read a titanic.csv file
# from seaborn library
df = sns.load_dataset('mag1')
 
# class v / s fare barplot
sns.barplot(x = 'n', y = 'li', data = df)
 
# Show the plot
plt.show() """



""" with open("test.csv", "wb") as outfile:
  writer = csv.writer(outfile) """

#d = {"key1": [1,2,3], "key2": [4,5,6], "key3": [7,8,9]}
""" with open("test.csv", "wb") as outfile:
   writer = csv.writer(outfile)
   writer.writerow(dic.keys())
   writer.writerows(zip(*d.values()))   """

""" with open('file.txt', 'rb') as f:
    lines = [x.strip() for x in f.readlines()] """
 
""" with open('.txt','w') as f:
    f.write(json.dumps(li))  """      
""" for line in lines:
    tmp = line.strip()
    split_line = tmp.split('-')
    price = (str(split_line[1]).replace(' ', '')) """   
# field names 
""" fields = ['sno','Name','value'] 
    
# data rows of csv file 
  
with open('GFG', 'w') as f:
      
    # using csv.writer method from CSV package
    write = csv.writer(f)
      
    write.writerow(fields)
    write.writerows(name)  """
""" 
import pandas as pd

read_file = pd.read_csv (r'D:\c_disk_documents\scopeX\web scraping\top_seller.txt')
read_file.to_csv (r'D:\c_disk_documents\scopeX\web scraping\top_seller.csv', index=None)    """
""" 
a_file = open("top_seller.txt", "r")
s=a_file.read() """

""" string_without_line_breaks = " "
for line in a_file:
  stripped_line = line.rstrip()
  string_without_line_breaks += stripped_line
a_file.close()

print(string_without_line_breaks)  """ 
""" s = s.replace('\n',' ')
print(s) """