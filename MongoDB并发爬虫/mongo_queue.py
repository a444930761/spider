# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 23:31:40 2017

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 20:57:05 2017

@author: Administrator
"""

from datetime import datetime, timedelta
from pymongo import MongoClient, errors


class MongoQueue():
    # possible states of a download
    OUTSTANDING, PROCESSING, COMPLETE = range(3)

    def __init__(self, client=None, timeout=300):
        self.client = MongoClient(host='localhost',port=27017,
                                  username='liwei',password='it088078') if client is None else client
        self.db = self.client.cache
        self.timeout = timeout

    def __nonzero__(self):
        """Returns True if there are more jobs to process
        """
        record = self.db.urllist.find_one(
            {'status': {'$ne': self.COMPLETE}} #查找状态不等于complete的（$ne不等于）
        )
        return True if record else False

    def push(self, url):
        """Add new URL to queue if does not exist
        """
        try:
            self.db.urllist.insert({'_id': url, 'status':self.OUTSTANDING})
        except errors.DuplicateKeyError as e:
            pass # this is already in the queue

    def pop(self):
        """Get an outstanding URL from the queue and set its status to processing.
        If the queue is empty a KeyError exception is raised.
        """
        record = self.db.urllist.find_one_and_update({'status':self.OUTSTANDING}, 
       {'$set': {'status':self.PROCESSING, 'timestamp': datetime.now()}}
        )#find_one_and_update返回一个状态为outstanding的数据，而后修改其状态和时间（没有就添加）
        if record:
            return record['_id']
        else:
            self.repair()
            raise KeyError()

    def peek(self):
        record = self.db.urllist.find_one({'status':self.OUTSTANDING})
        if record:
            return record['_id']

    def complete(self, url):
        self.db.urllist.update({'_id': url}, {'$set': {'status':self.COMPLETE}})

    def repair(self):
        """Release stalled jobs
        """
        record = self.db.urllist.find_one_and_update(
                {'timestamp': {'$lt': datetime.now() - timedelta(seconds=self.timeout)},
                               'status': {'$ne':self.COMPLETE}},
                {'$set': {'status':self.OUTSTANDING}})#下载超时的，设置为待下载状态
        if record:
            print('Released:', record['_id'])

    def clear(self):
        self.db.urllist.drop()
