#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/1/10 17:13
# @Author  : sonny
# @Site    : 
# @File    : PearsonCorrelation.py
# @Software: PyCharm
import math
import numpy as np

def computeCorrelation(x,y):
    xMean = np.mean(x)
    yMean = np.mean(y)
    SSR = 0
    varX = 0
    varY = 0
    for i in xrange(0,len(x)):
        diffXBar = x[i] - xMean
        diffYBar = y[i] - yMean
        SSR += (diffXBar * diffYBar)
        varX += diffXBar**2
        varY += diffYBar**2

    SST = math.sqrt(varX*varY)
    return SSR/SST

def polyfit(x,y,degree):
    results = {}

    #degree 几重的线性回归
    coeffs = np.polyfit(x, y, degree)
    results['polynomial'] = coeffs.tolist()

#一维的线性回归
    p = np.poly1d(coeffs)
    yhat = p(x)
    ybar = np.sum(y)/len(y)
    ssreg = np.sum((yhat-ybar)**2)
    sstot = np.sum((y-ybar)**2)
    results['determination'] = ssreg/sstot
    return results

if __name__ == "__main__":
    testX = [1,3,8,7,9]
    testY = [10,12,24,21,34]

    resu = computeCorrelation(testX, testY)
    print "r:",resu
    print "r**2",resu**2

    print polyfit(testX, testY, 1)['determination']