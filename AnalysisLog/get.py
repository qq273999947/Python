#!/usr/bin/python
# coding:utf-8

import urllib
import urllib2
import sys
import json

for line in open('key'):
    key = line.upper()
    url = "http://..." + key
    req = urllib2.Request(url)

    res_data = urllib2.urlopen(req)
    res = res_data.read()
    
    js = json.loads(res.encode('latin-1'))
    i = js['data']
    l = len(i)
    #print l
    
    if l > 0:
        print res
