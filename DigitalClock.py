from tkinter import *
from tkinter import ttk
import datetime

def date_time():
    time =datetime.datetime.now()
    hr = time.strftime("%I")
    mi = time.strftime("%M")
    sec = time.strftime("%S")
    am = time.strftime("%p")
    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    lab_hr.after(200,date_time)

    date = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%y")
    day = time.strftime("%a")
    lab_date.config(text=date)
    lab_month.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)
    lab_hr.after(200, date_time)


clock = Tk()
clock.title('----->> Digital Clock <<----')
clock.geometry('600x500')
clock.config(bg='Powder blue')

lab_hr=Label(clock,text='00',font=('Arial Black', 40,'bold'),bg='white')
lab_hr.place(x=40,y=40,height=110,width=100)
lab_min=Label(clock,text='00',font=('Arial Black', 40,'bold'),bg='white')
lab_min.place(x=180,y=40,height=110,width=100)
lab_sec=Label(clock,text='00',font=('Arial Black', 40,'bold'),bg='white')
lab_sec.place(x=320,y=40,height=110,width=100)
lab_am=Label(clock,text='00',font=('Arial Black', 40,'bold'),bg='white')
lab_am.place(x=460,y=40,height=110,width=100)

lab_h=Label(clock,text='Hour',font=('Arial Black', 20,'bold'),fg='blue',bg='white')
lab_h.place(x=40,y=180,height=40,width=100)
lab_m=Label(clock,text='Minute',font=('Arial Black', 20,'bold'),fg='blue',bg='white')
lab_m.place(x=180,y=180,height=40,width=100)
lab_s=Label(clock,text='Sec',font=('Arial Black', 20,'bold'),fg='blue',bg='white')
lab_s.place(x=320,y=180,height=40,width=100)
lab_AP=Label(clock,text='AM/PM',font=('Arial Black', 20,'bold'),fg='blue',bg='white')
lab_AP.place(x=460,y=180,height=40,width=100)

lab_date=Label(clock,text='00',font=('Arial Black', 40,'bold'),bg='white')
lab_date.place(x=40,y=280,height=110,width=100)
lab_month=Label(clock,text='00',font=('Arial Black', 40,'bold'),bg='white')
lab_month.place(x=180,y=280,height=110,width=100)
lab_year=Label(clock,text='00',font=('Arial Black', 40,'bold'),bg='white')
lab_year.place(x=320,y=280,height=110,width=100)
lab_day=Label(clock,text='00',font=('Arial Black', 40,'bold'),bg='white')
lab_day.place(x=460,y=280,height=110,width=100)

lab_da=Label(clock,text='Date',font=('Arial Black', 20,'bold'),fg='blue',bg='white')
lab_da.place(x=40,y=420,height=40,width=100)
lab_mo=Label(clock,text='Month',font=('Arial Black', 20,'bold'),fg='blue',bg='white')
lab_mo.place(x=180,y=420,height=40,width=100)
lab_ye=Label(clock,text='Year',font=('Arial Black', 20,'bold'),fg='blue',bg='white')
lab_ye.place(x=320,y=420,height=40,width=100)
lab_d=Label(clock,text='Day',font=('Arial Black', 20,'bold'),fg='blue',bg='white')
lab_d.place(x=460,y=420,height=40,width=100)



date_time()

clock.mainloop()    #Display and hold Window