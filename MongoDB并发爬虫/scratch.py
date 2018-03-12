# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 11:39:11 2017

@author: liwei

E-mail:444liwei@163.com

"""
# import ssl
import requests
from citymap import city

# ssl._create_default_https_context = ssl._create_unverified_context
# 设置不对证书进行校验

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.8'}


def get_track(url):
    response = requests.get(url, headers=header, verify=False).json()
    result = response['data']['result']
    c = 0
    for i in result:
        for a in i.strip().split('|'):
            # 车次 3；发车时间 8；到达时间 9；总耗时 10；
            print('{}:{}'.format(c, a))
            c += 1


url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-11-07&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'

citymap = city()
from_station = input('请输入始发地：')
from_station = citymap.find_citymap(from_station)
to_station = input('请输入目的地：')
to_station = citymap.find_citymap(to_station)
get_track(url.format(from_station, to_station))


