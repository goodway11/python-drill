import os
import sqlite3

conn=sqlite3.connect('drill2.db')

with conn:
    cur= conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_company(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        col_name TEXT,\
        col_phone TEXT,\
        col_email TEXT \
        )")
    conn.commit()
conn.close()


conn=sqlite3.connect('drill2.db')

with conn:
    cur=conn.cursor()
    cur.execute("INSERT INTO tbl_company (col_name, col_phone,col_email) VALUES(?,?,?)",\
                ('A_company','111-111-1111','Acompany@mail.com'))
    cur.execute("INSERT INTO tbl_company (col_name, col_phone,col_email) VALUES(?,?,?)",\
                ('B_company','111-111-1112','Bcompany@mail.com'))          
    cur.execute("INSERT INTO tbl_company (col_name, col_phone,col_email) VALUES(?,?,?)",\
                ('C_company','111-111-1113','Ccompany@mail.com'))
    conn.commit()
conn.close()


fileList = ('information.docx','Hello.txt','myImage.png',\
          'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
for B in fileList:
    if B.endswith(".txt"):
        print(B)
      
