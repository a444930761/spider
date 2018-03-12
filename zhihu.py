# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 20:10:12 2017

@author: liwei

E-mail:444liwei@163.com

"""
import requests
from lxml import etree

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36','Accept-Language': 'zh-CN,zh;q=0.8'}

url = 'https://www.zhihu.com/people/ma-zong-rui-2/following'

response = requests.get(url,headers=header).text
ht

