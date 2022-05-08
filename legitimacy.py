# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 11:59:01 2021

@author: MANIMEGALAI P
"""

import pymongo
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
 
client = pymongo.MongoClient("mongodb://localhost:27017/")
 
# Database Name
db = client["webscrap"]
 
# Collection Name
col = db["scraping"]
 
# Fields with values as 1 will
# only appear in the result
x = col.find({},{'_id': 0,'views':1,'favorite':1})

import csv
csv_columns = ['views','favorite']

csv_file = "dataset.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in x:
            writer.writerow(data)
except IOError:
    print("I/O error")
 

data = pd.read_csv('F:/gif_image_classification1/dataset.csv')

print(data)
   
    
normal = data[data['views']>=data['favorite']]
abnormal = data[data['views']<data['favorite']]

#print(abnormal)

abnormal['legitimacy score']=(abnormal['favorite']-abnormal['views'])/(abnormal['favorite']+abnormal['views'])*100
print(abnormal)

normal['legistimacy score']=(normal['views']-normal['favorite'])/(normal['favorite']+normal['views'])*100
print(normal)
# using merge function by setting how='inner'
df_row = pd.concat([normal,abnormal])
print(df_row)
#df_index = pd.merge(left,right,on=["normal", "abnormal"])

#print(df_index)
#df_index.to_csv("df_index.csv")




plt.figure()
plt.plot(normal,'bx')
plt.plot(abnormal,'ro')
#plt.xlabel("favorite")
#plt.ylabel("views")

plt.show()