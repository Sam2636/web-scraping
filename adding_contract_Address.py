import requests
import pymongo
from requests.models import Response


client2 =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')
#my_db=client2['nftgdp_coll']
#infoz=my_db.acclimatedmooncats
my_db=client2['nftgdp']
infoz=my_db["nftslugname"]
info=infoz.find({})


po=[]
yu=[]
count=0
pp=0


for num in info:
    #if num['owned_by'] == find(str("colection")):
    #print(num['token_id'])
    idd=num['slug_name']
    print(idd)
   
    ''' cd=num['contract_address'].split('/')[4]
    url='https://opensea.io/assets/klaytn/{}/{}'.format(cd,idd)
    print(url) '''

    #infoz.update({"token_id":"{}".format(idd)},{"$set" : {"perma_url":"{}".format(url)}},upsert= False ,multi=True)
    
    #print(vcxzcvcxz)
    


    

