import json
import requests
import pandas as pd

input_address=input("Enter the Wallet Address:")
depth=input("Enter the number incoming and outgoing transactions:")
def run_query(query):  # A simple function to use requests.post to make the API call.
    headers = {'X-API-KEY': 'BQY5AgJaWVnvLParWhqFEaqrnJwD2NFf'}
    request = requests.post('https://graphql.bitquery.io/',
                            json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Query failed and return code is {}.      {}'.format(request.status_code,
                        query))


# The GraphQL query

query = """
{
  ethereum(network: ethereum) {
    transfers(
      options: {desc: "block.timestamp.time", limit: 1000000}
      date: {since: null, till: null}
      amount: {gt: 0}
      receiver: {is: "0x0f212042347bd15210c66c01a3109c3157f2a12a"}
    ) {
      block {
        timestamp {
          time(format: "%Y-%m-%d %H:%M:%S")
        }
      }
      address: sender {
        address
      }
     
    }
  }
}

"""
#result = run_query(query)
result = run_query(query)  # Execute the query
bit_rslt=result
print(result)
