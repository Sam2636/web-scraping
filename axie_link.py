#s="https://opensea.io/assets/0xf5b0a3efb8e8e4c201e2a935f110eaaf3ffecb8d/{}"".format(daf)


import pymongo



client2 =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')
my_db=client2['nftgdp_coll']
infoz=my_db.axie
info=infoz.find({})
mycol = my_db["axie"]

li=[]
for num in info:
    #print(num)
    y=num["nft_name"]
    print(y)
    #print(y)
    daf=y.split("#")[1]
    
    #daff=int(daf[len(daf)-1])
    li.append(daf)
    s="https://opensea.io/assets/0xf5b0a3efb8e8e4c201e2a935f110eaaf3ffecb8d/{}".format(daf)

    print(s)
    myquery = { "nft_name":"{}".format(y)}
    newvalues = { "$set": { "perma_url": s } }

    mycol.update_one(myquery, newvalues)
    

    #infoz.update({"perma_url":"{}".format(y)},{"$set" : {"token_id":"{}".format(daff)}},upsert= False ,multi=True)
    #print("------------------------------------")

print(len(li))