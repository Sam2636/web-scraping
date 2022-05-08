from pymongo.collation import Collation
from pymongo import MongoClient, collection, write_concern
import pymongo
import json
import requests
from datetime import date
import datetime
in_slug_name=input("enter slug name:")
in_page_no=input("pg no")
in_rare_token_price=input("rare or token or price")
in_asc_dsc=input("ASCENDING or DESCENDING")

client = MongoClient('mongodb+srv://prabhat:aiotylabs2020%21@cluster0.qgqw9.mongodb.net/test?authSource=admin&replicaSet=atlas-fm1pq5-shard-0&readPreference=primary&appname=MongoDB+Compass&ssl=true')
database = client['nftgdp']
coll=database['nftgdp_coll_details']

today_date= date.today() 
#print(today_date)
yes_date= Previous_Date = datetime.datetime.today() - datetime.timedelta(days=1)
y_d=yes_date.strftime ('%Y-%m-%d')
#print(y_d)
order_coll=database['date']
cursor_validate =list(coll.find({'date':'{}'.format(today_date)}))
mainlist=[]
total_nfts=0
mainlist2=[]
mainlist3=[]
for xx in range(50):
    mainlist.append("")
    mainlist2.append("")
    mainlist3.append("")


        

    
def api_data():
    cursor =list(coll.find({'date':'{}'.format(f_d)}))
    skp_no=((int(in_page_no)-1)*30)
    db_pg2 = client['nftgdp_coll']
    slug_coll=db_pg2['{}'.format(in_slug_name)]
    if(in_asc_dsc== '-1'):
        cursor2 =list(slug_coll.find({}).skip(skp_no).limit(30).sort('{}'.format(in_rare_token_price),pymongo.DESCENDING).collation(Collation(locale='en_US', numericOrdering=True)))
    else:
        cursor2 =list(slug_coll.find({}).skip(skp_no).limit(30).sort('{}'.format(in_rare_token_price),pymongo.ASCENDING).collation(Collation(locale='en_US', numericOrdering=True)))
        
    #print(cursor2[0])
    total_nfts=slug_coll.count_documents({})
    #print(total_nfts)
    for yx in range(len(cursor2)):
        yam=str(cursor2[yx]['acc_owner'])
        list2=[((cursor2[yx]['rarity_rank'])),
        ((cursor2[yx]['image_url'])),
        (((yam.split("?")[0]).split("/")[4])),
        ((cursor2[yx]['token_id']))]
        mainlist2[yx]=list2
    #print("------------------")
    #print(mainlist2)
    #print("------------------")

    
    
    for x in range(len(cursor[0]['nft_collection'].values())):
        list3=[(list(cursor[0]['nft_collection'].values())[x]['collection']['name']),
        (list(cursor[0]['nft_collection'].values())[x]['collection']['slug']),
        (list(cursor[0]['nft_collection'].values())[x]['collection']['created_date']),
        (list(cursor[0]['nft_collection'].values())[x]['collection']['description']),
        (list(cursor[0]['nft_collection'].values())[x]['collection']['banner_image_url']),
        (list(cursor[0]['nft_collection'].values())[x]['collection']['stats']['total_volume'])]
        if ((list(cursor[0]['nft_collection'].values())[x]['collection']['slug'])==in_slug_name):
            list1=[(list(cursor[0]['nft_collection'].values())[x]['collection']['slug']),
            (list(cursor[0]['nft_collection'].values())[x]['collection']['banner_image_url']),
            (list(cursor[0]['nft_collection'].values())[x]['collection']['image_url']),
            (list(cursor[0]['nft_collection'].values())[x]['collection']['name']),
            (list(cursor[0]['nft_collection'].values())[x]['collection']['description']),
            (list(cursor[0]['nft_collection'].values())[x]['collection']['discord_url']),
            (list(cursor[0]['nft_collection'].values())[x]['collection']['twitter_username']),
            (list(cursor[0]['nft_collection'].values())[x]['collection']['instagram_username']),
            (list(cursor[0]['nft_collection'].values())[x]['collection']['external_url']),
            (list(cursor[0]['nft_collection'].values())[x]['collection']['stats']['seven_day_volume']),
            (list(cursor[0]['nft_collection'].values())[x]['collection']['stats']['total_volume']),
            (list(cursor[0]['nft_collection'].values())[x]['collection']['stats']['seven_day_average_price']),
            (list(cursor[0]['nft_collection'].values())[x]['collection']['stats']['num_owners']),
            ((str(total_nfts)))]
            #print(list1)

            mainlist[0]=list1
            
        mainlist3[x]=list3
        
    ltttt={}
        
    
    #print(type(stlt))
    #stlt[0]='['
    #stlt[len(stlt)]=']'
    
    lttt={}
    mainlist3.sort(key = lambda x: x[5])
    #print(mainlist3[0:9])
    ltt={}
    
    #print(stlt)
    for elem in range(0,len(mainlist3)):
        if(elem<1):
            ele=mainlist[elem]
            one={"slug":ele[0],"name":ele[3],"banner_img":ele[1],"image_url":(ele[2]),"description":(ele[4]),"discord_url":(ele[5]),"twitter_username":(ele[6]),"instagram_username":(ele[7]),"external_url":(ele[8]),"seven_day_volume":(ele[9]),"total_volume":(ele[10]),"seven_day_average_price":(ele[11]),"num_owners":(ele[12]),"total_nfts":(ele[13])}
            ltttt[elem]=(one)
        if(elem<30):
            ele=mainlist2[elem]
            one={"rarity_rank":ele[0],"image_url":ele[1],"acc_owner":ele[2],"token_id":ele[3]}
            lttt[elem]=(one)
        if(elem<9):
            ele=mainlist3[elem]
            one={"slug":ele[1],"name":ele[0],"created_date": ele[2],"desc":ele[3],"banner_img":(ele[4]),"total_volume":ele[5]}
            ltt[elem]=(one)
    
    stlt=str(ltttt)
    stlt="["+stlt[1:(len(stlt)-1)]+"]"
    #print(stlt)
    stltt=str(lttt)
    stltt="["+stltt[1:(len(stltt)-1)]+"]"
    stlttt=str(ltt)
    stlttt="["+stlttt[1:(len(stlttt)-1)]+"]"
    page2={'nft_info':stlt.strip(" ")}#'collection_nft':stltt.strip(""),'similar_collection':stlttt.strip("")}
    print(*[page2])

    
    
    #print(stltt)
    

    #print(mainlist)
    #print("-----------------")
    #print(mainlist2)
    #print("-----------------")
    #print(mainlist3)

if (cursor_validate != []):
    #print(cursor)
    f_d=today_date
    
    api_data()
else:
    yes_date= datetime.datetime.today() - datetime.timedelta(days=1)
    y_d=yes_date.strftime ('%Y-%m-%d')
    #print(y_d)
    f_d=y_d
    
    api_data()
    #print(mainlist)

