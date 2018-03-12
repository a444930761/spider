# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 20:57:05 2017

@author: Administrator
"""

from datetime import datetime, timedelta
from pymongo import MongoClient, errors


class MongoQueue():
    """
    >>> timeout = 1
    >>> url = 'http://example.webscraping.com'
    >>> q = MongoQueue(timeout=timeout)
    >>> q.clear() # ensure empty queue
    >>> q.push(url) # add test URL
    >>> q.peek() == q.pop() == url # pop back this URL
    True
    >>> q.repair() # immediate repair will do nothin
    >>> q.pop() # another pop should be empty
    >>> q.peek() 
    >>> import time; time.sleep(timeout) # wait for timeout
    >>> q.repair() # now repair will release URL
    Released: test
    >>> q.pop() == url # pop URL again
    True
    >>> bool(q) # queue is still active while outstanding
    True
    >>> q.complete(url) # complete this URL
    >>> bool(q) # queue is not complete
    False
    """

    # possible states of a download
    OUTSTANDING, PROCESSING, COMPLETE = range(3)

    def __init__(self, client=None, timeout=300):
        """
        host: the host to connect to MongoDB
        port: the port to connect to MongoDB
        timeout: the number of seconds to allow for a timeout
        """
        self.client = MongoClient(host='localhost',port=27017,
                                  username='liwei',password='it088078') if client is None else client
        self.db = self.client.cache
        self.timeout = timeout

    def __nonzero__(self):
        """Returns True if there are more jobs to process
        """
        record = self.db.urllist1.find_one(
            {'status': {'$ne': self.COMPLETE}} #查找状态不等于complete的（$ne不等于）
        )
        return True if record else False

    def push(self, url):
        """Add new URL to queue if does not exist
        """
        try:
            self.db.urllist1.insert({'_id': url, 'status':self.OUTSTANDING})
        except errors.DuplicateKeyError as e:
            pass # this is already in the queue

    def pop(self):
        """Get an outstanding URL from the queue and set its status to processing.
        If the queue is empty a KeyError exception is raised.
        """
        record = self.db.urllist1.find_one_and_update({'status':self.OUTSTANDING}, 
       {'$set': {'status':self.PROCESSING, 'timestamp': datetime.now()}}
        )#find_one_and_update返回一个状态为outstanding的数据，而后修改其状态和时间（没有就添加）
        if record:
            return record['_id']
        else:
            self.repair()
            raise KeyError()

    def peek(self):
        record = self.db.urllist1.find_one({'status':self.OUTSTANDING})
        if record:
            return record['_id']

    def complete(self, url):
        self.db.urllist1.update({'_id': url}, {'$set': {'status':self.COMPLETE}})

    def repair(self):
        """Release stalled jobs
        """
        record = self.db.urllist1.find_one_and_update(
                {'timestamp': {'$lt': datetime.now() - timedelta(seconds=self.timeout)},
                               'status': {'$ne':self.COMPLETE}},
                {'$set': {'status':self.OUTSTANDING}})#下载超时的，设置为待下载状态
        if record:
            print('Released:', record['_id'])

    def clear(self):
        self.db.urllist1.drop()
