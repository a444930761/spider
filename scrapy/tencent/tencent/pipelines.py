# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import sqlite3

class TencentPipeline(object):
    def __init__(self):
        self.conn = sqlite3.connect('test.db')
        self.c = self.conn.cursor()
        self.conn.execute('drop table if  exists tencentjob')
        self.c.execute('''create table tencentjob
          (title text,
          link text,
          category text,
          num text,
          city text,
          time time,
          jobduties text,
          jobrequirement text
          );''')
        self.insql = 'insert into tencentjob values(?,?,?,?,?,?,?,?)'

    def process_item(self, item, spider):
        self.c.execute(self.insql,(item['title'],item['link'],item['category'],item['num'],item['city'],item['time'],item['jobduties'],item['jobrequirement']))
        self.conn.commit()
        return item

    def close_spider(self,spider):
        self.conn.close()