#! /usr/bin/python
# -*- coding:utf-8 -*-

def printme(str):
    "打印字符串"
    print str
    return

printme("hello")
printme("python")

def add(a,b):
    "加法"
    return a+b

print(add(1,1))

def sub(a,b):
    "减法"
    c = a - b
    return c

print(sub(2,3))

# 不定长参数
def sum(a, *args):
    result = a
    for v in args:
        result += v
    return result

print(sum(1,2,3,4,5))