# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 07:04:05 2022

@author: User
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 12:32:18 2022

@author: User
"""

import requests
import json
import time
import pymongo
from datetime import date
from collections import namedtuple

def fun():

    #1-------->aiotydb
    client =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')

    #2---------->db2
    #client2 =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')
    my_db=client['v2_test_mani']
    mycol = client['nftgdp']["nftslugname"]
    #mycol2 = my_db.collection_stats_by_raritytools
    mycol3= my_db["try_name"]
    
   
    maindict={}
    
    type1={}
   
   
    for x in mycol.distinct("slug_name"):
        
        fetch_date=str(date.today())
        
        url = "https://api.opensea.io/api/v1/collection/{}".format(x)

        response = (requests.request("GET", url)).json()
        a=response["collection"]['primary_asset_contracts']
        type1[x]=a[0]['schema_name']
        
           
            
        
        #print(a[0]['schema_name'],"mmmmm")
    #print(type1)
    
    #[k for k,v in type1.items() if v == 'ERC1155']
    for key, values in list(type1.items()):
        if values == 'ERC1155':
            del type1[key]
            
        #print(type1,"kkkkkkkkkk")
            for i in type1:
                print(i[0])


                dicc={
                    "slug_name":i,
                    "blockchain":'ETH'
                         
                }
       
                mycol3.insert_one(dicc)    
    maindict["date"]=fetch_date
    maindict["type"]=type1
    #print(maindict)
    mycol3.insert_one(maindict)
    
                
fun() 
  
