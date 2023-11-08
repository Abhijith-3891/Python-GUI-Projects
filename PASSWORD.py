#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *


# In[4]:


import random

root = Tk()

root.geometry("500x500")
root.resizable(0,0)

root.configure(background="lightblue")

root.title("PYTHON PASSWORD GENERATOR")

checkone = IntVar()
checktwo = IntVar()

def generate_password(length):
    character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$%&*"
    password="".join(random.sample(character,length))
    entry.delete(0,END)
    entry.insert(0,password)
    
def password_length():
    if checkone.get() == 6:
        generate_password(6)
        
    elif checktwo.get() == 10:
        generate_password(10)
        
    else:
        generate_password(8)
    
val = StringVar()

label = Label(root,text="PASSWORD GENERATOR",padx=5,pady=5,font=("Times New Roman",15,"bold"))
label.place(x=125,y=20)

entry = Entry(root,text=val,width=25,font=("Times New Roman",20,"bold"))
entry.place(x=90,y=80)

one = Checkbutton(text = '6 Char',onvalue=6, offvalue=0, variable=checkone,padx=10,pady=5,font=("Times New Roman",15))
one.place(x=200,y=140)

two = Checkbutton(text = '10 Char',onvalue=10, offvalue=0, variable=checktwo,padx=5,pady=5,font=("Times New Roman",15))
two.place(x=200,y=200)

button = Button(root,text="Password",command=password_length,width=8,padx=5,pady=5,relief=RAISED,font=("Times New Roman",15))
button.place(x=200,y=260)

root.mainloop()


# In[ ]:




