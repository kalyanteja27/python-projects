from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

def login():
     if usernameEntry.get()==' ' or passwordEntry.get()=='':
         messagebox.showerror('Error','Fields cancont be empty')
     elif usernameEntry.get()=='Faizan' and  passwordEntry.get()=='123':
         messagebox.showinfo('Success','Welcome')
     else:
          messagebox.showinfo('error','please enter correct credentials')

window=Tk()
window.geometry("1250x700+0+0")#0 is distace from the x axis ,0 is distance from y axis
#window.resizable(False,False)
backgroundImage=ImageTk.PhotoImage(file='pexels-katlovessteve-548389.jpg',size=(1280,700))
bgLabel=Label(window,image=backgroundImage,width="1600", height="900")
bgLabel.place(x=0,y=0)
loginFrame=Frame(window,bg="white")
loginFrame.place(x=400,y=150)

loginImage=PhotoImage(file='logo.png')
logoLabel=Label(loginFrame,image=loginImage)
logoLabel.grid(row=0,column=0,columnspan=4,pady=10)


usernameImage=PhotoImage(file='usernameImage.png')
usernameLabel=Label(loginFrame,image=usernameImage,text='Username',compound=LEFT,bg="white",font=('times new roman',20,'bold'))
usernameLabel.grid(row=4,column=0,pady=10,padx=20)
usernameEntry=Entry(loginFrame,font=('arial',20),bd=5,fg='royalblue')
usernameEntry.grid(row=4,column=2,pady=10,padx=20)

passwordImage=PhotoImage(file='passwordimage.png')
passwordLabel=Label(loginFrame,image=passwordImage,text='Password',compound=LEFT,bg="white",font=('times new roman',20,'bold'))
passwordLabel.grid(row=6,column=0,pady=10,padx=20)
passwordEntry=Entry(loginFrame,font=('arial',20),bd=5,fg='royalblue')
passwordEntry.grid(row=6,column=2,pady=10,padx=20)

loginButton=Button(loginFrame,text='login',font=('arial',14),pady=10,widt=15,fg='white',bg='cornflowerblue',activebackground='cornflowerblue',activeforeground="white",cursor='hand2',command=login)
loginButton.grid(row=8,column=2)
window.mainloop()