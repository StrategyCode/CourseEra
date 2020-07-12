#To read the Web Content using URL and get the sum of all numeric Values.

import urllib.request,urllib.error,urllib.parse
import re
from bs4 import BeautifulSoup
sum=0

#Reading the content of Web Page
#WebContent=urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_42.html').read()
WebContent=urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_262655.html').read()

soup=BeautifulSoup(WebContent,'html.parser')
#Extracting the content of Comment
NumContent=re.findall('class="comments">(.+?)<',soup.decode())

#Calculating the Total Sum
for num in NumContent:
    sum=sum+int(num)
print(sum)
