# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 09:42:12 2017

@author: Administrator
"""
import requests
from lxml import etree
from io import BytesIO
from PIL import Image
import base64
import pytesseract


header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36','Accept-Language': 'zh-CN,zh;q=0.8'}

url = 'http://example.webscraping.com/places/default/user/login'
url1 = 'http://example.webscraping.com/places/default/user/register?_next=/places/default/index'
s = requests.Session()#传递cookies

def parse_form(html): #获取注册时需提交的post表单内容
    tree = html.xpath('//form/*//input')
    #trees = tree.xpath('./input')
    data = {}
    for i in tree:
        if i.get('name'):
            data[i.get('name')] = i.get('value')
    return data

def get_text(html):#获取验证码
    image = html.xpath('//div[@id="recaptcha"]/img/@src')[0]
    image = image.split(',')[-1]
    binary_image = base64.b64decode(image)
    #网页中可看到，验证码图片是经过bs64编码的，这里进行解码
    file = BytesIO(binary_image)
    #转化为二进制
    img = Image.open(file)
    img = img.convert('L')
    #设置图片格式为‘L’
#    img.save('123.png')#调试用
    img = img.point(lambda x: 0 if x<1 else 255)
    #对图片进行阈值化处理（将背景设置全白）
    text = pytesseract.image_to_string(img)
    #识别图形码
#    print(text) #调试对比用
    return text
    
def register(url,first_name,last_name,email,password):
    response = s.get(url,headers=header)
    html = etree.HTML(response.text)
    data = parse_form(html)
    data['recaptcha_response_field'] = get_text(html)
    data['first_name'] = first_name
    data['last_name'] = last_name
    data['email'] = email
    data['password'] = data['password_two'] = password
    print(response.cookies)
    response2 = s.post(url,data=data)
    print(response2.url)
    print(response2.cookies)
    return '/user/register' not in response2.url
    
if __name__ == '__main__':
    first_name = 'li'
    last_name = 'wei'
    email = '1877628404@qq.com'
    password = 'it088078'
    a = register(url1,first_name,last_name,email,password)
    print(a)




