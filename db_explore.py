import pymongo
import pandas as pd


client =pymongo.MongoClient('mongodb://127.0.0.1:27017/')

my_db=client['webscrap']
info=my_db.scraping

p=info.find({},{'_id': 0,"views":1,"favorite":1})

for doc in p:
    print(doc)

import csv
csv_columns = ['views','favorite']

csv_file = "dataset.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in p:
            writer.writerow(data)
except IOError:
    print("I/O error")
 

data = pd.read_csv('D:\c_disk_documents\scopeX\web scraping\dataset.csv')

print(data)
   