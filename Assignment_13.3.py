import json
import urllib.request,urllib.parse,urllib.error
api_key=None
while True:
    Address=input("Enter Location: ")
    if len(Address)<1:
        break
    if api_key is None:
        api_key=42
    params=dict()
    params['address']=Address
    params['key'] = api_key
    url='http://py4e-data.dr-chuck.net/json?' + urllib.parse.urlencode(params)
    print('URL:',url)
    UrlHandle=urllib.request.urlopen(url)
    UrlData=UrlHandle.read().decode()
    JsonHandle=json.loads(UrlData)
    print(JsonHandle)
    print("place_id: ",JsonHandle['results'][0]['place_id'])