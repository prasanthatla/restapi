import requests
BASE_URL=' http://127.0.0.1:8000/'
ENDPOINT=''
R=requests.get(BASE_URL+ENDPOINT)
print(R.json())