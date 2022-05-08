import requests

url = "https://qzlsklfacc.medianetwork.cloud/query_volume_all"

headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers)

print(response.text)

