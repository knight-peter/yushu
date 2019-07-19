#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/18 10:43
# @Author  : xuqi
# @Site    : 
# @File    : c2.py
# @Software: PyCharm

# map
list_x = [1, 2, 3, 4, 5, 6, ]
list_y = [1, 2, 3, 4, 5, 6, 7, 8]


def square(x):
  return x * x


# for x in list_x:
#   square(x)

r = map(lambda x, y: x + y, list_x, list_y)

print(list(r))
