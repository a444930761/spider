# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 15:13:26 2017

@author: Administrator
"""
import requests
import re
import pytesseract
from PIL import Image
from io import BytesIO
import os


s = requests.Session()
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36','Accept-Language': 'zh-CN,zh;q=0.8'}

def get_captcha():
    print('开始获取验证码')
    response = s.get('https://www.douban.com/login',headers=header,verify=False).text
    captchaid = re.findall(r'name="captcha-id" value="([\w\W]*?)"',response)
    
    codeurl = 'https://www.douban.com/misc/captcha?id={}&size=s'.format(captchaid[0])
    code = s.get(codeurl,headers=header,verify=False).content
    
    with open('douban.png','wb') as f:
        f.write(code)
    print('验证码图片已保存在{}'.format(os.getcwd()))
    codeimg = input('请输入验证码:')
    return captchaid,codeimg
'''
code = BytesIO(code)
codepng = Image.open(code)
codepng.save('douban.png')
print('保存验证码')
codepng = codepng.convert('L')
codepng = codepng.point(lambda x: 0 if x<1 else 255)
codepng.save('douban1.png')
print('保存验证码1')
codeimg = pytesseract.image_to_string(codepng)
print('识别验证码为：',codeimg)
'''

def logindouban(form_email,form_password):
    captchaid,codeimg = get_captcha()    
    
    data = {'source':None,
            'redir':'https://www.douban.com',
            'form_email':form_email,
            'form_password':form_password,
            'captcha-solution':codeimg,
            'captcha-id':captchaid[0],
            'login':'登录'}
    url = 'https://accounts.douban.com/login'
    print('开始登录')
    response2 = s.post(url,data=data,headers=header,verify=False)
    print(response2.url,response2.text)

if __name__=='__main__':
    form_email = input('请输入邮箱账号：')
    form_password = input('请输入密码：')
    logindouban(form_email,form_password)