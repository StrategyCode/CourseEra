import xml.etree.ElementTree as ET
import ssl
import urllib.request,urllib.parse,urllib.error

count=0
sum=0

XMLUrl="http://py4e-data.dr-chuck.net/comments_262657.xml"
if len(XMLUrl) <1:
    print("Url not provided. Exiting..")
    exit()

XMLHandle=urllib.request.urlopen(XMLUrl)
XMLData=XMLHandle.read().decode()
tree=ET.fromstring(XMLData)
for line in tree.findall('comments/comment'):
    count=count+1
    sum=sum+int(line.find('count').text)
print('Total Comments:',count)
print('Total Sum:',sum)