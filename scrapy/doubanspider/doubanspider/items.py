# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst
class DoubanspiderItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    image_url = scrapy.Field()
    images = scrapy.Field()
    pingfen = scrapy.Field()
    image_paths = scrapy.Field()
