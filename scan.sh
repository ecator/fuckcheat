#!/bin/bash

range=$1
range=${range:-'1-65535'}

target='www.icloud.ios.itacnes.cn'
echo "scanning ${target} on port ${range}"
nc -zv -w 3 $target $range
