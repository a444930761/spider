# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from doubanspider.items import DoubanspiderItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from scrapy_redis.spiders import RedisSpider
#class DeafultItemLoader(ItemLoader):
#    default_output_processor = TakeFirst()
    
class DoubanbookSpider(RedisSpider):
    name = 'doubanbook'
#    redis_key = 'doubanbook:start_urls'
#    allowed_domains = ['https://book.douban.com/']
    start_urls = ['http://www.whatismyip.com.tw/']
#    rule1 = LinkExtractor(allow=('subject\/\d'),deny=('subject\/\d*?\/buy'))
#    rules = [Rule(rule1,callback='parse2')]
    
    def parse(self,response):
        item = ItemLoader(item=DoubanspiderItem(),response=response)
        item.add_xpath('title','//span/@data-ip')
        yield item.load_item()
    
#    def get_cookie(self):
#        with open ('cookie.txt','r') as f:
#            cookies = {}
#            for line in f.read().split(';'):
#                name,value = line.strip().split('=',1)
#                cookies[name] = value
#        print(cookies)
#        return cookies