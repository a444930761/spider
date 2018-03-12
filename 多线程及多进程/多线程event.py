'''
http://www.cnblogs.com/alex3714/articles/5230609.html

写一个汽车等红绿灯的程序
'''
import threading
import time

event = threading.Event()
'''
event.set() 设置标志位
event.clear() 清除标志位
event处于未设置标志位状态时，event会处于wait状态，等待被设定
因此可设定event.clear()时是红灯，enent.set()时，绿灯
'''

def lighter():
    count = 0
    event.set() #设置标志位
    while True:
        if  5 < count < 10:
            event.clear() #设置为红灯
            print('红灯')
        elif count > 10:
            event.set() #设置为绿灯
            count = 0
        else:
            print('绿灯')
        time.sleep(1)
        count += 1

def car(name):
    while True:
        if event.isSet():#代表绿灯
            print('%s is running...' % name)
            time.sleep(1)
        else:
            print('linght is red')
            event.wait()
            
t1 = threading.Thread(target=lighter)
t2 = threading.Thread(target=car,args=('car',))
t1.start()
t2.start()




