#!/usr/bin/python
# coding:utf-8

import urllib
import urllib2


url = "接口地址"

req = urllib2.Request(url)
#print req

res_data = urllib2.urlopen(req)
res = res_data.read()
print res
