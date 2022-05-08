
''' import pymongo
from pymongo import cursor

client2 =pymongo.MongoClient('mongodb+srv://aiotylabs:aiotylabs2020!@cluster0.zpris.mongodb.net/test')
my_db=client2['test_db']
info=my_db.asdf
cursor=info.find({})

ds={
    "casc":"scac"
    }

we="scac" #----------->name of nft
re=10  #--------------->update the value
#info.update({"casc":"{}".format(we)},{"$set" : {"sdfd":"{}".format(re)}},upsert= False ,multi=True)  #-------------->makes change in all field
#info.update({"casc":"{}".format(we)},{"$set" : {"sdfd":re}},upsert= False ,multi=True)  #-------------->makes change in all field
for li in cursor:
    print(li) '''


#----------------------------------->update  the particular value in the database.
''' import pymongo

myclient = pymongo.MongoClient("mongodb+srv://aiotylabs:aiotylabs2020!@cluster0.zpris.mongodb.net/test")
mydb = myclient["test_db"]
mycol = mydb["asdf"]

myquery = { "casc": "scac"}
newvalues = { "$set": { "secon": 341 } }

mycol.update_one(myquery, newvalues)

#print "customers" after the update:
for x in mycol.find():
  print(x)
 '''


#----------------------------------->sorting 
import pymongo

myclient = pymongo.MongoClient("mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test")
mydb = myclient["webscrap"]
mycol = mydb["alpha"]

#mydoc = mycol.find().sort("token_id",1)   #----------------->ascending sort
mydoc = mycol.find()   #---------------->descending sort
#mydoc = mycol.find().sort("rarity_rank",-1)   #---------------->descending sort

for x in mydoc.distinct:
  print(x) 
  