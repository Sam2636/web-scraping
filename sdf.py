''' import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # This is chrome, you can set whatever browser you like
response = requests.get('https://api.opensea.io/api/v1/assets?asset_contract_address=0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d&limit=30&token_ids=7495&token_ids=3953&token_ids=9606&token_ids=7616&token_ids=4873&token_ids=8811&token_ids=8135&token_ids=446&token_ids=2087&token_ids=73&token_ids=6459&token_ids=5840&token_ids=5230&token_ids=8633&token_ids=4980&token_ids=236&token_ids=8817&token_ids=7265&token_ids=7612&token_ids=2794', headers=headers)
#response = requests.get('https://api.opensea.io/api/v1/events?asset_contract_address=0x3bf2922f4520a8ba0c2efc3d2a1539678dad5e9d&only_opensea=false&offset=0&limit=20', headers=headers)

print (response.status_code)
print (response.url)

print(response.json()['assets'])
 '''

import requests

url = "https://api.opensea.io/api/v1/events?asset_contract_address=0x3bf2922f4520a8ba0c2efc3d2a1539678dad5e9d&only_opensea=false&offset=0&limit=300"

headers = {
    "Accept": "application/json",
    "X-API-KEY": "5ca9ad56f654460c95f7c1aa25cbcd13"
}

response = requests.request("GET", url, headers=headers).json()['asset_events']#['asset']
#print((response))
for x in response:
    y=int(x['asset']['token_id'])
    #print(x['asset']['token_id'])
    if(y==6745):
        print(x)
#print(response.text)