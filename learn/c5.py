#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/18 11:20
# @Author  : xuqi
# @Site    : 
# @File    : c5.py
# @Software: PyCharm

list_x = [1,0,1,0,0,1]
r = filter(lambda  x:True if x==1 else False, list_x)

print(list(r))