# -*- coding: utf-8 -*-
import requests
from pymongo import MongoClient
import time

client = MongoClient(host='localhost',port=27017,username='liwei',password='it088078')
pinduoduo = client.cache.pinduoduo
goodslist = client.cache.goodslist

indexurl = 'http://apiv4.yangkeduo.com/home_operations' #主分类
baseurl = 'http://apiv4.yangkeduo.com/operation/{}/groups?size=1000' #商品列表
scoreurl = 'http://apiv4.yangkeduo.com/reviews/{}/info'

def get_title(url):
    title = requests.get(indexurl).json()
    
    for each in title:
        mainname = each['opt_name']
        mainnameid = each['opt_id']
        for i in each['children']:
            name = i['opt_name']
            nameid = i['opt_id']
            pinduoduo.insert_one({'父目录':mainname,'父ID':mainnameid,
                                  '子目录':name,'子ID':nameid,
                                  '子链接':baseurl.format(nameid),
                                  'status':0})

def get_info(url):
    response = requests.get(url).json()
    
    for each in response['goods_list']:
        goods_id = each['goods_id']
        goods_name = each['goods_name']
        group_price = int(each['group']['price']) / 100
        normal_price = int(each['normal_price']) / 100
        cnt = each['cnt']
        goodslist.insert_one({'ID':goods_id,'名称':goods_name,
                              '团购价':group_price,'标准价':normal_price,
                              '销量':cnt,'评价链接':scoreurl.format(goods_id),
                              'status':0})

def get_scores(url):
    response = requests.get(url).json()
    
    score_num = response['score_num']
    append = response['append']
    picture = response['picture']
    goodslist.update_one({'评价链接':url},{'$set':{'总分':score_num,
                          '追加评价数':append,'带图评价数':picture,}})
    for each in response['labels']:
        goodslist.update_one({'评价链接':url},
                             {'$set':{each['name']:each['num']}})


def main(url):
    get_title(url)
    
    while True:
        goods = pinduoduo.find_one_and_update({'status':0},{'$set':{'status':1}})
        if goods:
            get_info(goods['子链接'])
        else:
            break
    while True:
        scores = goodslist.find_one_and_update({'status':0},{'$set':{'status':1}})
        if scores:
            get_scores(scores['评价链接'])
        else:
            break

if __name__=='__main__':
    now = time.ctime()
    print(now)
    main(indexurl)
    print(time.time()-now)
        

        
        

    
