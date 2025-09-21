from tkinter import *

root = Tk()
root.title('Getting Started with Widgets')
root.geometry('400x1000')

desc_lbl = Label(text="Simple calculator",fg="black",bg="white",height=1, width=300)

lbl1 = Label(text="Enter first number:",fg="black",bg="white",height=3, width=300)
entry1 = Entry()

lbl2 = Label(text="Enter second number:",fg="black",bg="white",height=6, width=300)
entry2 = Entry()

lbl3 = Label(text="Choose Operation:",fg="black",bg="white",height=9, width=300)
operations = ["Add","Subtract","Multiply","Divide"]
selected_operation = StringVar()
selected_operation.set("Multiply")
choice = OptionMenu(root, selected_operation, "Add","Subtract","Multiply","Divide")

answer=0
def display():
    if selected_operation.get == "Add":
        answer = entry1+entry2
    elif selected_operation.get == "Subtract":
        answer = entry1 - entry2
    elif selected_operation.get == "Multiply":
        answer = entry1 * entry2
    elif selected_operation.get == "Divide":
        answer = entry1 / entry2
        
    lbl4=Label(text="Answer:",fg="black",bg="white",height=12, width=300)
    lbl5=Label(text=str(answer),fg="black",bg="white",height=13, width=300)

btn = Button(text="begin",command=display, height=1,fg="red",bg="white")






desc_lbl.pack()
lbl1.pack()
entry1.pack()
lbl2.pack()
entry2.pack()
lbl3.pack()
choice.pack()
btn.pack()
root.mainloop()