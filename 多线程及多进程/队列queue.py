'''
http://www.cnblogs.com/alex3714/articles/5230609.html
生产者消费者模型
'''
# -*- coding: utf-8 -*-
import queue
import threading,time
'''
q = queue.Queue(maxsize=10) #定义队列对象，，默认先进先出,设置大小为10，默认不设置
q = queue.LifoQueue() #后进先出
q.put('a') #往队列里面放数据
q.get() #从数据里面取数据
#当队列为空时，直接执行q.get()会卡住，一直等待
q.get_nowait()#为空时不等待，直接抛出异常
q = queue.PriorityQueue() #存储时可设置优先级队列
q.put((1,'a')) # 1为优先级，数字越小，优先级越大
q.qsize()#查看队列大小
if q.qsize():
    q.get()
'''
q = queue.Queue(maxsize=10)

def producer():
    count = 1
    while True:
        q.put('骨头')
        print('生产骨头',count)
        count += 1
        time.sleep(0.5)
        
def consumer(name):
    while True:
        if q.qsize() > 0:
            print(name,'eating 骨头',q.get())
            time.sleep(1)
            
t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer,args=('张三',))

t1.start()
t2.start()
