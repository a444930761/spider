g# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 18:42:59 2017

@author: Administrator
"""
import csv
from zipfile import ZipFile
import requests
from StringIO import StringIO

zipped_data = requests.get('http://s3.amazonaws.com/alexa-static/top-1m.csv.zip')
with open('top-1m.csv.zip','wb') as f:
    f.write(zipped_data.content)
urls = []
with ZipFile(StringIO(zipped_data)) as zf:
    csv_filename = zf.namelist()[0]
    for _, website in csv.reader(zf.open(csv_filename)):
        urls.append('http://'+website)
        





