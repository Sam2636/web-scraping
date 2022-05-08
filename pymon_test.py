import pymongo

client =pymongo.MongoClient('mongodb://127.0.0.1:27017/')

my_db=client['webscrap']
info=my_db.scraping

records={
    "id":'1',
    "firstname":'sam',
    "secondname":'dhana'
 
}

info.insert_one(records)

#To push csv or json to mongodb

""" import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient

#CSV to JSON Conversion
csvfile = open('C://test//final-current.csv', 'r')
jsonfile = open('C://test//6.json', 'a')
reader = csv.DictReader( csvfile )
header= [ "S.No", "Instrument Name", "Buy Price", "Buy Quantity", "Sell Price", "Sell Quantity", "Last Traded Price", "Total Traded Quantity", "Average Traded Price", "Open Price", "High Price", "Low Price", "Close Price", "V" ,"Time"]
#fieldnames=header
output=[]
for each in reader:
    row={}
    for field in header:
        row[field]=each[field]
    output.append(row)

json.dump(output, jsonfile, indent=None, sort_keys=False , encoding="UTF-8")
mongo_client=MongoClient() 
db=mongo_client.october_mug_talk
db.segment.drop()
data=pd.read_csv('C://test//6.json', error_bad_lines=0)
df = pd.DataFrame(data)
records = csv.DictReader(df)
db.segment.insert(records) """