#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/18 14:20
# @Author  : xuqi
# @Site    : 
# @File    : c8.py
# @Software: PyCharm

import time
def decorator(func):
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)
    return wrapper

@decorator
def f1(func_name):
    print('This is a function named '+func_name)
# f1('text')

@decorator
def f2(func_name1='1',func_name2='2'):
    print('This is a function named ' + func_name1)
    print('This is a function named ' + func_name2)

# f2()

@decorator
def f3(func_name1,func_name2,**kw):
    print(func_name1)
    print(func_name2)
    print(kw)

f3('test1','test2',a=1,b=2,c='123')