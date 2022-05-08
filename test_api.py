import requests
import json
url = "https://data.mongodb-api.com/app/61dbe1e96ce5d97556e9676c/endpoint/data/beta/action/post"

''' payload = json.dumps({
    "collection": "clonex",
    "database": "NewDB_test",
    "dataSource": "Cluster0",
    "": { "nft_name":1  }
})
headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': '30IKXLM246mugpufkgYYUvSmZiz5B0iVP7EyXmfdieFhqoBOCt0HOW78EVSUyNNM'
}
 '''

#print(response.json())

df={"key":"value"}

response = requests.request("POST", url, data=df)



