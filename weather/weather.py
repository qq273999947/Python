#!user/bin/python
#coding:utf-8

import urllib2
import json
from city import city

cityname = raw_input('你想查哪个城市的天气？\n')
citycode = city.get(cityname)

if citycode:
    url = ('http://www.weather.com.cn/data/cityinfo/%s.html' %citycode )
    content = urllib2.urlopen(url).read() 

    #print type(content)  str
    data = json.loads(content)
    #print type(data)  dict

    result = data['weatherinfo']
    ret = ('%s\n%s~%s')%(result['weather'],
                         result['temp1'],
                         result['temp2'])
    print ret

else:
    print "木有这个城市"
