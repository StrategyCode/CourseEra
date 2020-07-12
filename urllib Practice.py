# import urllib.request,urllib.parse,urllib.error
# from bs4 import BeautifulSoup
# import re
#
#LastName=None
# NameSequence=list()
# LinkName='http://py4e-data.dr-chuck.net/known_by_Fikret.html'
# for i in range(5):
#     WebContent=urllib.request.urlopen(LinkName).read()
#     CorrectedWebPage=BeautifulSoup(WebContent.decode(),'html.parser')
#     LinkTags=CorrectedWebPage('a')
#     TitleName=re.findall('<title>People that (.+?) ',str(CorrectedWebPage('title')[0]))
#     NameSequence.append(TitleName)
#     LinkName=re.findall('href="(.+?)">', str(LinkTags[2]))[0]
#     LastName=TitleName
#print(LastName[0])

import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import re
LinkName=input('Enter Link: ')

LastName=None
#LinkName='http://py4e-data.dr-chuck.net/known_by_Alanis.html'
for i in range(8):
    WebContent=urllib.request.urlopen(LinkName).read()
    CorrectedWebPage=BeautifulSoup(WebContent.decode(),'html.parser')
    LinkTags=CorrectedWebPage('a')
    TitleName=re.findall('<title>People that (.+?) ',str(CorrectedWebPage('title')[0]))
    LastName=TitleName
    LinkName=re.findall('href="(.+?)">', str(LinkTags[17]))[0]
print(LastName[0])