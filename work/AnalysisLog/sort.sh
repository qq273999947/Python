#!/bin/bash

./find.py |sort -r |awk '{a[$1]+=$2}END{for (i in a) print i,a[i];}'|sort -rn -k2|head -n 1000 > top.txt
