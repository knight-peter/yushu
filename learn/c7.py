#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/18 11:30
# @Author  : xuqi
# @Site    : 
# @File    : c7.py
# @Software: PyCharm

import time


def f1():
    print(time.time())
    print('This is a function')


def f2():
    print('This is a function')

def print_current_time(func):
    print(time.time())
    func()

print_current_time(f2)