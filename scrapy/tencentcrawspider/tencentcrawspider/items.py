# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst

class TencentcrawspiderItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field(output_processor=TakeFirst())
    title2 = scrapy.Field()
    title3 = scrapy.Field()

