# -*-coding: utf-8 -*-

import json
import requests

# url = 'http://192.168.1.44:8081/third/beanq/v3'
url = 'http://10.45.137.51:8081/third/beanq/v3'

parmas = {
    "query": "大年三十",
    "agentid": "lOTc4Y2QxYmYzNjR",
    "token": "d008ed014935ceec9020c1183bce450e5951",
    "sessionId": "1",
    "location": {
        "latitude": 40.040562,
        "longitude": 116.415884
    }
}

result = requests.post(url=url, data=json.dumps(parmas))

# print result.url
# print json.dumps(parmas, ensure_ascii=False)
print "text:", result.text
# print result.json()["results"][0]["hint"]
# print "=" * 100