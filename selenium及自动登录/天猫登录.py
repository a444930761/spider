# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import requests

url = 'https://login.tmall.com/'

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap['phantomjs.page.setting.userAgent'] = (
"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"
)  #添加header

driver = webdriver.PhantomJS(desired_capabilities=dcap)
driver.get(url)
driver.save_screenshot('log.png')
time.sleep(2)
driver.switch_to_frame('J_loginIframe') #登录是在iframe里面，切换到iframe
#driver.switch_to_default_content()  #切换回默认区域
#driver.page_source
driver.find_element_by_id('J_Quick2Static').click() #默认是扫码登录，切换到密码登录
#driver.save_screenshot('log2.png')
driver.find_element_by_name('TPL_username').send_keys('444930761@qq.com')
driver.find_element_by_name('TPL_password').send_keys('lwdtbmm&0330')
driver.find_element_by_id('J_SubmitStatic').click() #点击登录
#
time.sleep(3)
driver.save_screenshot('afterlog.png')
cookies = driver.get_cookies()
driver.quit()