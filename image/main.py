import requests
import json

from requests.api import get
from secret import serviceIP

geturl = f'{serviceIP}/get_task'
sendurl = f'{serviceIP}/push_result'

resp = requests.get(geturl)
task = resp.json()
print(task)
# id a b

param = {
    'id': task["id"],
    'result': task["a"]+task["b"]
    }

json_param = json.dumps(param)

print(json_param)

resp = requests.post(sendurl, data=json_param)

print(resp)
