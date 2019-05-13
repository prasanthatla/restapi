import requests
import json
BASE_URL=' http://127.0.0.1:8000/'
ENDPOINT='cbv/'
def create_resource():
    new_emp={
        'eno':105,
        'ename':'hindhu sree',
        'esal':5000.0,
        'eaddr':"nellore"
    }
    r=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
    print(r.status_code)
    print(r.json())
def update_resource():
    new_emp = {
        'eno': 105,
        'ename': 'hindhu sree',
        'esal': 5000.0,
        'eaddr': "nellore"
    }
    r = requests.post(BASE_URL + ENDPOINT+'1/',data=json.dumps(new_emp))
    print(r.status_code)
    print(r.json())

    update_resource()

# create_resource()