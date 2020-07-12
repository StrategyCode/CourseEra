#Using File /Users/anujsrivastav/Downloads/code3/geodata/where.data
import sqlite3
import urllib.request,urllib.parse,urllib.error
import ssl
import json
import time

LocationFile=input('Please enter the Location File: ')
if len(LocationFile)<1:
    print('Please provide valid input.')
    exit()
else:
    FileHandle=open(LocationFile,'r')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Databse connection Setup
con=sqlite3.connect('geodata.sqlite')
cur=con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

api_key = 42
urltemp = "http://py4e-data.dr-chuck.net/json?"
count=0
for location in FileHandle:
    print('Searching Location:',location)

    if len(location)<1:
        print("No address...")
        break
#Checking if data is laredy loaded
    cur.execute('SELECT geodata FROM Locations where address=?',(location.encode(),))
    try:
        DataCheck=cur.fetchone()[0]
        print('Data Already Loaded:',DataCheck)
        continue
    except:
        pass

#Creating URL to fetch data
    parm=dict()
    parm['address']=location.rstrip()
    parm['key']=api_key
    url=urltemp+urllib.parse.urlencode(parm)
    UrlHandle=urllib.request.urlopen(url)
    UrlData=UrlHandle.read().decode()           #Data is in Json Format here

#Reading data in Json Format
    try:
        JsonData=json.loads(UrlData)
    except:
        print(UrlData)
        continue
    if 'status' not in JsonData or (JsonData['status']!='OK' and JsonData['status'] != "ZERO_RESULT"):
        print('Fail to retrieve data')
        print(UrlData)
        break
    cur.execute('INSERT INTO Locations (address,geodata) VALUES(?,?)',(location.encode(),UrlData.encode()))
    con.commit()
    count=count+1
    if count %20 == 0:
        print('Pausing a bit..')
        time.sleep(5)
print('Program completed')

