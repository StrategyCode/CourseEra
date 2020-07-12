import json
import urllib.request,urllib.parse,urllib.error

sum=0
url='http://py4e-data.dr-chuck.net/comments_262658.json'
UrlOpen=urllib.request.urlopen(url)
URLData=UrlOpen.read()
print(URLData)
JsonHandle=json.loads(URLData)
count=len(JsonHandle)
for line in JsonHandle['comments']:
    sum=sum+int(line['count'])
print('Total Count:',count)
print('Total Sum:',sum)