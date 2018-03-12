# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 09:56:49 2017

@author: Administrator
"""
from selenium import webdriver
import time
url = 'https://www.douban.com/accounts/login'
driver = webdriver.PhantomJS(executable_path=r'D:\Program Files\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.get(url)
driver.find_element_by_name('form_email').send_keys('444930761@qq.com')
driver.find_element_by_name('form_password').send_keys('5201314Lwdar')
driver.find_element_by_id('captcha_field').send_keys('brick')
driver.find_element_by_name('login').click()
driver.save_screenshot('douban.png')
time.sleep(3)
driver.save_screenshot('douban1.png')
driver.page_source
driver.current_url
#class="shark-pager-next shark-pager-disable shark-pager-disable-next"
#class="shark-pager-next"
