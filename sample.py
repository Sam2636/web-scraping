import requests
import csv 
import concurrent.futures

proxylist=[]
pl=[]
with open('proxy.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        proxylist.append(row)
print(len(proxylist))        

def extract(proxy):
    try:
        r=requests.get('https://httpbin.org/ip',proxies={'http':proxy,'https':proxy},timeout=2)
        print(r.json(),'working--->')
        pl.append(r.json())
    except:
        print("notworking")
        pass    

    return proxy

extract('')


with concurrent.futures.ThreadPoolExecutor()  as exector:
    exector.map(extract,proxylist) 

print(pl)
