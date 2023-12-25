from tkinter import *
from tkinter import messagebox
root=Tk()

root.title("adding two numbers")
root.geometry("400x600")

terms=Entry(root,font=("arial",18,"bold"))
terms.place(relx=0.5,rely=0.6,anchor=CENTER)

lbl1=Label(root,text="enter first num")
lbl1.place(relx=0.5,rely=0.5,anchor=CENTER)

lbl2=Label(root)
lbl2.place(relx=0.5,rely=0.9,anchor=CENTER)
    

def add():
    try:
        a=5
        b=(terms.get())
        c=a+b
        lbl2["text"]="answer:"+str(c)
        
    except(TypeError):
         messagebox.askokcancel("error","cannot add two different datatypes int and str")

showResults=Button(root,text="show results",command=add)
showResults.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()