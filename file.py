#! /usr/bin/python
# -*- coding:utf-8 -*-

import os

doc = open('testfile.txt',"w+")
print "文件名：", doc.name

doc.write("hello")
doc.close()

try:
    doc = open('testfile2.txt',"r")
    doc.write("这是一个测试文件")
except IOError:
    print "error: not found file"
else:
    print "write success"
    doc.close()
