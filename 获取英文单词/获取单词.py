# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 08:49:46 2017

@author: Administrator
"""
import json
import requests
from lxml import etree
from pandas import Series
titlelist = []
timelist = []
urllist = []
textlist = []
articlelist2 = []
wordlist = []
def openurl(url):
    '打开url，而后返回html的内容'
    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.8'}
    response = requests.get(url,headers=header)
    resHTML = response.text
    html = etree.HTML(resHTML)
    return html

def findlisturl(starturl):
    '获取文章详情页url，每个列表页有15篇文章，获取80个列表页'
    basicurl = starturl
    num = 2
    count = 80
    while count:
        url = basicurl + str(num) + '.html'
        html = openurl(url)
        result = html.xpath('//div[@class="mb10 tw3_01_2"]')
        for each in result:
            titleurl = each.xpath('./a/@href')
            url = 'http://www.chinadaily.com.cn/china/'+titleurl[0]
            urllist.append(url)
            title = each.xpath('.//h4/a/text()')
            titlelist.append(title)
            time = each.xpath('.//b/text()')
            timelist.append(time)
        num += 1
        count -= 1
 
def readurl(urllist):
    '读取文章详情页内容'
    for url in urllist:
        html = openurl(url)
        result = html.xpath('//div[@id="Content"]')
        for each in result:
            textlist2 = []
            text = each.xpath('.//p')
            #print(url)
            for i in range(len(text)):
                if text[i].text is not None:
                    a = text[i].text.replace(',',' ').replace('.',' ').replace('"',' ').replace('\n',' ')
                    textlist2.append(a)
            txt = (' '.join(textlist2)).casefold()
            textlist.append(txt)    
if __name__ == '__main__':
    starturl = 'http://www.chinadaily.com.cn/china/society_'
    findlisturl(starturl)
    #print(len(urllist))
    readurl(urllist)
    text = ' '.join(textlist)
    db = text.split(' ')
    for each in db:
        if each.isalpha():
            wordlist.append(each)
    word = Series(wordlist)
    a = word.value_counts()
    #a.to_csv('word.csv')  
    print(len(titlelist),len(urllist),len(timelist),len(textlist))
    with open('456.txt','a+') as f:
        for i in range(len(textlist)):
            articlelist = {}
            articlelist['title'] = titlelist[i]
            articlelist['url'] = urllist[i]
            articlelist['time'] = timelist[i]
            articlelist['article'] = textlist[i]
            #articlelist2.append(articlelist)
            f.writelines(json.dumps(articlelist)+'\n')
                