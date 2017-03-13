#!/usr/bin/python
# coding:utf-8

import urllib
import urllib2
import sys
import json
import os

def cur_file_dir():
    #获取当前脚本路径
    return os.path.split(os.path.realpath(__file__))[0]

def printUsage():$
    print '''python {} file_key '''.format(sys.argv[0])

if __name__ == '__main__':
    if len(sys.argv) != 3 or (not os.path.isdir(sys.argv[1])):
        printUsage()
        sys.exit()
    files = os.listdir(sys.argv[1])

    f = open(cur_file_dir() + file)
    lines = f.readlines()
    f.close()

    for line in lines:
        line= line.strip('\n')
        url = "http://...." + line +
        try:
            req = urllib2.Request(url)
            res_data = urllib2.urlopen(req)
            res = res_data.read()
            js = json.loads(res.encode('latin-1'))
            i = js[line]['data']['playcnt']
            print line + '\t' + str(i)
        except:
            print line + '\t' + '0'
            continue
