import xml.etree.ElementTree as ET
import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('ass-4c-3w.sqlite')
cur = conn.cursor()

cur.execute('''SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3
    ''')


sqlresult = cur.fetchall()
print sqlresult
print

print tabulate(sqlresult, headers=['Title','Artist Name','Album name','Genre name'])
print

for row in sqlresult:
  for i in range(0,3):
    print row[i]+" ||",
  print