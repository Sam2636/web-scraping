
import json
import re
import csv
import pandas as pd
from matplotlib import pyplot as plt
with open('hot_bids.txt','r') as f:
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
#hot bit
doc ='''Top collections in7 days\n1\nArt Blocks\n$40,736,056.33\n2\nPudgyPenguins\n$34,589,078.36\n3\nOpenSea Shared Storefront\n$31,643,903.67\n4\nparallel\n$18,867,940.40\n5\nBoredApeYachtClub\n$17,954,462.61\n6\nVOX Series 1\n$11,967,026.13\n7\nTheCurrency\n$10,773,885.52\n8\nCyberKongz VX\n$10,469,693.12\n9\nArt Blocks\n$8,594,965.75\n10\nCryptoArte\n$6,709,378.96\n11\nIncognito\n$6,117,470.14\n12\nCool Cats\n$6,076,017.51\n13\nParty Penguins\n$5,394,150.08\n14\nFVCK_CRYSTAL//\n$4,768,294.70\n15\nMeebits\n$4,613,523.55\n16\n0x47e22659d...c545\n$4,497,592.29\n17\nLoneley Aliens Space Club\n$4,120,875.67\n18\nFLUF\n$4,086,874.07'''
doc = doc.replace('\n', ' ')
print(doc)
doct =re.compile(r'\d{1,2}\s[A-Za-z]\w+\s[$]\d{1,2}.\d{3}.\d{2}|\d{1,2}\s[A-Za-z]\w+\s[A-Z]\w+\s[$]\d{1,2}.\d{3}.\d{2}') #[A-Z]\w+.[A-Z]\w+?\s[$]\d{1}?d{2}.\d{3}.\d{2}')
name = doct.findall(doc)
print(lsit_to_string(name))
with open('hot_bit1.txt','w',encoding="utf-8") as f:
  f.write(lsit_to_string(name)) 

#sno
s=[]
sn= re.compile(r'\b([1-9]|1[0-6])\b\s')
#sno = sn.findall('top_seller1.txt')
#print(sno) 

#pattern = re.compile("<(\d{4,5})>")

for i, line in enumerate(open('hot_bit1.txt')):
    for match in re.finditer(sn, line):
        s.append( match.group())
        print( match.group())  


n=[]
nam =re.compile(r'\s[A-Za-z]\w+\s[A-Za-z]\w+\s|\s[A-Za-z]\w+')
#name =nam.findall(doc)
for i, line in enumerate(open('hot_bit1.txt')):
    for match in re.finditer(nam, line):
        n.append( match.group())
        print( match.group())        

#value
val =re.compile(r'\s[$]\d+.\d+.\d+')
#value =val.findall(doc)
li=[]
for i,line in enumerate(open('hot_bit1.txt')):
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
df.to_csv('hot_bit1.csv',encoding='utf-8', index=False)