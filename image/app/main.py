import requests
import json
import os

from requests.api import get

serviceAddr = os.getenv('SERVICE_ADDR')

geturl = f'{serviceAddr}/get_task'
sendurl = f'{serviceAddr}/push_result'

resp = requests.get(geturl)
task = resp.json()
#print(task)
# id a b

param = {
    'id': task["id"],
    'result': task["a"]+task["b"]
    }

json_param = json.dumps(param)

#print(json_param)
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
resp = requests.post(sendurl, data=json_param, headers=headers)

print(resp)
