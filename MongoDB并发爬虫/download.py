# -*- coding: utf-8 -*-
from datetime import datetime,timedelta
from pymongo import MongoClient
import pickle
import zlib
import requests
import time



class Download():
    def __init__(self,dealy=3,num=2,expires=timedelta(seconds=900)):#倒计时设置为7天
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36','Accept-Language': 'zh-CN,zh;q=0.8'}
        self.dealy = dealy #重新下载等待时间
        self.num = num #重新下载次数
        self.expires = expires
        client = MongoClient(host='localhost',port=27017,username='liwei',password='it088078')
        self.webpage = client.cache.webpage
        self.webpage.create_index('time',expireAfterSeconds=expires.total_seconds())
        #创建时间索引，并设置过期时间（过期后自动删除数据）
    def ceshi(self):
        print('ceshi')
    def Downloader(self,url):
        html = ''
        web = self.webpage.find_one({"_id":url})
        if web and web['code']==200:
            print('缓存已存在')
            html = web['html']
            html = pickle.loads(zlib.decompress(html))
        else:
            print('缓存不存在，开始下载')
            try:
                reponse = requests.get(url,headers=self.header)
#                print(reponse.status_code)
                reponse.raise_for_status()#如果状态码是非2或3开头，则抛出异常
                html = reponse.text
                print(reponse.status_code,url+'下载成功')
                html = zlib.compress(pickle.dumps(html))
                self.webpage.insert_one({"_id":url,"code":reponse.status_code,
                                   "html":html,"time":datetime.utcnow()})
#                html = etree.HTML(req)
            except requests.HTTPError as e:
                print(reponse.status_code,url+'下载失败')
                self.webpage.insert_one({"_id":url,"code":reponse.status_code,
                                   "html":html,"time":datetime.utcnow()})
#                if 500 <= reponse.status_code < 600:#如果状态码以5开头，则重新爬取
#                    if self.num:
#                        time.sleep(self.dealy)#设置等待时间
#                        self.num -= 1
#                        self.Download(url)
#            self.cache.update_one({"_id":url},{'$set':{"code":reponse.status_code,
#                                   "html":req,"time":datetime.utcnow()}},upsert=True)
#            print(len(html))
#            print(len(zlib.compress(pickle.dumps(html))))

            #因为设置了过期自动删除，因此时间要采用世界时间，即UTC时间
        return html
    

