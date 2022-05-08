import requests
import json
import time
import pymongo
from datetime import date
from collections import namedtuple
def f():

    #1-------->aiotydb
    client =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')

    #2---------->db2
    #client2 =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')

    my_db=client['nftgdp']
    mycol = my_db["nftslugname"] #-------->#get slug name
    
    
    my_db2=client['nftgdp_coll'] #---------------->2nd process
    #skip=['hashmasks','acclimatedmooncats','g-evols']
    skip=[]
    for x in mycol.distinct("slug_name"):
        if x in skip:
            continue
        mycol12=my_db2['{}'.format(x)]
        new=mycol12.find({})
        cv=0
        vc=0
        xd=0
        static_col_tkn="https://projects.rarity.tools/static/staticdata/"+x+".json"
        collzdtkn = requests.get(static_col_tkn).json()
        this_lt=[int(mn[0]) for mn in collzdtkn["items"]]
        new_lt=[]
        #print(this_lt)
        #print(type(new))
        for  yy in (new):
            y=yy["perma_url"]
            #print(y)
            if (y.find("?") == -1):
                
                cv=cv+1
                #print("bjj")
                #print(y)
            else:
                daf=(y.split("?")[0]).split("/")
                daff=int(daf[len(daf)-1])
                #print(daff)
                new_lt.append(daff)

                
                    
                vc=vc+1
                #print(y)
        
        for gad in this_lt:
            if gad not in new_lt:
                #print(gad)
                xd=xd+1
                #print(type(daff),len(this_lt))
        if(xd!=0 | cv!=0):    
            print(x)

            print(vc,cv)
            print("Pending:",xd)
            print("------------------------")
        
f() #Execute the function
