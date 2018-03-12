# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 18:35:10 2017

@author: Administrator

官方文档：http://selenium-python.readthedocs.io/api.html
http://blog.csdn.net/u011974639/article/details/73148949
https://www.urlteam.org/2017/02/selenium%E8%AE%BE%E7%BD%AEchrome%E5%92%8Cphantomjs%E7%9A%84%E8%AF%B7%E6%B1%82%E5%A4%B4%E4%BF%A1%E6%81%AF/   设置请求头
http://www.jianshu.com/p/9d408e21dc3a  盘点selenium phantomJS使用的坑
"""
from selenium import webdriver
#导入webdriver
from selenium.webdriver.common.keys import Keys
#调用键盘操作时需要引入的Keys包

'''基本操作'''

driver = webdriver.PhantomJS(executable_path=r'D:\Program Files\phantomjs-2.1.1-windows\bin\phantomjs.exe')
#调用PhantomJs创建浏览器对象
driver.get('http://www.baidu.com')
#模拟浏览器打开网页
driver.find_element_by_id("wrapper").text
#查找id名为“wrapper”的文本内容
driver.title
#查找标题
driver.save_screenshot('baidu.png')
#生成当前页面快照，并保存
driver.find_element_by_id('kw').send_keys('长城')
#查找id为kw的标签，并输入“长城”两个字
driver.find_element_by_id('su').click()
#查找id为su的标签（搜索按钮），并模拟点击
driver.page_source
#获取网页渲染后的源代码
driver.get_cookies()
#获取所有的Cookie
driver.get_cookie(name)
#获取指定的cookie

driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
#在id为kw的标签里执行ctrl+a操作
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')
#在id为kw的标签里执行ctrl+x操作
driver.find_element_by_id('kw').send_keys('爬虫')
#在id为kw的标签里输入‘爬虫’
driver.find_element_by_id('su').send_keys(Keys.ENTER)
#在id为su的标签上执行回车操作
driver.find_element.by_id('kw').clear()
#情况id为kw的标签里的输入内容

driver.current_url
#获取当前url
driver.close()
#关闭当前页面
driver.quit()
#退出浏览器

'''页面操作'''
'''
示例
<input type="text" name="user-name" id="passwd-id" />
'''

element = driver.find_element_by_id('passwd-id')
#依据id属性来查找标签
element = driver.find_element_by_name('user-name')
#依据name属性来查找标签
elemnt = driver.find_element_by_tag_name('input')
#依据标签名来查找标签
element = driver.find_element_by_xpath('//input[@id="passwd-id]')
#还可以使用xpath查找

'''定位UI元素（webelement）'''
element = driver.find_element_by_id('id')
element = driver.find_element_by_name('name')
element = driver.find_element_by_xpath
element = driver.find_element_by_tag_name
element = driver.find_element_by_link_text('link_text')
#通过完整的链接文本查找
element = driver.find_element_by_partial_link_text('link_text')
#通过链接本文的部分信息匹配查找
element = driver.find_element_by_class_name('类名')
element = driver.find_element_by_css_selector('css选择器')
'''
element,匹配的是首个，elements匹配的是所有
'''

'''鼠标动作'''
from selenium.webdriver import ActionChains
#导入ActionChains鼠标动作类
ac = driver.find_element_by_xpath('element')
#定位ac的位置
ActionChains(driver).move_to_element(ac).perform()
#将鼠标移动到ac的位置

ActionChains(driver).move_to_element(ac).click(ac).perform()
#在ac的位置进行单击

ActionChains(driver).move_to_element(ac).double_click(ac).perform()
#在ac的位置进行双击

ActionChains(driver).move_to_element(ac).context_click(ac).perform()
#在ac的位置进行右击

ActionChains(driver).move_to_element(ac).click_and_hold(ac).perform()
#在ac的位置左键单击并hold住

ac2 = driver.find_element_by_xpath('elementA')
ActionChains(driver).drag_and_drop(ac,ac2).perform()
#将ac拖拽到ac2的位置


'''针对下拉选择框'''
'''示例
<select id="status" class="form-control valid" onchange="" name="status">
    <option value=""></option>
    <option value="0">未审核</option>
    <option value="1">初审通过</option>
    <option value="2">复审通过</option>
    <option value="3">审核不通过</option>
</select>
'''
from selenium.webdriver.support.ui import Select
#导入Select类
select = Select(driver.find_element_by_name('status'))
#通过name找到下拉选择框位置
select.select_by_index(0)
#通过索引进行选择
select.select_by_value(0)
#通过属性中的value值进行选择
select.select_by_visible_text('未审核')
#通过标签文本值进行选择


'''弹窗处理'''

alert = driver.switch_to_alert()
#获取提示信息

'''页面切换'''
driver.switch_to.window('窗口名称')
#直接通过窗口名切换
for handle in driver.window_handles:
    driver.switch_to_window(handle)
#通过for循环进行切换
'''frame切换'''
driver.switch_to_frame('iframename')
driver.switch_to_default_content()  #切换回默认区域

'''页面的前进和后退'''
driver.forward() 
#前进
driver.back()
#后退

'''Cookies'''
for cookie in driver.get_cookies():
    print('{}={}'(cookie['name'],cookie['value']))
#输出每个页面的cookie
driver.delete_cookie('name')
#删除指定页面的cookie
driver.delete_all_cookies()
#删除所有的cookie

'''页面等待'''
'''
显示等待
指定某个条件，然后设置最长等待时间。如果在这个时间还没有找到元素，那么便会抛出异常了
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#WebDriverWait 库，负责循环等待
from selenium.webdriver.support import expected_conditions as EC
#expected_conditions 类，负责条件出发

driver = webdriver.PhantomJS(excutable_path='...phantomjs.exe')
driver.get('http://www.xxx.com')
try:
    element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID,"myDynamicElement"))
            )
    #每隔10秒查找页面id=myDynamicElement，出现则返回，默认是0.5秒
finally:
    driver.quit()
    
'''下面是内置的等待条件，可直接调用...
title_is
title_contains
presence_of_element_located
visibility_of_element_located
visibility_of
presence_of_all_elements_located
text_to_be_present_in_element
text_to_be_present_in_element_value
frame_to_be_available_and_switch_to_it
invisibility_of_element_located
element_to_be_clickable – it is Displayed and Enabled.
staleness_of
element_to_be_selected
element_located_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be
alert_is_present
'''

'''
隐式等待
设置等待时间，时间到了执行，默认为0秒
'''

driver.implicitly_wait(10)
#设置等待10秒
driver.get('http://www.xxx.com')
myDynamicElement = driver.find_element_by_id("myDynamicElement")




from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

url = 'https://httpbin.org/get?show_env=1' #该网址返回请求头


'''设置phantomjs请求头'''

dcap = dict(DesiredCapabilities.PHANTOMJS)

dcap['phantomjs.page.settings.userAgent'] = ("Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0")

driver = webdriver.PhantomJS(desired_capabilities=dcap)

driver.get(url)

driver.save_screenshot('tou.png')

'''设置phantomjs不加载图片'''
dcap['phantomjs.page.setting.loadImages'] = False
browser = webdriver.PhantomJS(desired_capabilities=dcap)
url = "http://image.baidu.com/"
browser.get(url)
browser.quit()



'''设置chrome请求头'''
options = webdriver.ChromeOptions()
#进入浏览器设置
options.add_argument('lang=zh_CN.UTF-8')
#设置中文
options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
#更换头部
browser = webdriver.Chrome(chrome_options=options)
#打开谷歌浏览器，这里需要安装谷歌驱动,而且浏览器版本不能过低
browser.get(url)

'''设置chrome--cookie'''
browser = webdriver.PhantomJS()
browser.get('http://www.baidu.com')
browser.get_cookies()
browser.delete_all_cookies()
#删除所有的cookie
browser.get_cookies()
browser.add_cookie({'name':'ABC','value':'DEF'})
#添加心的cookie
newwindow = "window.open('http://www.baidu.com');"
browser.execute_script(newwindow)
browser.quit()










