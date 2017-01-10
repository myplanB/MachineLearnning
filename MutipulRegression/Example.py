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
    # 从文本文件中获取内容
    deliveryData = genfromtxt(filename,delimiter=',')
    return deliveryData

if __name__ == "__main__":
    # 输出二维数组
    deliveryData = loadData()
    x = deliveryData[:,:-1]
    y = deliveryData[:,-1]
    # 设置线性回归模型
    regr = linear_model.LinearRegression()
    # 拟合操作
    regr.fit(x,y)
    print "coefficients:"
    print regr.coef_
    print "intercept:"
    print regr.intercept_

    xPred = [102,6]
    yPred = regr.predict(xPred)
    print "predicted y:"
    print yPred