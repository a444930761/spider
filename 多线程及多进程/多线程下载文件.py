# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 14:53:34 2017

@author: Administrator
"""
#import sqlite3
#conn = sqlite3.connect('test2.db')
#c = conn.cursor()
#selsql = "select name from sqlite_master where type='table'"
#inssql = "insert into job values(?,?,?,?,?,?,?,?)"
#value = (1,2,3,4,5,6,7,8)
#c.execute(inssql,value)
#c.execute(selsql)
#c.fetchall()

import requests
import threading
import time
class down():
    def __init__(self):
        self.url = 'https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-5.0.1-Windows-x86_64.exe'
        self.name = self.url.split('/')[-1]
        self.num = 8 #将文件分成几段
        r = requests.head(self.url)
        self.total = int(r.headers['Content-Length']) #获取文件大小
    def offset(self):
        offset = int(self.total / self.num)
        offsetlist = []
        for i in range(self.num):
            if i == self.num - 1:
                offsetlist.append((i*offset,''))
            else:
                offsetlist.append((i*offset,(i+1)*offset)) #设置每段字节区间
        return offsetlist
    
    def download(self,start,end):
        headers = {'Range':'Bytes=%s-%s'%(start,end)} #利用range获取下载区间
        req = requests.get(self.url,headers=headers)
        print('%s:%s download success'%(start,end))
        self.f.seek(start) #移动游标到区间的开始位置
        self.f.write(req.content)
        
    def save(self):
        thread_list = []
        n = 0
        with open(self.name,'wb') as self.f:
            for i in self.offset():
                start,end = i
                print('thread %d start:%s,end:%s'%(n,start,end))
                n += 1
                thread = threading.Thread(target=self.download,args=(start,end))
                thread.start()
                thread_list.append(thread)
            for i in thread_list:
                i.join()
            print('download %s load success'%(self.name))

if __name__=='__main__':
    print(time.ctime())
    down = down()
    down.save()
    print(time.ctime())
