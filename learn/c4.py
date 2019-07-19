#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/18 11:12
# @Author  : xuqi
# @Site    : 
# @File    : c4.py
# @Software: PyCharm

from functools import reduce

list_y = [1, 2, 3, 4, 5, 6, 7, 8]
r = reduce(lambda x,y:x+y,list_y)
print(r)
