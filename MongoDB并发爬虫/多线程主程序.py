# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 20:56:30 2017

@author: Administrator
"""
#from pymongo import MongoClient
import time
import threading
import multiprocessing
#from mongo_cache import MongoCache
from mongo_queue import MongoQueue
from download import Download

SLEEP_TIME = 1
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36','Accept-Language': 'zh-CN,zh;q=0.8'}

dealy=2


def threaded_crawler(delay=5, cache=None, scrape_callback=None, user_agent='wswp', proxies=None, num_retries=1, max_threads=10, timeout=60):
    """Crawl using multiple threads
    """
    # the queue of URL's that still need to be crawled
    urllist = MongoQueue()#查找是否有状态为0的数据，返回一个true或者false
    def process_queue():
        while True:
            # keep track that are processing url

            try:
                url = urllist.pop()
                print('url',url)
                D = Download()
                D.Downloader(url)
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

'''def Download(url):
        html = ''
        num = 2
        client = MongoClient(host='localhost',port=27017,username='liwei',password='it088078')
        webpage = client.cache.webpage
        web = webpage.find_one({"_id":url})
        if web and web['code']==200:
            print('缓存已存在')
#            html = web['html']
#            html = pickle.loads(zlib.decompress(html))
        else:
            print('缓存不存在，开始下载')
            try:
                reponse = requests.get(url,headers=header)
#                print(reponse.status_code)
                reponse.raise_for_status()#如果状态码是非2或3开头，则抛出异常
                html = reponse.text
#                html = etree.HTML(req)
            except requests.HTTPError as e:
                print(reponse.status_code,e)
                if 500 <= reponse.status_code < 600:#如果状态码以5开头，则重新爬取
                    if num:
                        time.sleep(dealy)#设置等待时间
                        num -= 1
                        Download(url)
#            self.cache.update_one({"_id":url},{'$set':{"code":reponse.status_code,
#                                   "html":req,"time":datetime.utcnow()}},upsert=True)
#            print(len(html))
#            print(len(zlib.compress(pickle.dumps(html))))
            html = zlib.compress(pickle.dumps(html))
            webpage.insert_one({"_id":url,"code":reponse.status_code,
                                   "html":html,"time":datetime.utcnow()})
            #因为设置了过期自动删除，因此时间要采用世界时间，即UTC时间
            print(reponse.status_code,url+'下载成功')
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