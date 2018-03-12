# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 16:08:51 2017

@author: Administrator
"""
import requests

url = 'https://login.tmall.com'

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36','Accept-Language': 'zh-CN,zh;q=0.8'}

s = requests.Session()

def get_cookies():
    with open ('cookie.txt','r') as f:
        cookies = {}
        for line in f.read().split(';'):
            name,value = line.strip().split('=',1)
            cookies[name] = value
    print(cookies)
    return cookies

def login(url):
    cookies = get_cookies()
    html1 = s.get(url,headers=header,verify=False)
    
    with open('example1.txt','w+') as fl:
        fl.write(html1.text)
        
    html = s.get(url,headers=header,cookies=cookies,verify=False)

    with open('example.txt','w+') as fl:
        fl.write(html.text)
        
if __name__ =='__main__':
    login(url)