import requests
import pandas as pd
import json

query="""query{
  collections(first:10) {
    edges{
      node{
        imageUrl
      }
      }
  }
  }"""

url = 'https://api.opensea.io/graphql/'
r = requests.post(url, json={'query': query})
print(r.status_code)
print(r.text)