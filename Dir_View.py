from tkinter import *
from datetime import datetime
import pandas as pd
import os
df=pd.DataFrame(columns=['Name','Type','Date Modified','Size'])
def my_details(path):
    global df
    df.drop(df.index,inplace=True)
    files=os.listdir(path)
    for f in files:
        f_path=path+'\\'+f                          # path with file name
        t_stamp=os.path.getmtime(f_path)
        # t_stamp=os.path.getmtime(f_path)
        f_name,f_extension=os.path.splitext(f_path)
        size=os.path.getsize(f_path)
        dt_mod=datetime.fromtimestamp(t_stamp)
        m_date=datetime.strftime(dt_mod, "%Y-%m-%d")
        # print(f,f_extension,m_date,size)
        df_new=[f,f_extension,m_date,size]
        df.loc[len(df)]=df_new
    print(df.head())


root = Tk()
root.geometry("550x350")
root.title("Directory Views")
root.config(bg="Powder Blue")
lab_txt=Label(root,text="Dir..",bg="Powder Blue", font=("Arial Black",14,"bold"))
lab_txt.place(x=10,y=10,height=30,width=70)
box_txt=Text(root,bg="white",font=("Time New Roman",14,'bold'),wrap=WORD)
box_txt.place(x=85,y=10,height=30,width=300)
button=Button(root,text="Check Path",font=("Arial Black",12,"bold"), bg="blue",fg="white",relief=RAISED, command=my_details('D:\STUDY\DS\\'))
button.place(x=390,y=10,height=30,width=120)
lab_down_txt=Label(root,text="",bg="lime", font=("Arial Black",14,"bold"))
lab_down_txt.place(x=30,y=50,height=270,width=480)






root.mainloop()