#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/15 11:45
# @Author  : sonny
# @Site    : 
# @File    : test.py
# @Software: PyCharm
import urllib2
import urllib
from lxml import tree

class getObject():
    price = 0.0
    store = ""
    category = ""
    dealSize = 0
    commentSize = ""
    link = ""

    def __init__(self, price, store, category, dealSize, commentSize,link):
        self.price = price
        self.store = store
        self.category = category
        self.dealSize = dealSize
        self.commentSize = commentSize
        self.link = link


def showCompleteUrl(num):
    num = -1 + 60 * num
    baseUrl = "https://list.tmall.com/"
    compeleteUrl = baseUrl + "search_product.htm?spm=a220m.1000858.0.0.dEqp2T&cat=50025983&s={0}&q=%D0%D8%D5%D6&sort=s&style=g&from=mallfp..pc_1_suggest&suggest=0_1&type=pc#J_Filter".format(num)
    return compeleteUrl


def getURL():
    values = ["username"]
    response = urllib2.urlopen("http://mail.163.com")
    print response.read()


if __name__ == "__main__":
    for i in range(0, 100):
        print showCompleteUrl(i)
