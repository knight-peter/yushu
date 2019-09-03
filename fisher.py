#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 16:44
# @Author  : xuqi
# @Site    : 
# @File    : fisher.py
# @Software: PyCharm

from flask import Flask,make_response
# from helper import is_isbn_or_key

__author__ = '徐子玉'

app = Flask(__name__)
app.config.from_object('config')


# 必须大写
# print(app.config['DEBUG'])


# 两种路由注册方式
@app.route('/')
def index():
    # 返回的是Response对象
    headers = {
        'content-type': 'application/json'
    }
    # 方法1.创建response
    # response = make_response('<html></html>', 404)
    # response.headers = headers
    # return response
    # 方法2.flask的方法
    return '<html></html>', 301, headers


def hello():
    # 基于类的视图
    return 'Hello,徐琪'


# 使用基于类的视图必须用add_url_rule来注册路由
app.add_url_rule('/hello', view_func=hello)


@app.route('/book/search')
def search(q, page):
    # q:普通关键字 isbn
    # page
    # isbn isbn13 13个0到9的数字组成
    # isbn 10个0到9数字组成，含有一些'-'
    # isbn_or_key = is_isbn_or_key(q)
    pass


# 1.作为入口文件直接被执行，被其他引用不执行 2.在开发环境下被执行
# 本机ip地址：192.168.2.101
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=8081)
