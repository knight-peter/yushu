#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 16:44
# @Author  : xuqi
# @Site    : 
# @File    : fisher.py.py
# @Software: PyCharm

from flask import Flask

__author__ = '徐子玉'

app = Flask(__name__)


@app.route('/hello/')
def hello():
    return 'Hello,XuQi'


app.run()
