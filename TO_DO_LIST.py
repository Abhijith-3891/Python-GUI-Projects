#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()

root.geometry("600x600")
root.resizable(0,0)
root.title("To-Do List")
root.configure(bg="lightgreen")

def add():
    task = inputval.get()
    listbox.insert(END,task)
    entry.delete(0,END)
    
def edit():
    for item in listbox.curselection():
        listbox.delete(item)
        listbox.insert(END,inputval.get())
    
def delete():
    if listbox.curselection():
         for item in listbox.curselection():
                value = tmsg.askyesno("Delete task","Do you want to delete a task?")
                if value:
                    listbox.delete(item)
                else:
                    pass
    else:
        tmsg.showinfo("Warning","Please select the task you want to Delete before pressing the Delete button?")
        
def clear():
    value = tmsg.askyesno("Clear All","Do you want to delete all the tasks?")
    if value:
        listbox.delete(0,END)
    else:
        pass
    

def exit():
    value = tmsg.askyesno("Exit","Do you want to exit?")
    if value:
        root.destroy()
    else:
        pass
    
label = Label(root,text="To-Do List",font=("Georgia 30 italic"), bg = "lightgreen",fg="darkblue")
label.place(x=200,y=20)

inputval = StringVar()

entry = Entry(root,textvariable=inputval,bg="#B6FFFA",font=("Lucida",12))
entry.place(x=90,y=150)

# This button is used to add the tasks into the listbox
addbutton = Button(root,text="Add Task",padx=5,pady=10,bg="yellow",fg="black",font=("Lucida",10),command=add)
addbutton.place(x=140,y=200)

editbutton = Button(root,text="Edit",padx=5,pady=10,bg="yellow",fg="black",font=("Lucida",10),command=edit)
editbutton.place(x=152,y=260)

# This button is used to delete the selected task from the listbox
deletebutton = Button(root,text="Delete Task",padx=5,pady=10,bg="yellow",fg="black",font=("Lucida",10),command=delete)
deletebutton.place(x=133,y=320)

# This button is used to clear all the tasks of the listbox
clearbutton = Button(root,text="Clear All",padx=5,pady=10,bg="yellow",fg="black",font=("Lucida",10),command=clear)
clearbutton.place(x=140,y=380)

# This button is used to exit from the tkinter window
exitbutton = Button(root,text="Close Window",padx=5,pady=10,bg="yellow",fg="black",font=("Lucida",10),command=exit)
exitbutton.place(x=125,y=450)

listbox = Listbox(root,height=13,width=16,bg="#FAEAB1",fg="#2192FF",font=("Arial",15,"bold"))
scroller = Scrollbar(root, orient=VERTICAL, command=listbox.yview)
scroller.place(x=558, y=200, height=332)

listbox.config(yscrollcommand=scroller.set)
listbox.place(x=380,y=200)

root.mainloop()


# In[ ]:




