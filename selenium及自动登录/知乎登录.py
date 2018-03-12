# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 11:33:12 2017

@author: liwei

E-mail:444liwei@163.com

"""
import requests
import re
import time

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36','Accept-Language': 'zh-CN,zh;q=0.8'}

url = 'https://www.zhihu.com/'
s = requests.Session()
response = s.get(url,headers=header,verify=False).text

value = re.findall(r'name="_xsrf" value="(\w*?)"',response)

#captchacode = {"img_size":[200,44],"input_points":[[13,25.6],[39,25.6],[65,25.6],[91,25.6],[117.2,25.6],[143,25.6],[169,25.6]]}

codemap = {'1':[18.2,25.6],
           '2':[41.2,25.6],
           '3':[66.2,25.6],
           '4':[89.2,25.6],
           '5':[115.2,25.6],
           '6':[141.2,25.6],
           '7':[165.2,25.6]}

img = s.get('https://www.zhihu.com/captcha.gif?type=login&lang=cn&r={}'.format(int((time.time())*1000)),headers=header).content
with open('123.png','wb') as f:
    f.write(img)
code = input('请输入倒立字的位数：')
inputlist = []
for i in code:
    inputlist.append(codemap[i])

captchacode = {"img_size":[200,44],"input_points":inputlist}

data = {'_xsrf':value[0],
        'email':'444930761@qq.com',
        'password':'5201314lwdar',
        'capthcha_type':'cn',
        'captcha':captchacode}

loginurl = 'https://www.zhihu.com/login/email'
response2 = s.post(loginurl,headers=header,data=data,verify=False)
print(response2.text,response2.url)



