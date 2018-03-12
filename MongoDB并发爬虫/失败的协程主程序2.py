# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 22:15:03 2017

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 20:56:30 2017

@author: Administrator
"""

import multiprocessing
from mongo_queue import MongoQueue
from download1 import Download
import asyncio
import time

SLEEP_TIME = 1
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36','Accept-Language': 'zh-CN,zh;q=0.8'}

dealy=2


def threaded_crawler(delay=5, cache=None, scrape_callback=None, user_agent='wswp', proxies=None, num_retries=1, max_threads=10, timeout=60):
    """Crawl using multiple threads
    """
    # the queue of URL's that still need to be crawled
    urllist = MongoQueue()#查找是否有状态为0的数据，返回一个true或者false
    D = Download()
    loop = asyncio.get_event_loop()
    while True:
        try:
            url = urllist.pop()
            print(url)
            tasks =[asyncio.ensure_future(D.Downloader(url))]*10
            loop.run_until_complete(asyncio.wait(tasks))
            urllist.complete(url)
        except KeyError:
            break
    
    '''
    urllist = MongoQueue()#查找是否有状态为0的数据，返回一个true或者false
    def process_queue():
        D = Download()
        loop = asyncio.get_event_loop()
        while True:
            # keep track that are processing url

            try:
                url = urllist.pop()
                print('url',url)
                loop.run_until_complete(asyncio.ensure_future(D.Downloader(url)))
#                D.Downloader(url)
            except KeyError:
                # currently no urls to process
                break
            


    # wait for all download threads to finish
    threads = []
    while threads or urllist:
        for thread in threads:
            if not thread.is_alive():
                threads.remove(thread)
        print(urllist.peek() is True)
        if urllist.peek():
            while len(threads) < max_threads:
                # can start some more threads
                thread = threading.Thread(target=process_queue)
                thread.setDaemon(True) # set daemon so main thread can exit when receives ctrl-c
                thread.start()
                threads.append(thread)
        else:
            break
        time.sleep(SLEEP_TIME)
'''



#def process_crawler(args, **kwargs):
if __name__=='__main__':
    now = lambda :time.time()
#    __spec__ = "ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>)"
    num_cpus = multiprocessing.cpu_count()
    #pool = multiprocessing.Pool(processes=num_cpus)
    print('Starting {} processes'.format(num_cpus))
    processes = []
    start = now()
    for i in range(num_cpus):
        p = multiprocessing.Process(target=threaded_crawler)
        #parsed = pool.apply_async(threaded_link_crawler, args, kwargs)
        p.start()
        processes.append(p)
    # wait for processes to complete
    for p in processes:
        p.join()
    print(now()-start)

#def normalize(seed_url, link):
#    """Normalize this URL by removing hash and adding domain
#    """
#    link, _ = urlparse.urldefrag(link) # remove hash to avoid duplicates
#    return urlparse.urljoin(seed_url, link)