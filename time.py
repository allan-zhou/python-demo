#! /usr/bin/python
# -*- coding:utf-8 -*-

import time;

ticks = time.time()
print "当前时间戳是：", ticks

localtime = time.localtime(time.time())
print "本地时间是：", localtime

# 格式化时间
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
