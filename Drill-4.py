from tkinter import *
import tkinter as tk




class parentwindow(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)


        self.master=master
        self.master.minsize(500,150)
        self.master.maxsize(500,150)


        self.master.title("Select File")
        self.master.configure(bg="#F0F0F0")
        self.master.protocol("WM_DELETE_WINDOW")
        arg=self.master
                         
        self.txt_browse1=tk.Entry(self.master,text='')
        self.txt_browse1.grid(row=0,column=3,columnspan=3,padx=(25,0),pady=(50,0),sticky=N+E+W)
       
        
        self.btn_browse_1=tk.Button(self.master,width=12,height=1,text='Browse...',command=lambda:browse_button(self)) #만약에 파일에서 불러오지 않으면 그냥 FUNCTION NAME만 쓰면 된다 
        self.btn_browse_1.grid(row=0,column=0,padx=(20,0),pady=(50,0),sticky=NW)
        
from tkinter import filedialog
from tkinter import *

def browse_button(self):
    filename = filedialog.askdirectory()
    self.txt_browse1.insert(0,filename)#index는 0로다. 글짜하나씩 index로 계산하게되면 텍스트박스안에서 어느 index부터 시작할지 정해주는것이다.
    print(filename)
    return filename                                
                                  


if __name__== "__main__":
    root=tk.Tk()
    App=parentwindow(root)
    root.mainloop(0)
    



