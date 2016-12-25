#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/18 21:32
# @Author  : sonny
# @Site    : 
# @File    : Example.py
# @Software: PyCharm
from numpy import genfromtxt
from sklearn import linear_model

def loadData():
    filename = "Delivery.csv"
    deliveryData = genfromtxt(filename,delimiter=',')
    return deliveryData

if __name__ == "__main__":
    # 输出二维数组
    deliveryData = loadData()
    x = deliveryData[:,0:-1]
    y = deliveryData[:,-1]
    regr = linear_model.LinearRegression()
    regr.fit(x,y)
    print "coefficients:"
    print regr.coef_