#!/usr/bin/python
# coding:utf-8

import re
import os


# 遍历指定目录，显示目录下的所有文件名

directory = os.path.expanduser("/home/work/private/yanghuiqin/show_log/videolog")

for f in os.listdir(directory):
   
    file = open('/home/work/private/yanghuiqin/show_log/videolog/'+f,'r')
    log = file.read()
    
    # 匹配提取关键字
    id = re.findall('"id":"sv_(.*?)"',log)
    i = 0
    for each in id:
       print each + " 1"
       i += 1
       
    file.close()

