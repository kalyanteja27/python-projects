from tkinter import *
root=Tk()
import tkinter.messagebox as msg
root.title("loging form")
root.geometry("570x600+100+200")
root.resizable(False ,False)
root.config(bg="#F6E5E5")

equation =""
def show(v):
    global equation
    equation+=v#e="8*7"
    label_result.config(text=equation)

equation =" "
def clear ():
    global equation
    equation=" "
    label_result.config(text=equation)

def calculate():
    global equation
    result =" "
    if equation!=" ":
        try:
            result=eval(equation)
        except:
            result ="error"
            equation=""
    label_result.config(text=result)

label_result=Label(root,width=500,height=3,text="",font=("arial",30),bg="#DDCBE1")
label_result.pack()
Button(root,text="c",width=5,height=1,font=("arial",30,"bold"),bg="#CECECE",command=lambda:clear(), fg="blue").place(x=40,y=100)
Button(root,text="/",width=5,height=1,font=("arial",30,"bold"),bg="#fff",command = lambda :show("/"),fg="blue").place(x=170,y=100)
Button(root,text="%",width=5,height=1,font=("arial",30,"bold"),bg="#fff",command = lambda :show("%"),fg="blue").place(x=300,y=100)
Button(root,text="*",width=5,height=1,font=("arial",30,"bold"),bg="#fff",command = lambda :show("*"),fg="blue").place(x=430,y=100)


Button(root,text="9",width=5,height=1,font=("arial",30,"bold"),bg="#fff",command = lambda :show("9"),fg="blue").place(x=40,y=200)
Button(root,text="8",width=5,height=1,font=("arial",30,"bold"),bg="#fff",command = lambda :show("8"),fg="blue").place(x=170,y=200)
Button(root,text="7",width=5,height=1,font=("arial",30,"bold"),bg="#fff",command = lambda :show("7"),fg="blue").place(x=300,y=200)
Button(root,text="-",width=5,height=1,font=("arial",30,"bold"),bg="#fff",command = lambda :show("-"),fg="blue").place(x=430,y=200)


Button(root,text="6",width=5,height=1,font=("arial",30,"bold"),bg="#fff",command = lambda :show("6"),fg="blue").place(x=40,y=300)
Button(root,text="5",width=5,height=1,font=("arial",30,"bold"),bg="#fff",command = lambda :show("5"),fg="blue").place(x=170,y=300)
Button(root,text="4",width=5,height=1,font=("arial",30,"bold"),bg="#fff",command = lambda :show("4"),fg="blue").place(x=300,y=300)
Button(root,text="+",width=5,height=1,font=("arial",30,"bold"),bg="#fff",command = lambda :show("+"),fg="blue").place(x=430,y=300)

Button(root,text="3",width=5,height=1,font=("arial",30,"bold"),bg="#fff",command = lambda :show("3"),fg="blue").place(x=40,y=400)
Button(root,text="2",width=5,height=1,font=("arial",30,"bold"),bg="#fff",command = lambda :show("2"),fg="blue").place(x=170,y=400)
Button(root,text="1",width=5,height=1,font=("arial",30,"bold"),bg="#fff",command = lambda :show("1"),fg="blue").place(x=300,y=400)
Button(root,text="=",width=5,height=3,font=("arial",30,"bold"),bg="#fff",command = lambda :calculate(),fg="blue").place(x=430,y=400)

Button(root,text="0",width=10,height=1,font=("arial",30,"bold"),bg="#fff",command = lambda :show("0"),fg="blue").place(x=40,y=500)
Button(root,text=".",width=5,height=1,font=("arial",30,"bold"),bg="#fff",command = lambda :show("."),fg="blue").place(x=290,y=500)


root.mainloop()