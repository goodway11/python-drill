import os
import sqlite3

conn=sqlite3.connect('drill2.db')
with conn:
    cur= conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_drill2(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        col_name TEXT)")

    conn.commit()
conn.close()

fileList = ('information.docx','Hello.txt','myImage.png',
          'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
for B in fileList:
    if B.endswith(".txt"):
        conn=sqlite3.connect('drill2.db')
        with conn:
            cur=conn.cursor()
            cur.execute("INSERT INTO tbl_drill2 (col_name) VALUES(?)",(B,))    
            conn.commit()
        conn.close()
        print(B)
      
