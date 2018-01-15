#! /usr/bin/python
# -*- coding:utf-8 -*-

print "hello"
print "你好"

age = 20
city = "beijing"

print age,
print city

a, b, c = 1, 3, "three"

print a,
print b,
print c

#　字符串
s1, s2 = "hello ", "python"
print s1+s2

# 数组
list = [123, 2.12, "john", 3.14]
tinylist = [1,2]
print list
print list[0]
print list[1:3]
print tinylist *2      #输入列表两次
print list + tinylist  #数组组合
print list[-2]

print __name__
print __file__