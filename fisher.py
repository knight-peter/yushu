#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 16:44
# @Author  : xuqi
# @Site    : 
# @File    : fisher.py
# @Software: PyCharm

from flask import Flask

__author__ = '徐子玉'

app = Flask(__name__)


# @app.route('/hello/')
def hello():
    # 基于类的视图
    return 'Hello,徐琪'

app.add_url_rule('/hello',view_func=hello)

app.run(debug=True)
