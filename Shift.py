import tkinter as tk
from tkinter import BOTH,END,LEFT
root =tk.Tk()
root.geometry("400x100")

def my_upd():
    t2.insert(tk.END, t1.get('1.0',END))
    t1.delete('1.0',END)



l1=tk.Label(root,text="Enter Text: ")
l1.grid(row=1,column=1)
t1=tk.Text(root,height=1,width=15,bg="yellow")
t1.grid(row=1,column=2)

b1=tk.Button(root,text='UPDATE',command=lambda:my_upd())
b1.grid(row=1,column=3)

t2=tk.Text(root,height=1,width=15,bg="yellow")
t2.grid(row=1,column=4)




root.mainloop()