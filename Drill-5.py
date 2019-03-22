import os,time
import sqlite3
import shutil

conn=sqlite3.connect('fdrill.db')
with conn:
    cur= conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_finaldrill(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        col_addfile TEXT)")
    conn.commit()
conn.close()

A='C:\\Users\\12147\\Desktop\\final drill'

for B in os.listdir(A):
    if B.endswith(".txt"):
        C=os.path.join(A,B)#B is item from the list not just name of the files(sting)
        print(C)
        print("Last modified: %s"%time.ctime(os.path.getmtime(C)))
        print("created: %s" %time.ctime(os.path.getctime(C)))
        shutil.move(B,"C:\\Users\\12147\\Desktop\\here")
        conn=sqlite3.connect('fdrill.db')
        with conn:
            cur=conn.cursor()
            cur.execute("INSERT INTO tbl_finaldrill (col_addfile) VALUES(?)",(B,))   
            conn.commit()
    conn.close()
    # C=os.path.join(A,B)#B is item from the list not just name of the files(sting)
    # print(C)
    # print("Last modified: %s"%time.ctime(os.path.getmtime(C)))
    # print("created: %s" %time.ctime(os.path.getctime(C)))
    # shutil.move(B,"C:\\Users\\12147\\Desktop\\here")
