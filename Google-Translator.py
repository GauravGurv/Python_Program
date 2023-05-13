from tkinter import *
from tkinter import ttk
# from tkinter import tk
from googletrans import Translator,LANGUAGES

# --------------------------------------Google Translator--------------------------------------------
def change(text="type",src="English",dest="Hindi"):                     #calling funtion
    text1=text
    src1=src
    dest1=dest
    trans= Translator()
    result=trans.translate(text = text1 ,src=src1,dest=dest1)
    # trans1=trans.translate(text,src=src1,dest=dest1)
    return result

def data():
    s=comb_sor.get()
    d=comb_dest.get()
    masg= Sor_txt.get(1.0, END)
    textget = change(text = masg, src=s, dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)



# --------------------------------------Making Window--------------------------------------------
root = Tk()
root.title("--->Google Translator<---")             #put title on window
root.geometry("500x450")                            #set dimension of window
root.config(bg="powder blue")                       #window color change

# --------------------------------------Making Label (Google Translator)--------------------------------------------
lab_txt=Label(root,text="Google Translator",font=("Time New Roman",20,'bold'))              #making label of text
lab_txt.place(x=100,y=10,height=50,width=350)                                               #set label box height width and position in window

frame=Frame(root).pack(side=BOTTOM)                                                         #make a frame for textbox and button
# ------------------------------Source Text---------------------------
lab_txt=Label(root,text="Source Text",font=("Time New Roman",20,'bold'),fg="blue",bg="powder blue")
lab_txt.place(x=150,y=60,height=50,width=200)
Sor_txt = Text(frame,font=("Time New Roman",40,'bold'),wrap=WORD)                              #make text box
Sor_txt.place(x=10,y=110,height=80,width=480)

# list_text= ['English','Hindi','French','Spanish','Bengoli','Kannad']
list_text= list(LANGUAGES.values())                                 #importing all languages via googletrans module
#Make Combo Box
comb_sor= ttk.Combobox(frame,values=list_text)                      # Make Combo Box
comb_sor.place(x=10,y=80,height=25,width=100)                     # Set dimension
comb_sor.set("english")                                            # Set default value of Combo Box



# ------------------------------Output---------------------------
lab_txt=Label(root,text="Output",font=("Time New Roman",20,'bold'),fg="blue",bg="powder blue")
lab_txt.place(x=150,y=190,height=50,width=200)
dest_txt = Text(frame,font=("Time New Roman",40,'bold'),wrap=WORD)                              #make text box
dest_txt.place(x=10,y=240,height=80,width=480)

comb_dest= ttk.Combobox(frame,values=list_text)                      # Make Combo Box
comb_dest.place(x=10,y=210,height=25,width=100)                     # Set dimension
comb_dest.set("english")                                            # Set default value of Combo Box

# ------------------------------Button---------------------------
button_change = Button(frame, text="Translate", relief=RAISED, command=data)
button_change.place(x=110,y=330,height=100,width=300)                     # Set dimension

root.mainloop()