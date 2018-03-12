# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 10:45:17 2017

@author: liwei

E-mail:444liwei@163.com

"""
import scrapy
import re

class ceshi(scrapy.Spider):
        name = 'ceshispider'
        allow_domain = ['example.com']
        start_urls = ['http://example.webscraping.com/places/default/user/login']
        
#        def start_requests(self): #重写start_requests方法，不再从start_urls里面拿数据
#            return [scrapy.Request('http://example.webscraping.com/places/default/user/login',callback = self.ceshi)]
#        #通过Request方法打开指定链接，生成requests对象response，而后调用ceshi函数
#        #start_requests方法返回的必须是个可迭代对象，因此要以列表的形式返回
        
        
        def parse(self,response):
            formkey = re.findall(r'name="_formkey" type="hidden" value="(.*?)"',response.text)[0]
            print(formkey)
            data = {'email':'1877628404@qq.com',
                    'password':'it088078',
                    '_next':'/places/default/index',
                    '_formkey':formkey,
                    '_formname':'login'}
            return [scrapy.FormRequest.from_response(response,formdata=data,callback=self.login)]
        #调用scrapy的post方法进行登录，登录需要提交的表单数据用formdata参数传递，其他
        #要传递的非表单数据，用meta参数传递
        
        def login(self,response):
            with open('456.html','w+') as f:
                f.write(response.text)
#            print(response.url,response.text)
