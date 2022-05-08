import pymongo

#1-------->aiotydb
client =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')

#2---------->db2
client2 =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')


my_db=client['webscrap']
mycol = my_db["rank"]


my_db2=client2['NewDB_test']
info=my_db2.collction_stats


for x in mycol.distinct("nft_collection_links"):
    p=s.append(x)