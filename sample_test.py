''' import requests

url = "https://api.opensea.io/api/v1/events?collection_slug=boredapeyachtclub&event_type=successful&cursor=LWV2ZW50X3RpbWVzdGFtcD0yMDIyLTA0LTExKzEyJTNBMzIlM0E1OS4yMDI2OTcmLXBrPTQ5MTU3NjU3OTI="

headers = {
    "Accept": "application/json",
    "X-API-KEY": "5ca9ad56f654460c95f7c1aa25cbcd13"
}

response = requests.request("GET", url, headers=headers)

print(len(response.json())) '''

from datetime import datetime, timedelta
import time
dtime = datetime. now() + timedelta(seconds=3)
unixtime = time. mktime(dtime. timetuple())

print(unixtime)