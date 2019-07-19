#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/19 14:13
# @Author  : xuqi
# @Site    : 
# @File    : spider.py
# @Software: PyCharm


from urllib import request
import re


class Spider():
    url = 'https://book.douban.com/'
    root_pattern = '<div class="book-info">([\s\S]*?)/div>'
    name_pattern = 'target="_blank">([\s\S]*?)</a>'
    author_pattern = '<div class="author">([\s\S]*?)<'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattern, htmls)
        books = []
        for html in root_html:
            name = re.findall(Spider.name_pattern, html)
            author = re.findall(Spider.author_pattern,html)
            book = {'name': name,'author':author}
            books.append(book)
        return books

    def __refine(self, books):
        l = lambda book: {
            'name': book['name'][0].strip(),
            'author': book['author'][0].strip(),
        }
        return map(l, books)

    def __sort(self,books):
        books = sorted(books,key=self.__sort_seed,reverse=True)
        return books
    def __sort_seed(self,book):
        return book['name']

    def __show(self,books):
        for book in books:
            print(book['name']+'---'+book['author'])

    def go(self):
        htmls = self.__fetch_content()
        books = self.__analysis(htmls)
        books = list(self.__refine(books))
        books = self.__sort(books)
        self.__show(books)

spider = Spider()
spider.go()
