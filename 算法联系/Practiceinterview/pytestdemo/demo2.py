# -*- coding:utf-8 -*-
import pytest
import requests
import json

@pytest.mark.website
def test_1():
    params = {
        "query": "查询闹钟",
        "sessionId": "400010B400000005",
        "token": "4249a3ff83a68a00cc8e8048c1c927cc8818",
        "agentid": "4ZGJjMzA4NWVhNmM",
        "location": {
            "latitude": 39.90983,
            "longitude": 116.43512
        }
    }
    response = requests.post("http://192.168.1.44:8081/third/storybox/v3",data=params)
    response = json.loads(response.text)
    assert response["status"]["code"]==401