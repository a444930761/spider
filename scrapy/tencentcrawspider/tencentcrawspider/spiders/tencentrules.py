# -*- coding: utf-8 -*-
#import scrapy
#import logging
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
from tencentcrawspider.items import TencentcrawspiderItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from scrapy.mail import MailSender

class DefaultItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
    #定义一个类，继承ItemLoader，设置输出为TakeFirst()，即第一个
    
class TencentrulesSpider(CrawlSpider):
#    logging.log(logging.WARNING,'这个是怎么输出的')
    name = 'tencentrules'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php']
    rule1 = LinkExtractor(allow=('start=\d'))
    rule2 = LinkExtractor(allow=('position_detail.php'))
    rules = [Rule(rule1),Rule(rule2,callback='findtitle')]
    
    def findtitle(self, response):
        l = DefaultItemLoader(item=TencentcrawspiderItem(),response=response)
        l.add_xpath('title','//td[@id="sharetitle"]/text()')
        return l.load_item()
#        items = TencentcrawspiderItem()
#        items['title'] = response.xpath('//td[@id="sharetitle"]/text()')
#        return items
'''
    def closed(self,spider):
        mailer = MailSender(smtphost='smtp.qq.com',
                            mailfrom='scrapy',
                            smtpuser='1877628404@qq.com',
                            smtppass='ngqliwfkzgthijih',
                            smtpport=25)
        body = '爬虫结束'
        title = 'scrapytitle'
        mailer.send(to=['444930761@qq.com'],subject=title,body=body)
''' 