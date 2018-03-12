# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 16:23:55 2017

@author: liwei

E-mail:444liwei@163.com

"""
import pandas as pd
import os 
import glob

path = 'D:/Anaconda/test/m5/'
os.chdir(path)

c = pd.DataFrame()

for file in glob.glob('*.TXT'):#查找类似于*.txt的文件
    filename,fileExtension = os.path.splitext(file)#将文件名和后缀分离
    columnss = pd.MultiIndex.from_arrays([[filename]*6,['open','high','close','low','volume','amount']]) #建立一个层级索引
    filepath = path+file
    a = pd.read_table(filepath,sep=' ',index_col=[0],parse_dates=[[0,1]])
    a.columns = columnss
    b = a.stack().T
    c = pd.concat([c,b])
print(c)
print(c.info())
    
    
    