# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 11:39:11 2017

@author: liwei

E-mail:444liwei@163.com

"""
#import ssl
import requests
from citymap import city

#ssl._create_default_https_context = ssl._create_unverified_context
#设置不对证书进行校验 

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36','Accept-Language': 'zh-CN,zh;q=0.8'}


def get_track(url):
    response = requests.get(url,headers=header,verify=False).json()
    result = response['data']['result']

    for i in result:
        a = i.strip().split('|')
            #车次 3；发车时间 8；到达时间 9；总耗时 10；软卧 23；无座 26；硬卧 28；硬座 29
            # 二等座 30 ；一等座 31；商务特等座 32
        if a[29] =='有' or int(a[29]) > 0:
            
            
'''
        if a[3][0] in 'DG':
            print("车次:{};发车时间:{};到达时间:{};二等座:{};一等座:{};商务特等座:{};无座:{}".format(a[3],a[8],a[9],a[30],a[31],a[32],a[26]))
        else:
            print("车次:{};发车时间:{};到达时间:{};硬卧:{};软卧:{};硬座:{};无座:{}".format(a[3],a[8],a[9],a[28],a[23],a[29],a[26]))
'''
    
url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-{}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'


citymap = city()
from_station = input('请输入始发地：')
from_station = citymap.find_citymap(from_station)
to_station = input('请输入目的地：')
to_station = citymap.find_citymap(to_station)
time = input('请输入乘车时间(eg:10-01)：')

get_track(url.format(time,from_station,to_station))


