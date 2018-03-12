# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 17:38:08 2017

@author: Administrator
"""
import requests
from lxml import etree
import pandas as pd
import numpy as np
from pandas import DataFrame,Series
import re
url = 'http://www.chinadaily.com.cn/china/2017-09/18/content_32168594.htm'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.8'}
req = requests.get(url,headers=headers)

resHtml = req.text
html = etree.HTML(resHtml)
textlist = []
result = html.xpath('//div[@id="Content"]/text()')
p = re.compile(r'[,."()/\n]')
txt = ' '.join(result).lower()
a = p.sub(' ',txt)
print(txt)
print(a)
db = txt.split(' ')
count = Series(db)
#print(count)
b = count.value_counts()
#print(b)
#b.to_csv('b.csv')
#print(textlist)