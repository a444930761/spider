# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 10:02:09 2017

@author: Administrator

http://www.cnblogs.com/alex3714/articles/5230609.html
"""

import threading
import time

def run():
    global num
#    lock.acquire()#加锁
    num += 1 
#    lock.release()#释放
    print(num)
    
#gil lock 全程解释器锁，该锁限定同一时间只能有一个线程在运行
#threading.Lock 用户态锁（互斥锁），该锁限定同一时间只能有一个线程读写数据
#threading.RLock 递归锁，锁里面还要嵌套锁的情况下，要用Rlock
#threading.BoundedSemaphore(5) 信号量，同时有5把锁，可同时允许5个线程读写数据
#lock = threading.Lock() 
num = 0
threadlist = []    
for i in range(10):    
#t1 = threading.Thread(target=run,args=('t1',))
    t = threading.Thread(target=run,args=())
#t1.start()
#    t.setDaemon(True)#定义子线程为守护线程，主线程执行完，不用等子线程结束
    #要在start之前设置，与下面的join作用相反
    t.start()#启动线程   
    threadlist.append(t)

#while threading.active_count() != 1:
#当前活动线程数，该命令效果同下面的for join
    
for t in threadlist:
    t.join()  #等待所有的线程执行完，再往下执行.
    #join不写到上面的for循环里，是为了先开始所有线程，再等待，否则就是串行了
print('all done',num)
#run('t1')
#run('t2')
