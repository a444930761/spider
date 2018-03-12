# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 16:13:08 2017

@author: liwei

E-mail:444liwei@163.com

"""
import requests

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36','Accept-Language': 'zh-CN,zh;q=0.8'}

s = requests.Session()

def get_captcha():
    url = 'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand'
    response = s.get(url,headers=header,verify=False).content
    with open('验证码.png','wb') as f:
        f.write(response)
    print('验证码下载成功')

def check_captcha():
    get_captcha()
    url = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
    codemap = {1:'34,34',2:'110,34',3:'186,34',4:'262,34',
           5:'34,110',6:'110,110',7:'186,110',8:'262,110'}
    
    captcha = input('请输入图片序号：')
    if len(captcha) == 1:
        code = codemap[int(captcha)]
    else:
        codelist = []
        for i in captcha:
            codelist.append(codemap[int(i)])
        code = ','.join(codelist)
        
    data = {'answer':code,
            'login_site':'E',
            'rand':'sjrand'}
    response = s.get(url,headers=header,params=data,verify=False).json()
    return response

def login(username,password):
    url = 'https://kyfw.12306.cn/passport/web/login'
    data = {'username':username,
            'password':password,
            'appid':'otn'
            }
    response = s.get(url,params=data,headers=header,verify=False).json()
    print(response['result_message'])
    
    

def main(username,password):
    code = check_captcha()
    print(code['result_message'],code['result_code'])
    if int(code['result_code']) == 4:
        login(username,password)
    else:
        print('验证失败')
        
username = input('请输入用户名：') 
password = input('请输入密码：')   
main(username,password)    

