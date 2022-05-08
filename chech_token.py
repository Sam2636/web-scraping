import pymongo



client2 =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')
my_db=client2['nftgdp_coll']
infoz=my_db["world-of-women-nft"]
info=infoz.find({})


for num in info:
    #print(num)
    y=num["perma_url"]
    print(y)
    daf=(y.split("?")[0]).split("/")
    daff=int(daf[len(daf)-1]) 
    print(daff)
    infoz.update({"perma_url":"{}".format(y)},{"$set" : {"token_id":"{}".format(daff)}},upsert= False ,multi=True)