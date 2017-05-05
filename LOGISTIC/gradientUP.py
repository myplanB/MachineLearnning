#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@version: latest
@author: sonny
@license: Apache Licence 
@contact: 71567636@qq.com
@site: 
@software: PyCharm
@file: gradientUP.py
@time: 2017/5/5 11:32
"""
from numpy import *

from LOGISTIC.logistic import sigmod
from LOGISTIC.logistic import loadDataSet
from LOGISTIC.logistic import plotBestFit


def stocGradAscentUp(dataMatrix, classLabels):
    m, n = shape(dataMatrix)
    alpha = 0.01
    weights = ones(n)  # 1*3
    for i in range(m):
        h = sigmod(sum(dataMatrix[i] * weights))
        error = classLabels[i] - h
        weights += alpha * error * dataMatrix[i]
    return weights


def stocGradAscentRandom(dataMats, classLabels, numIter=1000):
    # dataMats
    m, n = shape(mat(dataMats))
    weights = ones(n)
    for j in range(numIter):
        dataIndex = arange(m)
        dataIndex = array(dataIndex)
        for i in range(m):
            alpha = 4 / (1.0 + j + i) + 0.01
            randIndex = int(random.uniform(0, len(dataIndex)))
            h = sigmod(sum(dataMats[randIndex] * weights))
            error = classLabels[randIndex] - h
    return weights


if __name__ == "__main__":
    dataArr, labelArr = loadDataSet()
    # weights = stocGradAscentUp(array(dataArr), labelArr)
    # plotBestFit(weights)

    weights = stocGradAscentRandom(array(dataArr),labelArr)
    plotBestFit(weights)