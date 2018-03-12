import aiohttp
import asyncio
import string
import json
#from pymongo import MongoClient

async def get(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                assert resp.status == 200
                html = await resp.json()              
                return html
    except AssertionError as e:
        print(resp.status,e)
        return None
            
    
            
if __name__ =='__main__':
    country = set()
    url = 'http://httpstat.us/500'
    url1 = 'http://example.webscraping.com/places/ajax/search.json?&search_term={}&page_size=10&page={}'
    loop = asyncio.get_event_loop()
    for letter in string.ascii_lowercase:
        page = 0
        while True:          
            ajax = loop.run_until_complete(asyncio.ensure_future(get(url1.format(letter,page))))
            if ajax:
                for result in ajax['records']:
                    country.add(result['country'])
                page += 1
            elif ajax is None or page > ajax['num_pages']:
                break
            
以上for循环可用以下代码替换（用正则中的.匹配出所有的字母，将page_size设置大点可一次性展示所有数据），因此，了解网站的机制很重要

    url2 = 'http://example.webscraping.com/places/ajax/search.json?&page_size=1000&page=0&search_term=.'
    html = loop.run_until_complete(asyncio.ensure_future(get(url1)))
    for result in ajax['records']:
        country.add(result['country'])
    
    #html = loop.run_until_complete(asyncio.ensure_future(get(url1)))