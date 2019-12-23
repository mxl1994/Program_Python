# -*- coding=utf-8 -*-

import os
import time
import json
import random
import requests
import threading
from multiprocessing.dummy import Pool

def get_request_parmas(host_list, filename):
    fullname = os.path.join(os.getcwd(), filename)
    with open(fullname, 'r') as fr:
        global num
        for line in fr:
            temp = line.strip('\n').split('\t')
            if temp[2] in (None, '', '\t', '\n', '\r') or '/third/cheji/v3' in temp[5]:
                continue
            path = (temp[5].split('?')[0]).strip('').strip('\n')
            parmas = dict()
            if '/third/beanq/v3' in path:
                parmas = {
                    "agentid": auth.get('dy').keys()[0],
                    "token": auth.get('dy').values()[0]
                }
            elif '/third/os/query/tmp' in path and temp[3] == auth.get('dd').keys()[0]:
                parmas = {
                    "agentid": auth.get('dd').keys()[0],
                    "token": auth.get('dd').values()[0]
                }
            elif '/v2/query' in path:
                parmas = {
                    "agentid": temp[3],
                    "token": auth.get('v2').get(temp[3])
                }
            elif '/third/storybox' in path:
                parmas = {
                    "agentid": auth.get('story').keys()[0],
                    "token": auth.get('story').values()[0]
                }
            else:
                continue
            num += 1
            parmas.update({
                "query": temp[2],
                "sessionId": temp[0] + '_' + str(num) + '_' + 'test',
                "location": {
                    "latitude": 39.90983,
                    "longitude": 116.43512
                }
            })

            flg = random.randint(0, len(host_list)-1)
            host = host_list[flg]

            request = {
                "url": 'http://' + host + temp[5].split('?')[0],
                "parmas": parmas
            }
            yield request

def request_post(request):

    url = request.get('url')
    parmas = request.get('parmas')
    lock.acquire()
    print parmas.get('sessionId')
    lock.release()
    result = requests.post(url=url, data=json.dumps(parmas))
    result_text = (result.text).replace('\n', '').replace('\r', '').replace('\t', '').replace(' ','')
    result_str = (parmas.get('sessionId') + '\t' + parmas.get('query') + '\t' + parmas.get('agentid') +
                   '\t' + parmas.get('token') + '\t' + request.get('url') + '\t' + result_text.encode('utf-8'))
    lock.acquire()
    fw.write(result_str + '\n')
    lock.release()

if __name__ == '__main__':
    start_time = time.time()
    num = 0
    auth = {
        'dd': {
            'MTZjMmFoWVRGa1l6UmlORFUwWlRFZWIxYw==': 'd30aa8aa67589f8d99e52ec4d2332eb89049'
        },
        'dy': {
            'MmI4MjMyODI3YzRl': '0ba624f353f117c6273be39758fce8f84327'
        },
        'story': {
            'I4MzMxZWNhNWI0OW': '287497f4cc28abcc2f64b52d5a486f4e8166'
        },
        'v2': {
            '4ZDM2OWQ1ZGEwOTY': '8429b25c4e2dd0d188240c516d87c1524352',
            'c3NWJlZDVlYTZmNT': '2dfaae3c455c260ca33efab46cde0c342616',
            'dkYjU3MDgwODI4Mz': 'dacbc5227e2f061afafdc355db7b4bc28234',
            'MTI1Y2FEVXlOVEZtWlRVNFpqUTVOZjJiYQ==': 'ecc2d28eeb6f3c324e4c8c5adf5bf37e2481',
            'NlYTk5NjBjMDRjYz': 'a0301999f0037461ebf64e03b0d761cf5860'
        }
    }
    lock = threading.Lock()
    filename = 'rda_result'
    fullname = os.path.join(os.getcwd(), filename)
    fw = open(fullname, 'a')
    ip_list = ['10.25.142.116:8081', '10.27.74.53:8081', '10.27.75.162:8081', '10.27.78.16:8081', '10.27.78.35:8081','10.27.240.124:8081', '10.27.241.111:8081']
    parmas_list = get_request_parmas(ip_list, 'nlu_cc_query_0802')
    pool = Pool(5)
    pool.map_async(request_post, parmas_list)
    pool.close()
    pool.join()
    fw.close()
    end_time = time.time() - start_time
    print end_time
