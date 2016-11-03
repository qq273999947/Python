#!/usr/bin/python
# coding:utf-8

import json
import sys

out_list = []
out_list.append('vid')
out_list.append('site_id')
out_list.append('title')
out_list.append('tags')
out_list.append('title')
out_list.append('categoryType')
out_list.append('html5_playurl')
out_list.append('time_length')
out_list.append('site_key')
out_list.append('site_name')

out_file = open('hotVideo.txt', 'w')
out_file_gbk = open('hotVideo_gbk.txt', 'w')

for i in out_list:
   out_file.write(i + '\t')
   out_file_gbk.write(i + '\t')
out_file.write('\n')
out_file_gbk.write('\n')

out_str = ''
out_str_gbk = ''

with open('meta.txt', 'r') as f:
    lines = f.readlines();
    for line in lines:
        js = json.loads(line.encode('latin-1'))
       
        out_file.write( js['data'][0]['id'] + '\t')
        out_file.write( js['data'][0]['site_id'] + '\t')
        out_file.write( js['data'][0]['title'].encode('utf-8') + '\t')
        out_file.write( js['data'][0]['tags'].encode('utf-8') + '\t')
        #out_file.write( js['data'][0]['categoryType'].encode('utf-8') + '\t')
        out_file.write( js['data'][0]['html5_playurl'] + '\t')
        out_file.write( js['data'][0]['publish_time'] + '\t')
        out_file.write( js['data'][0]['time_length'] + '\t')
        out_file.write( js['data'][0]['site_key'] + '\t')
        out_file.write( js['data'][0]['site_name'].encode('utf-8') + '\t')


        out_file_gbk.write( js['data'][0]['id'] + '\t')
        out_file_gbk.write( js['data'][0]['site_id'] + '\t')
        out_file_gbk.write( js['data'][0]['title'].encode('gbk') + '\t')
        out_file_gbk.write( js['data'][0]['tags'].encode('gbk') + '\t')
        #out_file_gbk.write( js['data'][0]['categoryType'].encode('gbk') + '\t')
        out_file_gbk.write( js['data'][0]['html5_playurl'] + '\t')
        out_file_gbk.write( js['data'][0]['publish_time'] + '\t')
        out_file_gbk.write( js['data'][0]['time_length'] + '\t')
        out_file_gbk.write( js['data'][0]['site_key'] + '\t')
        out_file_gbk.write( js['data'][0]['site_name'].encode('gbk') + '\t')
        
        out_file.write('\n')
        out_file_gbk.write('\n')
       
