from tkinter import *
from datetime import date

root = Tk()
root.title('Getting Started with Widgets')
root.geometry('400x300')

lbl=Label(text="hey there!",fg="white",bg="black",height=1, width=300)

name_lbl=Label(text="Full name", bg="white")
name_entry = Entry()

def display():
    name = name_entry.get()
    message = "welcome to the application! \nToday's date is: "
    greet="\nHello "+name+"\n"
    
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())
text_box = Text(height=3)

def clear():
    text_box.delete(1.1,END)

btn = Button(text="begin",command=display, height=1,fg="red",bg="black")
clr = Button(text="clear",command=clear, height=1,fg="red", bg="black")

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
clr.pack()
text_box.pack()
root.mainloop()