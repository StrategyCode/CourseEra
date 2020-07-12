#Using file: /Users/anujsrivastav/Downloads/code3/mbox.txt
import sqlite3

FileName=input('Enter the File Name: ')
FileHandle=open(FileName,'r')
Domain=dict()

#Forming a dictionary in the form of (Domain,Count present)

for line in FileHandle:
    if not line.startswith('From '):
        continue
    else:
        Key = str(line.rstrip().split()[1].split('@')[1])
        if Domain.get(Key,0) == 0:
            Domain[Key]=1
        else:
            Domain[Key]=int(Domain.get(Key,1)) + 1

#Using the value of dictionary "Domain", will load the data in Database

#Establishing connection with database
conn=sqlite3.connect('DomainCount.sqlite')
cur=conn.cursor()
cur.execute('drop table if exists Counts')
cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')
for k,v in Domain.items():
    cur.execute('INSERT INTO Counts values (?,?)',(k,v))
conn.commit()
print(cur.execute('''select * from Counts''').fetchall())
conn.close()