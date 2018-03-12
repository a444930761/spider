# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class TencentcrawspiderPipeline(object):
    def __init__(self):
        self.f = open('1232212.json','w+')
    def process_item(self, item, spider):
#        a = json.dumps(dict(item),ensure_ascii=False)+',\n'
        print('*'*40)
        print(item)
        print('*'*40)
#        self.f.write(a)
        return item
    def close_spider(self,spider):
        self.f.close()