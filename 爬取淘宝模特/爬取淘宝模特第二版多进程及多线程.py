# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 17:07:00 2017

@author: liwei

E-mail:444liwei@163.com

"""
import requests
from lxml import etree
from threading import Thread
from multiprocessing import Process
import re,time,os
from pymongo import MongoClient

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.8'}

def get_user(url):
    html = requests.get(url,headers=header).json()
    datalist = html['data']['searchDOList']
    
    for data in datalist:
        mmuser.insert_one({'_id':str(data['userId']),'name':data['realName'],
                       'city':data['city'],'height':data['height'],
                       'weight':data['weight'],'totalFavorNum':data['totalFavorNum'],
                       'state':0})
       
def down_photo(userid,html):
    for i in html['picList']:
        url = 'http:' + i['picUrl']
        mmphoto.insert_one({'id':userid,'photourl':url})
    
#        
def get_photourl(userid,url):
    album_id = re.findall('album_id=(\d*?)&album_flag',url)[0]
    url = url2.format(userid,album_id)
    html = requests.get(url,headers=header).json()
    down_photo(userid,html)
    page = 2
    while True:
        if page <= int(html['totalPage']):
            url = url + '&page={}'.format(page)
            html = requests.get(url,headers=header).json()
            down_photo(userid,html)
            page += 1 
        else:
            break
                  
        
def get_album(userid):
    url = url1.format(userid)
    html = etree.HTML(requests.get(url,headers=header).text)
    hreflist = html.xpath('//h4/a/@href') #获取模特的相册
    for href in hreflist:
        get_photourl(userid,href)


def main():
#    for i in range(1,167): #获取所有模特的ID等个人信息
#        get_user(url.format(i)) 
        
    while True:
        userid = mmuser.find_one_and_update({'state':0},{'$set':{'state':1}})['_id']
        if userid:
            print('开始下载{}'.format(userid),'进程id是:',os.getpid())
            get_album(int(userid))
            print('{}下载完成'.format(userid))
        else:
            break
    
    
    
#def main2(i):
#    print('开始线程',i,'主线程id是',os.getpid())

def thread_list():
    threadlist = []
    for i in range(10):
        t = Thread(target=main)
        t.start()
 #       print('开始线程',i,'进程id是:',os.getpid())
    for t in threadlist:
        t.join()


if __name__ =='__main__':
    
    now = lambda : time.time()
    start = now()
    url = 'https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8?q=&currentPage={}'
    #所有模特列表页url
    url1 = 'https://mm.taobao.com/self/album/open_album_list.htm?_charset=utf-8&user_id%20={}'
    #模特相册列表页url
    url2 = 'https://mm.taobao.com/album/json/get_album_photo_list.htm?user_id={}&album_id={}'
    client = MongoClient(host='localhost',port=27017,username='liwei',password='it088078')
    mmuser = client.cache.mmuser
    mmphoto = client.cache.mmphoto
    
    print(time.ctime())
#    pool = []
#    for i in range(2):
#        p = Process(target=thread_list,)
#        p.start()
#        pool.append(p)
#    for p in pool:
#        p.join()
        
    thread_list()
    print(time.ctime())
    print(now()-start)
    



