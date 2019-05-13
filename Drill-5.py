from tkinter import *
import tkinter as tk

import os,time
import sqlite3
import shutil


class parentwindow(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)


        self.master=master
        self.master.minsize(470,200)
        self.master.maxsize(470,200)


        self.master.title("Check files")
        self.master.configure(bg="#F0F0F0")
        self.master.protocol("WM_DELETE_WINDOW")
        arg=self.master

        self.txt_source1=tk.Entry(self.master,text='')
        self.txt_source1.grid(row=0,column=1,rowspan=1,columnspan=4,padx=(25,0),pady=(50,0),sticky=N+E+W)
        self.txt_destination2=tk.Entry(self.master,text='')
        self.txt_destination2.grid(row=1,column=1,rowspan=1,columnspan=4,padx=(25,0),pady=(10,0),sticky=N+E+W)
    
        self.btn_source_1=tk.Button(self.master,width=12,height=1,text='Source',command=lambda:browse(self))
        self.btn_source_1.grid(row=0,column=0,padx=(20,0),pady=(50,0),sticky=NW)

        self.btn_destination_2=tk.Button(self.master,width=12,height=1,text='Destination',command=lambda:browse1(self))
        self.btn_destination_2.grid(row=1,column=0,padx=(20,0),pady=(10,0),sticky=NW)
    
        self.btn_movefiles=tk.Button(self.master,width=12,height=2,text='Move Files',command=lambda:browse2(self))
        self.btn_movefiles.grid(row=2,column=0,padx=(20,0),pady=(10,0),sticky=NW)

    

from tkinter import filedialog
from tkinter import *

conn=sqlite3.connect('fdrill.db')
with conn:
    cur= conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_finaldrill(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        col_addfile TEXT)")
    conn.commit()
conn.close()

def browse(self):
    filename = filedialog.askdirectory()
    self.sourceDir = filename
    self.txt_source1.insert(0,filename)
    print(filename)
    return filename


def browse1(self):
    filename1 = filedialog.askdirectory()
    self.sourceDir1 = filename1
    self.txt_destination2.insert(0,filename1)
    print(filename1)
    return filename1
 

def browse2(self):
    for B in os.listdir(self.sourceDir):
        if B.endswith(".txt"):
           c=os.path.join(self.sourceDir,B)
           print("Last modified: %s"%time.ctime(os.path.getmtime(c)))
           print("created: %s" %time.ctime(os.path.getctime(c)))
           shutil.move(c,self.sourceDir1)
           conn=sqlite3.connect('fdrill.db')
           with conn:
               cur=conn.cursor()
               cur.execute("INSERT INTO tbl_finaldrill (col_addfile) VALUES(?)",(B,))   
               conn.commit()
           conn.close()
        
if __name__== "__main__":
    root=Tk()
    App=parentwindow(root)
    root.mainloop(0)
   



