from tkinter import *
import hashlib
def button_press():
    user=username.get()
    pas=password.get()
    if (user=="" or pas==""):
       label3["text"]=str("Enter a username or password")
    else:
        pas=hashlib.md5((password.get()).encode("utf-8")).hexdigest()
        if (username=="guest" and pas=="804c46cfec3d10628803370cfbc46b36"):
            label3["text"]="hello Mr." + str(username)
        else:
            label3["text"]="Incorrect username or password"
window= Tk()
window.geometry("500x400")
window.title("Login")
label0= Label(text="Login",font=("cosolas",20))
label0.pack()
frame= Frame()
frame.pack()
label1=Label(frame,text="Username",font=("cosolas",20))
label2=Label(frame,text="Password",font=("cosolas",20))
label1.grid(row=0,column=0)
label2.grid(row=1,column=0)
username = Entry(frame,font= ("algerian",20),fg = "black",bg = "white")
username.grid(row=0,column=1)
password = Entry(frame,font= ("algerian",20),fg = "black",bg = "white")
password.grid(row=1,column=1)
button1= Button(text="Login", width=9, height=4, font=20, command= button_press)
button1.pack()
label3=Label(text="",font=("cosolas",20),fg="red")
label3.pack()
window.mainloop()