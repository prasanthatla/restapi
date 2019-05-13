import  requests
BASE_URL=' http://127.0.0.1:8000/'
ENDPOINT='cbv/'
n=input("enter a number")
req=requests.get(BASE_URL+ENDPOINT+n+'/')
if req.status_code==requests.codes.ok:
    data=req.json()
    print(data)
else:
    print("something wrong ")
    print("status code",req.status_code)