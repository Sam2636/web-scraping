
from operator import le
import pymongo
from requests.models import Response



client2 =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')
#my_db=client2['nftgdp_coll']
#infoz=my_db.acclimatedmooncats
my_db=client2['nftgdp_solana_details']
my_db2=client2['nftgdp_solana']

infoz=my_db2["solana_slug"]
info=my_db.list_collection_names()
#print(len(info))
newinfo=[]
for xx in info:
    sd={"slug_name":xx,"blockchain":"sol"}
    newinfo.append(sd)



infoz.insert_many(newinfo)
