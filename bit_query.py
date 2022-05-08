#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests


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
query ($network: EthereumNetwork!, $address: String!, $limit: Int!, $offset: Int!, $from: ISO8601DateTime, $till: ISO8601DateTime) {
  ethereum(network: $network) {
    smartContractCalls(
      options: {desc: "block.timestamp.time", limit: $limit, offset: $offset}
      date: {since: $from, till: $till}
      smartContractAddress: {is: $address}
    ) {
      block {
        timestamp {
          time(format: "%Y-%m-%d %H:%M:%S")
        }
        height
      }
      smartContractMethod {
        name
        signatureHash
      }
      address: caller {
        address
        annotation
      }
      transaction {
        hash
      }
      gasValue
      external
    }
  }
}


"""
result = run_query(query)  # Execute the query
print ('Result - {}'.format(result))