#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/15 10:22
# @Author  : sonny
# @Site    : 
# @File    : sourcecodeTest.py
# @Software: PyCharm

from numpy import *
import matplotlib.pyplot as plt

def loadDataSet():
    dataMat = [];
    labelMat = []
    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat, labelMat


def sigmoid(inX):
    return 1.0 / (1 + exp(-inX))


def gradAscent(dataMatIn, classLabels):
    dataMatrix = mat(dataMatIn)  # convert to NumPy matrix
    labelMat = mat(classLabels).transpose()  # convert to NumPy matrix
    m, n = shape(dataMatrix)
    alpha = 0.001
    maxCycles = 500
    weights = ones((n, 1))
    for k in range(maxCycles):  # heavy on matrix operations
        h = sigmoid(dataMatrix * weights)  # matrix mult
        error = (labelMat - h)  # vector subtraction
        weights += alpha * dataMatrix.transpose() * error  # matrix mult
    return weights


def plotBestFit(weights):

    dataMat, labelMat = loadDataSet()
    # 将二维列表list(list)-> 转换成二维数组 array(array)
    dataArr = array(dataMat)
    # 获取行数
    n = shape(dataArr)[0]
    xcord1 = []
    ycord1 = []
    xcord2 = []
    ycord2 = []
    for i in range(n):
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i, 1])
            ycord1.append(dataArr[i, 2])
        else:
            xcord2.append(dataArr[i, 1])
            ycord2.append(dataArr[i, 2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = arange(-3.0, 3.0, 0.1)
    y = (-weights[0] - weights[1] * x) / weights[2]
    ax.plot(x, y)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()

if __name__ == "__main__":
    dataMat, labelMat = loadDataSet()
    weights = gradAscent(dataMat,labelMat)
    plotBestFit(weights)