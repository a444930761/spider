# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:42:55 2017

@author: liwei

E-mail:444liwei@163.com

"""
from pymongo import MongoClient
import random

class DoubanProxy(object):
    def __init__(self):
        self.f = open(r'D:/Anaconda/test/proxy.txt','r')
        self.proxy = random.choice(self.f.readlines())
        self.f.close()
        
    def process_request(self,request,spider):
        proxy = self.proxy.strip()
        print(proxy)
        request.meta['proxy'] = proxy

