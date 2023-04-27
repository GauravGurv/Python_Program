import os
from datetime import datetime
import pandas as pd
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

my_details('D:\STUDY\DS\\')