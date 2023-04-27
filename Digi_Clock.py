import time
from tkinter import *

root = Tk()

root.geometry("360x150+0+0")
root.config(bg="black")
root.title("*****Digital Clock*****")
root.resizable(0,0)

def start():
    text = time.strftime("%H:%M:%S")
    label.config(text=text)
    label.after(200,start)

label = Label(root,font=("ds-digital",50,"bold"),bg="black",fg='red')
label.grid(row=2,column=1,padx=5,pady=10)
start()
print("done")
root.mainloop()