from tkinter import *
import tkinter as tk


import checkbox_main



def create_gui(self):
    self.txt_browse1=tk.Entry(self.master,text='')
    self.txt_browse1.grid(row=0,column=1,rowspan=1,columnspan=4,padx=(25,0),pady=(50,0),sticky=N+E+W)
    self.txt_browse2=tk.Entry(self.master,text='')
    self.txt_browse2.grid(row=1,column=1,rowspan=1,columnspan=4,padx=(25,0),pady=(10,0),sticky=N+E+W)
    
    self.btn_browse_1=tk.Button(self.master,width=12,height=1,text='Browse...')
    self.btn_browse_1.grid(row=0,column=0,padx=(20,0),pady=(50,0),sticky=NW)

    self.btn_browse_2=tk.Button(self.master,width=12,height=1,text='Browse...',)
    self.btn_browse_2.grid(row=1,column=0,padx=(20,0),pady=(10,0),sticky=NW)
    
    self.btn_checkfiles=tk.Button(self.master,width=12,height=2,text='Check for files...')
    self.btn_checkfiles.grid(row=2,column=0,padx=(20,0),pady=(10,0),sticky=NW)

    self.btn_close=tk.Button(self.master,width=12,height=2,text='Close Program')
    self.btn_close.grid(row=2,column=4,padx=(220,20),pady=(10,0),sticky=SE)


    

