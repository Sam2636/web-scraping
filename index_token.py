

#------------------------->adding new field to the databaase
import pymongo



client2 =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')
my_db=client2['nftgdp_coll']
infoz=my_db["winterbears"]
info=infoz.find({})
import requests
import pymongo
from requests.models import Response


client2 =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')
my_db=client2['nftgdp_coll']
infoz=my_db.axie
info=infoz.find({})

po=[]
yu=[]
for num in info:
    #print(num)
    y=num["token_id"]
    #print(y)
    
    ''' daf=(y.split("?")[0]).split("/")
    daff=int(daf[len(daf)-1]) 
    assert_contr=daf[len(daf)-2] '''
    po.append(y)   #----------------->token id
    #lp=yu.append(assert_contr)   #------------>contract address
print(len(po))
print(len(yu))

    #infoz.update({"token_id":"{}".format(y)},{"$set" : {"prize_value":"{}".format(daff)}},upsert= False ,multi=True)
    #print("------------------------------------")