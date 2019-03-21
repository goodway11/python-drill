from tkinter import *
import tkinter as tk


import checkbox_gui



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

        checkbox_gui.create_gui(self)                             
        





if __name__== "__main__":
    root=tk.Tk()
    App=parentwindow(root)
    root.mainloop(0)
