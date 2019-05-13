import requests
import json

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT='API/'
def get_resourses(id=None):
    data={}
    if id is not None:
        data={
        'id':id
        }
    req=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(req.json())
    print(req.status_code)

# get_resourses(8)
def create_resourses():
    data={
        'eno':104,
        'ename':'chinna',
        'esal':4200,
        'eaddr':'my '
    }
    req = requests.post(BASE_URL + ENDPOINT, data=json.dumps(data))
    print(req.json())
    print(req.status_code)

create_resourses()
def update_resourse():
    data = {
        'id':3,
        'ename': 'chinna',
        'esal': 40200,
        'eaddr': 'nellore'
    }
    req = requests.put(BASE_URL + ENDPOINT, data=json.dumps(data))
    print(req.json())
    print(req.status_code)

# update_resourse()
def delete_resourse(id=None):
    data = {}
    if id is not None:
        data = {
            'id': id
        }
    req = requests.delete(BASE_URL + ENDPOINT, data=json.dumps(data))
    print(req.json())
    print(req.status_code)

# delete_resourse()
