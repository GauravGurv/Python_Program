from tkinter import *
import speedtest

def speedcheck():
    root = speedtest.Speedtest()
    # root = speedtest.Speedtest()
    root.get_servers()
    down= str(round(root.download()/(10**6),2))+" Mbps "
    up= str(round(root.upload()/(10**6),2))+" Mbps "
    lab_down.config(text=down)
    lab_up.config(text=up)

root = Tk()
root.geometry("600x200")
root.title("******Speed Test********")
root.config(bg="#36454f")

lab = Label(root,text="T-Y-P-I-N-G---S-P-E-E-D---T-E-S-T",font=("Time New Roman", 24, "bold"))
lab.place(x=50,y=30)

lab = Label(root,text="DOWNLOAD ",font=("Time New Roman", 12, "bold"),fg="White",bg="#36454f")
lab.place(x=50,y=80)

lab_down = Label(root,text="00",font=("Time New Roman", 12, "bold"),fg="White",bg="#36454f")
lab_down.place(x=200,y=80)

lab = Label(root,text="UPLOAD ",font=("Time New Roman", 12, "bold"),fg="White",bg="#36454f")
lab.place(x=340,y=80)

lab_up = Label(root,text="00",font=("Time New Roman", 12, "bold"),fg="White",bg="#36454f")
lab_up.place(x=450,y=80)

button= Button(root,text=" CHECK  SPEED ",font=("Time New Roman", 12, "bold"),fg="White",bg="#551a8b",relief=RAISED,command=speedcheck)
button.place(x=60,y=120, height=50,width=160)



root.mainloop()