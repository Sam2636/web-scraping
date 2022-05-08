import requests
import pymongo


client2 =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')
#my_db=client2['nftgdp_coll']
#infoz=my_db.acclimatedmooncats
my_db=client2['nftgdp_coll']

s=['0n1-force', 'acclimatedmooncats', 'adam-bomb-squad','akc','axie', 'animetas', 'bears-deluxe', 'bored-ape-kennel-club', 'boredapeyachtclub', 'collectvox', 'collectvoxmirandus', 'cool-cats-nft', 'cryptoadz-by-gremplin', 'cryptopunks', 'cyberkongz', 'cyberkongz-vx', 'deadfellaz', 'desperate-ape-wives', 'fluf-world', 'fvck-crystal', 'g-evols', 'galacticapes', 'galaxyeggs9999', 'gamblingapes', 'guttercatgang', 'hashmasks', 'jungle-freaks-by-trosley', 'koala-intelligence-agency', 'lazy-lions', 'lootproject', 'meebits', 'mekaverse', 'mutant-ape-yacht-club', 'mutantcats', 'peaceful-groupies', 'pudgypenguins', 'robotos-official', 'rumble-kong-league', 'sneaky-vampire-syndicate', 'supducks', 'the-doge-pound', 'the-sevens-official', 'thecryptodads', 'thehumanoids', 'theshiboshis', 'thewickedcraniums', 'veefriends', 'vogu', 'winterbears', 'world-of-women-nft']
contract=""
for iu in s[45:46]:
    guii=s.index(iu)

    flag=False
    print(iu)
    infoz=my_db["{}".format(iu)]
    info=infoz.find({})




    def func_getans(lt_gtt):
        xd=""
        for i in lt_gtt:
            fed="token_ids="+str(i)+"&"
            xd=xd+fed
        #print(xd)


        #url = "https://api.opensea.io/api/v1/assets?"+xd+"order_direction=desc&offset=0&limit={}".format(len(lt_gtt)+1)
        url= "https://api.opensea.io/api/v1/assets?"+xd+"&asset_contract_address="+contract+"&offset=0&limit={}".format(len(lt_gtt)+1)

        #r=session.get("https://api.opensea.io/api/v1/assets",params=params)

        #url = "https://api.opensea.io/wyvern/v1/assets?asset_contract_address=0x60e4d786628fea6478f785a6d7e704777c86a7c6&bundled=false&include_bundled=false&"+xd+"limit=5&offset=0&order_by=created_date&order_direction=desc"
        
        response = requests.request("GET", url)
        q=response.json()['assets']
        #print((q))
    
        for x in range(len(q)):
            #print("-----------------------------------")
        #print("slug: "+q[x]['slug'])
            eve=q[x]['token_id']
            print(guii,iu,eve)
            #if(q[x]['owner']['user']['username']==)
            
            odict={}

            if((q[x]['owner']['user'] is not None) and (q[x]['owner']['user']['username'] is not None)):
                #print("owner_name: ",q[x]['owner']['user']['username'])
                odict['owner_name']=q[x]['owner']['user']['username']
            else:
                #print("owner_name:",None)
                odict['owner_name']="None"
            
            #infoz.update({"token_id":"{}".format(eve)},{"$set" : {"owner_name":"{}".format(dp_ownr_name)}},upsert= False ,multi=True)

            #print("owner_address: ",q[x]['owner']['address'])
            odict['owner_address']=q[x]['owner']['address']

            #print("owner_profile_img_url: ",q[x]['owner']['profile_img_url'])
            odict['owner_profile_img_url']=q[x]['owner']['profile_img_url']
            infoz.update({"token_id":"{}".format(eve)},{"$set" : {"owner_details":odict}},upsert= False ,multi=True)

            #print("num_sales: ",q[x]['num_sales'])
        
            p_num_sale=q[x]['num_sales']
            infoz.update({"token_id":"{}".format(eve)},{"$set" : {"num_sales":p_num_sale}},upsert= False ,multi=True)

            listing={}
            if(q[x]['sell_orders'] is not None):
                #print("Listing: ",(q[x]['sell_orders'][0]['created_date']))
                listing['created_date']=q[x]['sell_orders'][0]['created_date']
                last_date={}

                if((q[x]['sell_orders'][0]['closing_date']) is not None): 

                    #print("Last date: ",q[x]['sell_orders'][0]['closing_date'])
                    last_date['closing_date']=q[x]['sell_orders'][0]['closing_date']
                    #print("Last date: ",q[x]['sell_orders'][0]['closing_extendable'])
                    last_date['closing_extendable']=q[x]['sell_orders'][0]['closing_extendable']
                    listing['last_date']=last_date
                else:
                    #print("Last date: ",None)
                    listing['last_date']="None"
                current_price=round(((float(q[x]['sell_orders'][0]['current_price']))/1000000000000000000),4)
                #print("current_price(eth): ",current_price)
                listing['current_price']=str(current_price)
                
                #infoz.update({"token_id":"{}".format(eve)},{"$set" : {"listing":listing}},upsert= False ,multi=True)

                """ print("current_price_symbol: ",q[x]['sell_orders'][0]['payment_token_contract']['symbol'])
                print("current_price_token_name: ",q[x]['sell_orders'][0]['payment_token_contract']['name'])
                print("current_price_decimals: ",q[x]['sell_orders'][0]['payment_token_contract']['decimals'])
                print("current_price_usd_price: ",q[x]['sell_orders'][0]['payment_token_contract']['usd_price'])
                print("total_current_price_in_usd: $", ((current_price)*float(q[x]['sell_orders'][0]['payment_token_contract']['usd_price']))) """

                listing["current_price_symbol"]=q[x]['sell_orders'][0]['payment_token_contract']['symbol']
                listing["current_price_token_name"]=q[x]['sell_orders'][0]['payment_token_contract']['name']
                listing["current_price_decimals"]=q[x]['sell_orders'][0]['payment_token_contract']['decimals']
                listing["current_price_usd_price"]=q[x]['sell_orders'][0]['payment_token_contract']['usd_price']
                listing["total_current_price_in_usd"]= ((current_price)*float(q[x]['sell_orders'][0]['payment_token_contract']['usd_price']))

                infoz.update({"token_id":"{}".format(eve)},{"$set" : {"listing":listing}},upsert= False ,multi=True)

            else:
                #print(">>>Listing: ",None)
                infoz.update({"token_id":"{}".format(eve)},{"$set" : {"listing":"None"}},upsert= False ,multi=True)
                
            
            #infoz.update({"token_id":"{}".format(y)},{"$set" : {"prize_value":"{}".format(daff)}},upsert= False ,multi=True)

            last_sale={}
            if(q[x]['last_sale'] is not None):

                #print("Last_sale_event_timestamp: ",(q[x]['last_sale']['event_timestamp']))
                last_sale["last_sale_event_timestamp"]=(q[x]['last_sale']['event_timestamp'])
                price=(int(q[x]['last_sale']['total_price'])/1000000000000000000)


                """ print("Last_sale_price_eth: ",price)
                print("Payment_token_name: ",(q[x]['last_sale']['payment_token']['name']))
                print("Payment_token_symbol: ",(q[x]['last_sale']['payment_token']['symbol']))
                print("Payment_token_symbol: ",(q[x]['last_sale']['payment_token']['decimals']))
                print("Payment_token_symbol_url: ",(q[x]['last_sale']['payment_token']['image_url']))
                print("One_usd_price_day_of_purchase: ",(q[x]['last_sale']['payment_token']['usd_price']))
                print("total_usd_price_convertion: $",((float(q[x]['last_sale']['payment_token']['usd_price']))*price))"""
                
                last_sale["last_sale_price_eth"]=price
                last_sale["payment_token_name"]=q[x]['last_sale']['payment_token']['name']
                last_sale["payment_token_symbol"]=q[x]['last_sale']['payment_token']['symbol']
                last_sale["payment_token_symbol"]=(q[x]['last_sale']['payment_token']['decimals'])
                last_sale["payment_token_symbol_url"]=(q[x]['last_sale']['payment_token']['image_url'])
                last_sale["one_usd_price_day_of_purchase"]=(q[x]['last_sale']['payment_token']['usd_price'])
                last_sale["total_usd_price_convertion"]=((float(q[x]['last_sale']['payment_token']['usd_price']))*price)
                
                if ((q[x]['last_sale']['transaction']['from_account']['user']) is not None):
                    #print("Last_Sale_user_name: ",(q[x]['last_sale']['transaction']['from_account']['user']['username']))
                    last_sale["last_Sale_user_name"]=(q[x]['last_sale']['transaction']['from_account']['user']['username'])
                    
                else:
                    #print("Last_Sale_user_name: ",None)
                    last_sale["last_Sale_user_name"]="None"
                #print("Last_sale_user_address: ",(q[x]['last_sale']['transaction']['from_account']['address']))
                last_sale["last_sale_user_address"]=(q[x]['last_sale']['transaction']['from_account']['address'])

                infoz.update({"token_id":"{}".format(eve)},{"$set" : {"last_sale":last_sale}},upsert= False ,multi=True)
            
            else:
                #print("last_sale: ",None)
                last_sale["last_sale"]="None"
                
                infoz.update({"token_id":"{}".format(eve)},{"$set" : {"last_sale":"None"}},upsert= False ,multi=True)

                
                
    po=[]
    yu=[]
    count=0
    pp=0
    for num in info:
        #print(num)
        y=num["token_id"]
        #print(y)
        if(flag==False ):
            #print(num)
            #print(num['perma_url'])
            st=num["perma_url"].split("/"+y+"?")[0]
            #print(st)
            ltst=st.split("/")
            contract=(ltst[len(ltst)-1])
            print(contract)
            flag=True
            #print(hhhhhhh)
        if(iu=="axie"):
            contract="0xf5b0a3efb8e8e4c201e2a935f110eaaf3ffecb8d"
        po.append(y)
        #er=po.append(daff)   #----------------->token id
        #lp=yu.append(assert_contr)   #------------>contract address 
        if(count==29):
            print(pp)
            if pp>356:#must -1
                try:
                    func_getans(po)
                except:
                    func_getans(po)
            #print(len(cfa))
            po=[]
            yu=[]
            count=0
            pp=pp+1
            #break
        else:
            count=count+1
    else:
        func_getans(po)
    print(pp)
#print(len(yu))
#cfa=func_getans([6,4,5,10,11,12,13,14,15])
#print(len(cfa))
