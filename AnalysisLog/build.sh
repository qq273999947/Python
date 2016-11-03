#!/bin/bash

sh sort.sh

echo "download the news....[3/3]"
./get.py > meta.txt
