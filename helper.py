#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/28 22:40
# @Author  : xuqi
# @Site    : 
# @File    : helper.py
# @Software: PyCharm

def is_isbn_or_key(word):
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
