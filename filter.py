#! /usr/bin/python
# -*- coding:utf-8 -*-

def increase_name(name):
    idx = int(filter(str.isdigit, name))
    return "peer" + str(idx +1)

print increase_name("2peer1")
