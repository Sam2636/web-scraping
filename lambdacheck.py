from pymongo.collation import Collation
from pymongo import MongoClient, collection, write_concern
import pymongo
import json
import requests
from datetime import date
import datetime
def lambda_handler(event=None, context=None):
    client = MongoClient('mongodb+srv://prabhat:aiotylabs2020%21@cluster0.qgqw9.mongodb.net/test?authSource=admin&replicaSet=atlas-fm1pq5-shard-0&readPreference=primary&appname=MongoDB+Compass&ssl=true')
    database = client['nftgdp']
    coll=database['nftgdp_coll_details']

    today_date= date.today() 
    print(today_date)
    yes_date= Previous_Date = datetime.datetime.today() - datetime.timedelta(days=1)
    y_d=yes_date.strftime ('%Y-%m-%d')
    print(y_d)
    order_coll=database['date']
    cursor_validate =list(coll.find({'date':'{}'.format(today_date)}))


    def api_data():
        cursor =list(coll.find({'date':'{}'.format(y_d)}))
        mainlist=[]
        mainlist2=[]
        mainlist3=[]

        for xx in range(50):
            mainlist.append("")
            mainlist2.append("")
            mainlist3.append("")
        
        for x in range(len(cursor[0]['nft_collection'].values())):
            list1=[(list(cursor[0]['nft_collection'].values())[x]['collection']['name']),
            (list(cursor[0]['nft_collection'].values())[x]['collection']['slug']),
            (list(cursor[0]['nft_collection'].values())[x]['collection']['stats']['one_day_change']),
            (list(cursor[0]['nft_collection'].values())[x]['collection']['banner_image_url'])]
            
            list2=[(list(cursor[0]['nft_collection'].values())[x]['collection']['name']),
                (list(cursor[0]['nft_collection'].values())[x]['collection']['slug']),
                (list(cursor[0]['nft_collection'].values())[x]['collection']['image_url']),
                (list(cursor[0]['nft_collection'].values())[x]['collection']['stats']['total_volume']),
                (list(cursor[0]['nft_collection'].values())[x]['collection']['stats']['total_sales']),
                (list(cursor[0]['nft_collection'].values())[x]['collection']['stats']['num_owners']),
                (list(cursor[0]['nft_collection'].values())[x]['collection']['stats']['floor_price']),
                (list(cursor[0]['nft_collection'].values())[x]['collection']['stats']['one_day_change']),
                (list(cursor[0]['nft_collection'].values())[x]['collection']['stats']['seven_day_change']),
                (list(cursor[0]['nft_collection'].values())[x]['collection']['stats']['thirty_day_change']),
                (list(cursor[0]['nft_collection'].values())[x]['collection']['stats']['market_cap'])]
            
            list3=[(list(cursor[0]['nft_collection'].values())[x]['collection']['name']),
            (list(cursor[0]['nft_collection'].values())[x]['collection']['slug']),
            (list(cursor[0]['nft_collection'].values())[x]['collection']['created_date']),
            (list(cursor[0]['nft_collection'].values())[x]['collection']['description']),
            (list(cursor[0]['nft_collection'].values())[x]['collection']['banner_image_url']),
            (list(cursor[0]['nft_collection'].values())[x]['collection']['stats']['total_volume'])]
            mainlist[x]=list1
            mainlist2[x]=list2
            mainlist3[x]=list3
        #print(mainlist)
        #print("-----------------")
        #print(mainlist2)
        #print("-----------------")
        #print(mainlist3)

        mainlist.sort(key = lambda x: x[2],reverse=True)
        #print(mainlist[0:7])
        ltttt={}
            
        
        #print(type(stlt))
        #stlt[0]='['
        #stlt[len(stlt)]=']'
        
        #print(stlt)
        mainlist2.sort(key = lambda x: x[3],reverse=True)
        #print(mainlist2[0])
        
        lttt={}
        
        
        #print(stltt)
        
        mainlist3.sort(key = lambda x: x[5])
        print(mainlist3[0:9])
        ltt={}
        for elem in range(0,len(mainlist2)):
            if(elem<7):
                ele=mainlist[elem]
                one={"slug":ele[1],"name":ele[0],"banner_img":ele[3],"one_day_change":"+"+str(ele[2])}
                ltttt[elem]=(one)
            if(elem<9):
                ele=mainlist3[elem]
                one={"slug":ele[1],"name":ele[0],"created_date": ele[2],"desc":ele[3],"banner_img":(ele[4]),"total_volume":ele[5]}
                ltt[elem]=(one)
            ele=mainlist2[elem]
            one={"slug":ele[1],"name":ele[0],"icon":ele[2],"total_volume":(ele[3]),"total_sales":(ele[4]),"num_owners":(ele[5]),"floor_price":(ele[6]),"one_day_change":(ele[7]),"seven_day_change":(ele[8]),"thirty_day_change":(ele[9]),"market_cap":(ele[10])}
            lttt[elem]=(one)    
        stlt=str(ltttt)
        stlt="["+stlt[1:(len(stlt)-1)]+"]"
        stltt=str(lttt)
        stltt="["+stltt[1:(len(stltt)-1)]+"]"
        stlttt=str(ltt)
        stlttt="["+stlttt[1:(len(stlttt)-1)]+"]"
        page1="{'slider':"+stlt+",'ranking':"+stltt+",'collect':"+stlttt+"}"
        print(page1)
        #return(page1)
    if(cursor_validate != []):
        #print(cursor)
        f_d=today_date
        print(json.dumps(api_data()))
        #return(json.dumps(api_data()))
        
    else:
        yes_date= datetime.datetime.today() - datetime.timedelta(days=1)
        y_d=yes_date.strftime ('%Y-%m-%d')
        #print(y_d)
        f_d=y_d
        print(json.dumps(api_data()))
        #return(json.dumps(api_data()))