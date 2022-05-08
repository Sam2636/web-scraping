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
    y=num["perma_url"]
    #print(y)
    
    daf=(y.split("?")[0]).split("/")
    daff=int(daf[len(daf)-1]) 
    assert_contr=daf[len(daf)-2]
    er=po.append(daff)   #----------------->token id
    lp=yu.append(assert_contr)   #------------>contract address
print(len(po))
print(len(yu))


def func_getans(lt_gtt):
    xd=""
    for i in lt_gtt:
        fed="token_ids="+str(i)+"&"
        xd=xd+fed
    print(xd)


    #url = "https://api.opensea.io/api/v1/assets?"+xd+"order_direction=desc&offset=0&limit={}".format(len(lt_gtt)+1)
    url= "https://api.opensea.io/api/v1/assets?"+xd+"&asset_contract_address=0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b&order_direction=desc&offset=0&limit={}".format(len(lt_gtt)+1)

    #r=session.get("https://api.opensea.io/api/v1/assets",params=params)

    #url = "https://api.opensea.io/wyvern/v1/assets?asset_contract_address=0x60e4d786628fea6478f785a6d7e704777c86a7c6&bundled=false&include_bundled=false&"+xd+"limit=5&offset=0&order_by=created_date&order_direction=desc"
    
    response = requests.request("GET", url)
    q=response.json()['assets']
    print(len(q))
   
    for x in range(len(q)):
        print("-----------------------------------")
    #print("slug: "+q[x]['slug'])
        print("token_id: ",q[x]['token_id'])
        #if(q[x]['owner']['user']['username']==)
        if((q[x]['owner']['user'] is not None) and (q[x]['owner']['user']['username'] is not None)):
            print("owner_name: ",q[x]['owner']['user']['username'])
        else:
            print("owner_name:",None)
        print("owner_address: ",q[x]['owner']['address'])
        print("owner_profile_img_url: ",q[x]['owner']['profile_img_url'])
        print("num_sales: ",q[x]['num_sales'])
        if(q[x]['sell_orders'] is not None):
            print("Listing: ",(q[x]['sell_orders'][0]['created_date']))
            if((q[x]['sell_orders'][0]['closing_date']) is not None):  
                print("Last date: ",q[x]['sell_orders'][0]['closing_date'])
                print("Last date: ",q[x]['sell_orders'][0]['closing_extendable'])
            else:
                print("Last date: ",None)
            current_price=((float(q[x]['sell_orders'][0]['current_price']))/1000000000000000000)
            print("current_price(eth): ",current_price)
            
            print("current_price_symbol: ",q[x]['sell_orders'][0]['payment_token_contract']['symbol'])
            print("current_price_token_name: ",q[x]['sell_orders'][0]['payment_token_contract']['name'])
            print("current_price_decimals: ",q[x]['sell_orders'][0]['payment_token_contract']['decimals'])
            print("current_price_usd_price: ",q[x]['sell_orders'][0]['payment_token_contract']['usd_price'])
            print("total_current_price_in_usd: $", ((current_price)*float(q[x]['sell_orders'][0]['payment_token_contract']['usd_price'])))
            
        
            
        else:
            print("Listing: ",None)
        if(q[x]['last_sale'] is not None):
            print("Last_sale_event_timestamp: ",(q[x]['last_sale']['event_timestamp']))
            price=(int(q[x]['last_sale']['total_price'])/1000000000000000000)
            print("Last_sale_price_eth: ",price)
            print("Payment_token_name: ",(q[x]['last_sale']['payment_token']['name']))
            print("Payment_token_symbol: ",(q[x]['last_sale']['payment_token']['symbol']))
            print("Payment_token_symbol: ",(q[x]['last_sale']['payment_token']['decimals']))
            print("Payment_token_symbol_url: ",(q[x]['last_sale']['payment_token']['image_url']))
            print("One_usd_price_day_of_purchase: ",(q[x]['last_sale']['payment_token']['usd_price']))
            print("total_usd_price_convertion: $",((float(q[x]['last_sale']['payment_token']['usd_price']))*price))
            
            if ((q[x]['last_sale']['transaction']['from_account']['user']) is not None):
                print("Last_Sale_user_name: ",(q[x]['last_sale']['transaction']['from_account']['user']['username']))
            else:
                print("Last_Sale_user_name: ",None)
            print("Last_sale_user_address: ",(q[x]['last_sale']['transaction']['from_account']['address']))

        else:
            print("last_sale: ",None)

cfa=func_getans([6,4,5,10,11,12,13,14,15])
#print(len(cfa))



