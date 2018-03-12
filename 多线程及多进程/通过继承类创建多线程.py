# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 10:07:18 2017

@author: Administrator
"""
import threading
import time

class MyThread(threading.Thread):
    def __init__(self,n):
        super(MyThread,self).__init__()#因为把父类的默认函数重构，因此要继承一下
        self.n = n
        
    def run(self):
        print('runnint task',self.n)
threadlist = []        
for i in range(10):   
    t = MyThread(i)
    t.start()
    threadlist.append(t)

for i in threadlist:
    i.join()        
