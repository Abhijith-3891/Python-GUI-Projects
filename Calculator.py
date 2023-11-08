#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *


# In[2]:


root = Tk()

# The below syntax to set the geometry of tkinter window
root.geometry("500x500")

# The below syntax is not to resize the window
root.resizable(0,0)

# The below syntax set the background colour of GUI to lightgreen
root.configure(background="lightgreen")
root.title("CALCULATOR")

# the following fuctions are used to set the value of corresponding pressed in entry widget
def seven():
    val.set(val.get()+str(7))
    
def eight():
    val.set(val.get()+str(8))
    
def nine():
    val.set(val.get()+str(9))

def four():
    val.set(val.get()+str(4))

def five():
    val.set(val.get()+str(5))

def six():
    val.set(val.get()+str(6))    
    
def three():
    val.set(val.get()+str(3))        
    
def two():
    val.set(val.get()+str(2)) 
    
def one():
    val.set(val.get()+str(1))  

def zero():
    val.set(val.get()+str(0))   
    
def doublezero():  
    val.set(val.get()+str(0)+str(0))

# The following functions is used to perform the required operation    
def mul():
    val.set(val.get()+'*')
    
def equal():    
    expression = val.get()
    total = eval(expression)
    val.set(total)
    
def clear():
    entry.delete(0,END)

def modulo():
    val.set(val.get()+'%')

def delete():
    length = len(entry.get())
    entry.delete(length-1,END)

def division():
    val.set(val.get()+'/')
    
def subtract():
    val.set(val.get()+'-')
    
def add():   
    val.set(val.get()+'+')
    
def dot():
    val.set(val.get()+'.')
    
label = Label(root, text="CALCULATOR")
label.place(x=200,y=20)

val = StringVar("")


entry = Entry(root,text=val,width=30,font=("Times New Roman",20,"bold"))
entry.place(x=40,y=60)

clearbutton = Button(root,text="C",command=clear,width=8,padx=5,pady=5,relief=RAISED)
clearbutton.place(x=60,y=120)

modulobutton = Button(root,text="%",command=modulo,width=8,padx=5,pady=5,relief=RAISED)
modulobutton.place(x=160,y=120)

deletebutton = Button(root,text="del",command=delete,width=8,padx=5,pady=5,relief=RAISED)
deletebutton.place(x=260,y=120)

divbutton = Button(root,text="/",command=division,width=8,padx=5,pady=5,relief=RAISED)
divbutton.place(x=360,y=120)

sevenbutton = Button(root,text="7",command=seven,width=8,padx=5,pady=5,relief=RAISED)
sevenbutton.place(x=60,y=180)

eightbutton = Button(root,text="8",command=eight,width=8,padx=5,pady=5,relief=RAISED)
eightbutton.place(x=160,y=180)

ninebutton = Button(root,text="9",command=nine,width=8,padx=5,pady=5,relief=RAISED)
ninebutton.place(x=260,y=180)

mulbutton = Button(root,text="X",command=mul,width=8,padx=5,pady=5,relief=RAISED)
mulbutton.place(x=360,y=180)

fourbutton = Button(root,text="4",command=four,width=8,padx=5,pady=5,relief=RAISED)
fourbutton.place(x=60,y=240)

fivebutton = Button(root,text="5",command=five,width=8,padx=5,pady=5,relief=RAISED)
fivebutton.place(x=160,y=240)

sixbutton = Button(root,text="6",command=six,width=8,padx=5,pady=5,relief=RAISED)
sixbutton.place(x=260,y=240)

subbutton = Button(root,text="-",command=subtract,width=8,padx=5,pady=5,relief=RAISED)
subbutton.place(x=360,y=240)

onebutton = Button(root,text="1",command=one,width=8,padx=5,pady=5,relief=RAISED)
onebutton.place(x=60,y=300)

twobutton = Button(root,text="2",command=two,width=8,padx=5,pady=5,relief=RAISED)
twobutton.place(x=160,y=300)

threebutton = Button(root,text="3",command=three,width=8,padx=5,pady=5,relief=RAISED)
threebutton.place(x=260,y=300)

addbutton = Button(root,text="+",command=add,width=8,padx=5,pady=5,relief=RAISED)
addbutton.place(x=360,y=300)

doublezerobutton = Button(root,text="00",command=doublezero,width=8,padx=5,pady=5,relief=RAISED)
doublezerobutton.place(x=60,y=360)

zerobutton = Button(root,text="0",command=zero,width=8,padx=5,pady=5,relief=RAISED)
zerobutton.place(x=160,y=360)

dotbutton = Button(root,text=".",command=dot,width=8,padx=5,pady=5,relief=RAISED)
dotbutton.place(x=260,y=360)

equalbutton = Button(root,text="=",command=equal,width=8,padx=5,pady=5,relief=RAISED)
equalbutton.place(x=360,y=360)


root.mainloop()


# In[ ]:




