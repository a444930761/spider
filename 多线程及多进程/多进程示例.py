# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 14:13:23 2017

@author: liwei

E-mail:444liwei@163.com

"""
from  multiprocessing import Process,Pool
import time
 
def Foo(i):
    time.sleep(3)
    print('*'*20)
    return i+100
 
def Bar(arg):
    print('-->exec done:',arg)

def main():
    pool = Pool(100)
    result = [] 
    for i in range(1000):
        result.append(pool.apply_async(func=Foo, args=(i,),callback=Bar))
        #pool.apply(func=Foo, args=(i,))
     
#    print('end')
    pool.close()
    pool.join()
if __name__=='__main__':
    main()