#!/usr/bin/python
# coding:utf-8

import urllib
import urllib2


url = "http://boxvideo.vp.hz-orp.int.baidu.com/video/quality/infos/?ids=144115191564491170"

req = urllib2.Request(url)
#print req

res_data = urllib2.urlopen(req)
res = res_data.read()
print res
