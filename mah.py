import requests

res = requests.get('https://opensea.io/')

print(res.text)
print(res.status_code)