# -*- coding: utf-8 -*-
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware 
import random
from doubanspider.settings import USER_AGENTS

class DoubanUserAgent(UserAgentMiddleware):

    def process_request(self, request, spider):
        ua = random.choice(USER_AGENTS)
        print(ua)
        request.headers.setdefault('User-Agent',ua)
        
