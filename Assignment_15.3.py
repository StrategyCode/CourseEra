#Using File /Users/anujsrivastav/Downloads/code3/roster/roster_data.json
import sqlite3
import json
FileName=input('Please enter File Name: ')

#Reading JSON File
FileHandle=open(FileName,'r')
JsonData=json.load(FileHandle)

#Creating Table
con=sqlite3.connect('coursedb.sqlite')
cur=con.cursor()
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')
for line in JsonData:
    cur.execute('INSERT OR IGNORE INTO User (name) VALUES(?)',(line[0],))
    cur.execute('SELECT id FROM User WHERE name=?',(line[0],))
    UserId=cur.fetchone()[0]
    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES(?)',(line[1],))
    cur.execute('SELECT id FROM Course WHERE title=?',(line[1],))
    CourseId=cur.fetchone()[0]
    cur.execute('INSERT OR IGNORE INTO Member (role,user_id,course_id) VALUES(?,?,?)', (line[2],UserId,CourseId))
    con.commit()
con.close()
