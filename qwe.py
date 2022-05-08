import requests
import pymongo
from requests.models import Response


client2 =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')
#my_db=client2['nftgdp_coll']
#infoz=my_db.acclimatedmooncats
my_db=client2['webscrap']
infoz=my_db.cryptopunks
info=infoz.find({})


    
po=[]
yu=[]
count=0
pp=0
for num in info:
    #print(num)
    y=num["toke_id"]
    #print(y)
    
    daf=(y.split("?")[0]).split("/")
    #print(daf)
    daff=int(daf[len(daf)-1]) 
    print(daff)
    assert_contr=daf[len(daf)-2]
    """ po.append(daff)   #----------------->token id
    yu.append(assert_contr)   #------------>contract address """
    #infoz.update({"perma_url":"{}".format(y)},{"$set" : {"token_id":"{}".format(daff)}},upsert= False ,multi=True)
#print(len(yu))
#cfa=func_getans([6,4,5,10,11,12,13,14,15])
#print(len(cfa))



