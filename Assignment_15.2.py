#Using file /Users/anujsrivastav/Downloads/code3/tracks/Library.xml
import xml.etree.ElementTree as ET
import sqlite3
XMLFile=input('Enter the File:')
tree=ET.parse(XMLFile)
SongDetails=tree.findall('dict/dict/dict')
print('Dict count:', len(SongDetails))
def TrackDetails(obj,Val):
    Flag=False
    for tagval in obj:
        if Flag:
            return tagval.text
        if tagval.tag == 'key' and tagval.text == Val:
            Flag=True
    return None

#DB Connection
conn=sqlite3.connect('trackdb.sqlite')
cur=conn.cursor()

#Creating Table
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;''')
conn.commit()
cur.executescript('''
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);''')
conn.commit()

for line in SongDetails:
    TrackName=TrackDetails(line,'Name')
    ArtistName=TrackDetails(line,'Artist')
    AlbumName=TrackDetails(line,'Album')
    GenreName=TrackDetails(line,'Genre')
    TrackLength=TrackDetails(line,'Total Time')
    Rating=TrackDetails(line,'Rating')
    Count=TrackDetails(line,'Play Count')
    if TrackName is None or ArtistName is None or AlbumName is None or GenreName is None:
        continue
    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)',(ArtistName,))
    ArtistId=cur.execute('SELECT id FROM Artist WHERE name = ?',(ArtistName,)).fetchone()[0]
    cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)',(GenreName,))
    GenreId=cur.execute('SELECT id FROM Genre WHERE name=?',(GenreName,)).fetchone()[0]
    cur.execute('INSERT OR IGNORE INTO Album (artist_id,title) VALUES (?,?)',(ArtistId,AlbumName))
    AlbumId=cur.execute('SELECT id FROM Album WHERE title=?',(AlbumName,)).fetchone()[0]
    cur.execute('INSERT OR IGNORE INTO Track (title,album_id,genre_id,len,rating,count) VALUES (?,?,?,?,?,?)',(TrackName,AlbumId,GenreId,TrackLength,Rating,Count))
    conn.commit()
conn.close()