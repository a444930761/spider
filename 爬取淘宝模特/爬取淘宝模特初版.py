# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 19:19:37 2017

@author: Administrator
"""
import requests
from lxml import etree
import os
import re,time
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
'''
        name = data['userId']
        
        os.mkdir('D:/MM/{}'.format(name)) #以模特ID创建目录
        path = 'D:/MM/{}/{}.txt'.format(name,name)#保存模特的个人信息
        with open(path,'w+') as f:
            f.writelines('昵称:{}\nID:{}\n城市:{}\n身高:{}\n体重:{}\n点赞数:{}'.format(
                    data['realName'],data['userId'],data['city'],data['height'],
                    data['weight'],data['totalFavorNum'])) 
            
        userID.append(data['userId']) #将模特ID加入列表
'''        
def down_photo(userid,html):
    for i in html['picList']:
        url = 'http:' + i['picUrl']
 #       html = requests.get(url,headers=header).content
        mmphoto.insert_one({'id':userid,'photourl':url})
#        name = url.split('/')[-1]
#        path = 'D:/MM/{}/{}'.format(userid,name)
#        with open(path,'wb+') as f:
#            html = requests.get(url,headers=header).content
#            f.write(html)        
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
    now = lambda : time.time()
    start = now()
    print(time.ctime())
#    for i in range(1,167): #获取所有模特的ID等个人信息
#        get_user(url.format(i)) 
        
    while True:
        userid = mmuser.find_one_and_update({'state':0},{'$set':{'state':1}})['_id']
        if userid:
            print('开始下载{}'.format(userid))
            get_album(int(userid))
            print('{}下载完成'.format(userid))
        else:
            break
#    for userid in userID: #获取所有模特的相册
#        print('开始下载{}'.format(userid))
#        get_album(userid)
#        print('{}下载完成'.format(userid))
    print(time.ctime())
    print(now()-start)

if __name__ =='__main__':
    
    url = 'https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8?q=&currentPage={}'
    #所有模特列表页url
    url1 = 'https://mm.taobao.com/self/album/open_album_list.htm?_charset=utf-8&user_id%20={}'
    #模特相册列表页url
    url2 = 'https://mm.taobao.com/album/json/get_album_photo_list.htm?user_id={}&album_id={}'
    client = MongoClient(host='localhost',port=27017,username='liwei',password='it088078')
    mmuser = client.cache.mmuser
    mmphoto = client.cache.mmphoto
    
    userID = [186173830,176817195,362438816]
    main()
    


