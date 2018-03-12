# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 09:47:44 2017

@author: Administrator
"""
import requests
from lxml import etree
import json
import pandas as pd
import numpy as np
from pandas import DataFrame,Series
from datetime import datetime
import sqlite3

conn = sqlite3.connect('test2.db')
c = conn.cursor()
#c.execute('''create table job3
#          (title text,
#          link char(50),
#          category text,
#          num int,
#          city text,
#          time time,
#          jobduties text,
#          jobrequirement text
#          );''')
#conn.commit()

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.8'}
baseurl = 'http://hr.tencent.com/'
offset = 'position.php?&start=0#a'
joblist = []

def loadurl(url):  
    req = requests.get(url,headers=header)
    body = req.text
    html = etree.HTML(body)
    return html


def findlist(url,meta):
    html = loadurl(url)
#    item = {}
#   
#    item['title']=meta['title']
#    item['link']=meta['link']
#    item['category']=meta['category']
#    item['num']=meta['num']
#    item['city']=meta['city']
#    item['time']=meta['time']
#    item['jobduties'] = html.xpath('//tr[@class="c"][1]/td[@colspan="3"]/ul')[0].xpath('string(.)')
#    item['jobrequirement'] = html.xpath('//tr[@class="c"][2]/td[@colspan="3"]/ul')[0].xpath('string(.)')
    item = []
    jobduties = html.xpath('//tr[@class="c"][1]/td[@colspan="3"]/ul')[0].xpath('string(.)')
    jobrequirement = html.xpath('//tr[@class="c"][2]/td[@colspan="3"]/ul')[0].xpath('string(.)')

#    item.append([meta['title'],meta['link'],meta['category'],meta['num'],
#                 meta['city'],meta['time'],jobduties,jobrequirement])
    item.append([jobduties,jobrequirement])
    yield item[0]

def find(baseurl,offset):
    url = baseurl + offset
    html = loadurl(url)
    result1 = html.xpath('//tr[@class="even" or @class="odd"]')
    item = {}
    for i in result1:
        title = i.xpath('./td[1]/a/text()')[0]
        link = baseurl + i.xpath('./td[1]/a/@href')[0]
        if len(i.xpath('./td[2]/text()')) == 0:
            category = ''
        else:
            category = i.xpath('./td[2]/text()')[0]
        num = i.xpath('./td[3]/text()')[0]
        city = i.xpath('./td[4]/text()')[0]
        time = i.xpath('./td[5]/text()')[0]
            
   
        item['title']=title
        item['link']=link
        item['category']=category
        item['num']=num
        item['city']=city
        item['time']=time
        
        for a in findlist(link,meta={'title':title,'category':category,'num':num,
                                  'city':city,'time':time,'link':link}):
            print(a[0])
            print('_'*64)
            print(a[1])
            print('*'*64)
            item['jobduties'] = a[0]
            item['jobrequirement'] = a[1]
            yield item
    
    
      
#    if len(html.xpath('//*[@id="next"]/@class')) == 0:
#        offset = html.xpath('//*[@id="next"]/@href')[0]
#        for i in find(baseurl,offset):
#            yield i

if __name__ =='__main__':
#    print(datetime.now())
#    for item in find(baseurl,offset):
#        insertsql = "insert into job3 values(?,?,?,?,?,?,?,?)"
#        c.execute(insertsql,(item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7]))
#        conn.commit()
#    print(datetime.now())
#    sql = 'select * from job3'
#    df = pd.read_sql(sql,conn)


    with open('joblist.txt','w+',encoding='utf-8') as f:
        print(datetime.now())
        for item in find(baseurl,offset):
            #print(item)
            #b = ' '.join(item[0])
            b = json.dumps(item,ensure_ascii=False)
            f.write(b+'\n')
        print(datetime.now())


#    ceshi = DataFrame({"title":[],"link": [],"category": [],"num": [],"city":[],
#                       "time": [],"jobduties": [],"jobrequirement":[]})
#    print(datetime.now())
#    for item in find(baseurl,offset):
#        frame = DataFrame.from_dict(item,orient='index').T
#        #ceshi = pd.concat([ceshi,frame],ignore_index=True)
#        ceshi = ceshi.append(frame,ignore_index=True)
#        ceshi.to_csv('job.csv')
#    print(datetime.now())
