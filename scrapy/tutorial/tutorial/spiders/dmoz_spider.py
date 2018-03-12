# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem

class DmozSpiderSpider(scrapy.Spider):
    name = 'dmoz_spider'
    allowed_domains = ['dmoztools.net']
    start_urls = ['http://dmoztools.net/Computers/Programming/Languages/Python/Books/','http://dmoztools.net/Computers/Programming/Languages/Python/Resources/']

    def parse(self, response):
        #item = TutorialItem()
        for sel in response.xpath('//div[@class="site-item "]'):
#            item['title'] = sel.xpath('//div[@class="site-title"]/text()').extract()
#            item['link'] = sel.xpath('//a/@href').extract()
#            item['desc'] = sel.xpath('//div[@class="site-descr "]/text()').extract()
#            yield item
            a = sel.xpath('//div[@class="site-title"]/text()').extract()
            return TutorialItem(title=a)