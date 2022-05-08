""" from web3.auto import w3

# which is equivalent to:

from web3 import Web3
w3 = Web3() 

 """

input=1
#s="""{cwecewcqewc{sas}xwqx}""".format(sas="1")
s="""{{
ethereum {{
inbound: coinpath(initialAddress: {{is: "0x575757e0a0b19bee7e07887fbbd616b395e32d4b"}}, currency:{{is: "ETH"}}, depth: {vgh}, options: {{direction: inbound, asc: "depth", desc: "amount", limitBy: {{each: "depth", limit: {vgh}}}}}, date:{{since: null, till: null}){{
sender {{
address
annotation
smartContract {{
contractType
currency {{
symbol
name
}}}}
}}
receiver {{
address
annotation
smartContract {{
contractType
currency {{
symbol
name
}}}}
}}
amount
currency{vgh}
depth
count
}}
outbound: coinpath(initialAddress: {{is: "0x575757e0a0b19bee7e07887fbbd616b395e32d4b"}}, currency:{{is: "ETH"}}, depth: {vgh}, options: {{asc: "depth", desc: "amount", limitBy: {{each: "depth", limit: 2}}}}, date:{{since: null, till: null}}){{
sender {{
address
annotation
smartContract {{
contractType
currency {{
symbol
name
}}}}
}}
receiver {{
address
annotation
smartContract {{
contractType
currency {vgh}
symbol
name
}}}}
}}
amount
currency{symbol}
depth
count
}}}}
}}""".format(vgh="1")

print(s)