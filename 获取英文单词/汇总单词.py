# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 16:33:11 2017

@author: Administrator
"""

import pandas as pd
from pandas import DataFrame,Series
txtlist = []
txtlist1 = []
file = open(r'D:\python示例\english\word.json',encoding='gb18030')
for each in file:
    a = each[:-2]
    b = eval(a)
    txtlist.append(b['text'])
txt = ' '.join(txtlist)
a = txt.split(' ')
for each in a:
    if each.isalpha():
        txtlist1.append(each)

word = Series(txtlist1)
count = word.value_counts()
count.to_csv('word2.csv')
