from pymongo.collation import Collation
from pymongo import MongoClient, collection, write_concern
import pymongo
import json
import requests
from datetime import date
import datetime

client = MongoClient('mongodb+srv://prabhat:aiotylabs2020%21@cluster0.qgqw9.mongodb.net/test?authSource=admin&replicaSet=atlas-fm1pq5-shard-0&readPreference=primary&appname=MongoDB+Compass&ssl=true')
database = client['nftgdp']
coll=database['nftgdp_coll_details']

today_date= '2022-01-11'#date.today() 
print(today_date)
yes_date= Previous_Date = datetime.datetime.today() - datetime.timedelta(days=1)
y_d=yes_date.strftime ('%Y-%m-%d')
print(y_d)
order_coll=database['date']
cursor_validate =list(coll.find({'date':'{}'.format(today_date)}))


def api_data():
    list11=[]
    cursor =list(coll.find({'date':'{}'.format(y_d)}))
    for x in range(len(cursor[0]['nft_collection'].values())):
        q={}
        q.add(list(cursor[0]['nft_collection'].values())[x]['collection']['name'])
        q.add(list(cursor[0]['nft_collection'].values())[x]['collection']['slug'])
        q.add(list(cursor[0]['nft_collection'].values())[x]['collection']['stats']['one_day_change'])
        q.add(list(cursor[0]['nft_collection'].values())[x]['collection']['image_url'])
        list11.append(q)
    print(list11)
    
    

if (cursor_validate != []):
    print(cursor)
    f_d=today_date
    api_data()
else:
    yes_date= datetime.datetime.today() - datetime.timedelta(days=1)
    y_d=yes_date.strftime ('%Y-%m-%d')
    print(y_d)
    f_d=y_d
    api_data()
        
