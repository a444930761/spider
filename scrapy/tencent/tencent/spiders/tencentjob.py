# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem
import copy

class TencentjobSpider(scrapy.Spider):
    name = 'tencentjob'
    allowed_domains = ['hr.tencent.com']
    baseurl = 'http://hr.tencent.com/'
    offset = 'position.php?&start=0#a'
    start_urls = [baseurl + offset]
    
    def parse2(self,response):
        item = response.meta['key']
        jobduties = response.xpath('//tr[@class="c"][1]/td[@colspan="3"]/ul')[0].xpath('string(.)')
        jobrequirement = response.xpath('//tr[@class="c"][2]/td[@colspan="3"]/ul')[0].xpath('string(.)')
        
        item['jobduties'] = jobduties.extract()[0]
        item['jobrequirement'] = jobrequirement.extract()[0]

        yield  item

    
    def parse(self, response):
        result = response.xpath('//tr[@class="even" or @class="odd"]')
        item = TencentItem()
        for i in result:
            title = i.xpath('./td[1]/a/text()').extract()[0]
            link = 'http://hr.tencent.com/' + str(i.xpath('./td[1]/a/@href').extract()[0])
            if len(i.xpath('./td[2]/text()')) == 0:
                category = ''
            else:
                category = i.xpath('./td[2]/text()').extract()[0]
            num = i.xpath('./td[3]/text()').extract()[0]
            city = i.xpath('./td[4]/text()').extract()[0]
            time = i.xpath('./td[5]/text()').extract()[0]
            
            item['title']=title
            item['link']=link
            item['category']=category
            item['num']=num
            item['city']=city
            item['time']=time
            
            yield scrapy.Request(link,callback=self.parse2,meta={'key':copy.deepcopy(item)})
      
#        for a in scrapy.Request(link,callback=self.findlist):
#        a = scrapy.Request(link,callback=self.findlist)
#        print(a)
#        jobduties = a[0]
#        jobrequirement = a[1]
#        item.append([title,link,category,num,city,time,jobduties,jobrequirement])
#        yield item[0] 
        
        if len(response.xpath('//*[@id="next"]/@class')) == 0:
            offset = response.xpath('//*[@id="next"]/@href').extract()[0]
            url = self.baseurl + str(offset)
            yield scrapy.Request(url,callback=self.parse)