# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 20:38:40 2017

@author: Administrator
"""
import requests
from lxml import etree
urllist = []
titlelist = []
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.8'}
#basicurl = 'http://www.chinadaily.com.cn/china/society_'
#num = 2
count = 1
while count:
    #starturl = basicurl+str(num)+'.html'
    starturl = 'http://www.chinadaily.com.cn/china/society_62.html'
    response = requests.get(starturl,headers=headers)
    reqHTML = response.text
    html = etree.HTML(reqHTML)
    result = html.xpath('//div[@class="mb10 tw3_01_2"]')
    for each in result:
        title = each.xpath('.//h4/a/text()')
        if len(title)==0:
            title = each.xpath('./span/p/text()')
        time = each.xpath('.//b/text()')
        print(title)
        titleurl = each.xpath('./a/@href')
        url = 'http://www.chinadaily.com.cn/china/'+titleurl[0]
        urllist.append(url)
        titlelist.append(title)
    count -= 1 
    #num += 1
#print(len(urllist))
#print(titlelist)

#获取页面
