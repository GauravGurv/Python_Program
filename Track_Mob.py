'''
import phonenumbers                 #calling phonenymbers module
from phonenumbers import timezone,geocoder,carrier
#(timezone: Dipslay the timzone of area mobile), (geocoder: is used to get information about sim)  ,(carrier: give you details of SIM)
num=input("Enter your Phone No. :+__ ")
phone=phonenumbers.parse(num)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en")
print(phone)
print(time)
print(car)
print(reg)
'''
import tkinter as tk
from tkinter import*
import phonenumbers                 #calling phonenymbers module
from phonenumbers import timezone,geocoder,carrier
#(timezone: Dipslay the timzone of area mobile), (geocoder: is used to get information about sim)  ,(carrier: give you details of SIM)

def call():
    # num=input("Enter your Phone No. :+__ ")
    # num="+918789527540"
    num=Mob_txt.get(1.0, END)
    # num= Mob_txt.config(text=num1)
    phone=phonenumbers.parse(num)
    time=timezone.time_zones_for_number(phone)
    car=carrier.name_for_number(phone,"en")
    reg=geocoder.description_for_number(phone,"en")
    Result_txt.set(text=phone)
    print(phone)
    print(time)
    print(car)
    print(reg)
    Result_txt = Mob_txt.insert(tk.END, phone, time, car, reg, get(1.0, END))




screen=Tk()                                                                             #calling window
screen.title("-----------------<<< Mobile Tracking >>>-----------------",)                          #Displaying Title
screen.geometry("500x280")                                                              #Set Window Screen Resolutioin
screen.config(bg="powder blue")                       #window color change

frame=Frame(screen).pack(side=TOP)
lab_txt=Label(screen,bg="powder blue",fg='blue',text="NUMBER INFORMATION",font=('Arial Black',20,'bold'))           #label the text
lab_txt.place(x=10,y=20,height=50,width=480)

lab_txt=Label(screen,bg="powder blue",text="Enter Moblie Number with (+91):",font=('Times New roman',8,'bold'))           #label the heading text
lab_txt.place(x=10,y=70,height=40,width=200)
Mob_txt = Text(frame,font=("Time New Roman",12,'bold'),wrap=WORD)                              #make text box for input mobile number
Mob_txt.place(x=200,y=70,height=40,width=150)
Show_button = Button(frame,text="SEARCH",relief=RAISED,font=('Arial Black',14,'bold'),fg="blue",command=call)
Show_button.place(x=360,y=70,height=40,width=120)                     # Set dimension

Result_txt = Text(frame,font=("Time New Roman",12,'bold'),wrap=WORD)                              #make text box for input mobile number
Result_txt.place(x=10,y=120,height=150,width=480)



screen.mainloop()