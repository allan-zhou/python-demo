#! /usr/bin/python
# -*- coding:utf-8 -*-

a = 21
b = 10
c = 0

c = a + b
print "a+b= ", c

c = a / b
print "a/b= ", c

# 幂, 返回ｘ的ｙ次方
c = b**2
print "b**2= ", c

# for循环
for letter in "python":
    print "当前字母是：", letter

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
    print "当前水果是：",fruit
print "len(fruits): ",len(fruits)

for index in range(len(fruits)):
    print "当前索引是：", index, " 当前水果是：", fruits[index]
