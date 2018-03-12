# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
class DoubanspiderPipeline(object):
    def __init__(self):
        self.f = open('save2.json','w+',encoding='utf-8')
    def process_item(self, item, spider):
        a = json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.f.write(a)
        return item
    def close_spider(self,spider):
        self.f.close()

class DoubanImagesPipeline(ImagesPipeline):
    def item_completed(self,results,item,info):
        image_paths = [x['path'] for ok,x in results if ok]
        if not image_paths:
            raise DropItem('not images')
        item['image_paths'] = image_paths
        return item