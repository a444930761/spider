# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 17:47:17 2017

@author: liwei

E-mail:444liwei@163.com

"""
import requests
from lxml import etree
from pymongo import MongoClient
import telnetlib

class Proxy_ip():
    def __init__(self):
        self.iplist = []
        self.f = open('proxy.txt','w+')
#        self.client = MongoClient(host = 'localhost',
#                             port = 27017,
#                             username = 'liwei',
#                             password = 'it088078')
#        self.proxyip = self.client.cache.proxyip
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36','Accept-Language': 'zh-CN,zh;q=0.8'}
        self.getip()
    
    def getip(self):
        #从西刺代理获取IP
        url = 'http://www.xicidaili.com/nn/'  
        response = requests.get(url,headers=self.header).text
        html = etree.HTML(response)
        for i in html.xpath('//tr[@class="" or @class="odd"]'):
            ip = i.xpath('./td[2]/text()')[0]
            port = i.xpath('./td[3]/text()')[0]
            iptype = i.xpath('./td[6]/text()')[0]
            
            self.checkip(ip,port,iptype)#检验IP的可用性
        self.f.writelines(self.iplist)
        self.f.close()
            
    def checkip(self,ip,port,iptype):
        try:
            telnetlib.Telnet(ip,port,timeout=1)#通过telnet方法验证，超时时间视需求设定
        except:
            print('{}验证失败'.format(ip))
        else:
            print('{}验证成功'.format(ip))
            a = iptype+'://'+ip + ':' + port+'\n'
            self.iplist.append(a)
#            self.proxyip.update_one({'_id':ip},{'$set':{'port':port}},upsert=True)
            #通过验证的IP保存到数据库中
if __name__=='__main__':
    Proxy_ip()
    