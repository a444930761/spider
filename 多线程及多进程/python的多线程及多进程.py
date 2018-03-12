# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 10:19:39 2017

@author: Administrator

http://www.cnblogs.com/alex3714/articles/5230609.html
"""
#import threading
#import time,os
#from multiprocessing import Pool,Process

##def print_time(threadName,delay):
##    count = 0
##    while count < 3 :
##        time.sleep(delay)
##        count += 1 
##        print('%s:%s'%(threadName,time.ctime(time.time())))
##        
##try:
##    thread = threading.Thread(target=print_time,args=(1,2))
##    thread1 = threading.Thread(target=print_time,args=(2,3))
##    thread.start()
##    thread1.start()
##    thread.join()
##    thread1.join()
###    print(threading.enumerate())
###    _thread.start_new_thread(print_time,(3,2))
###    _thread.start_new_thread(print_time,(4,2))
##except:
##    print('创建线程失败')
#
#class myThread(threading.Thread):
#    def __init__(self,threadID,threadName,count):
#        threading.Thread.__init__(self)
#        self.id = threadID
#        self.name = threadName
#        self.count = count
#        
#    def run(self):
#        global lock
#        print('开始线程：'+ self.name)
##        lock.acquire()
#        print_time(self.name,self.count,5)
#        print('退出线程:'+ self.name)
##        lock.release()
#def print_time(threadName,delay,count):
#    while count:
#        time.sleep(delay)
#        print('%s: %s'%(threadName,time.ctime(time.time())))
#        count -= 1
#
##lock = threading.Lock()        
#thread1 = myThread(1,'Thread-1',2)
#thread2 = myThread(2,'Thread-2',3)
#
#thread1.start()
#thread2.start()
#thread1.join()
#thread2.join()
#print('退出主程序')
#
##非下载模式下，不建议使用多线程，尤其是对同一数据源进行操作的时候（涉及到线程锁）
#多线程，不适合cpu密集操作型的任务，适合IO操作密集型的任务
#cpu密集，如计算等使用cpu的
#IO密集，如打开文件、操作数据库之类的
#
#多进程，
#进程锁的主要目的是为了防止输出时错乱

#进程和线程的区别：
#1、线程共享内存空间（共享数据），进程的内存是独立的（数据独立的）
#2、同一个进程的线程之间可以直接进行通信，进程之间进行通信必须通过一个中间代理
#3、线程可直接创建，创建进程是克隆父进程
#4、线程之间可进行直接操作，进程只能操作子进程

'''def run(i):
    print(i,os.getpid())
    
def run2(i):
    print('这是回调输出',i,os.getpid())

if __name__ == "__main__":
#    p = Pool(2)
    print('主进程',os.getpid())
#    for i in range(2):
#        p.apply_async(func=run,args=(i,),callback=run2)#apply_async是异步
##        callback属于回调，子进程执行完以后，主进程会进行回调
##        p.apply(func=run,args=(i,))#applys是串行   
#    p.close()
#    p.join()
    p = Process(target = run,args=(1,))
    p.start()
    p.join()
'''
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    a = input('请输入：')
    print(a)
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')



