import os,time
A = 'C:\\Users\\H\\Documents\\drill 1 for python'


for B in os.listdir(A):
    if B.endswith(".txt"):
        C=os.path.join(A,B)#B is item from the list not the name of the files(string)
        print(C)
        print("Last modified: %s"%time.ctime(os.path.getmtime(C)))
        print("created: %s" %time.ctime(os.path.getctime(C))) 
        continue
    else:
        continue
