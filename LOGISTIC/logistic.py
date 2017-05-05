#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *
import matplotlib.pyplot as plt


# 载入数据
def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split("\t")
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[-1]))
    return dataMat, labelMat


# sigmod 函数
def sigmod(inX):
    return 1.0 / (1 + exp(-inX))


# 梯度下降
def gradAscent(dataMatIn, classlabels):
    # 转换成矩阵
    dataMatrix = mat(dataMatIn)
    # 矩阵转置 labelMat -> classlabels 100*1
    labelMat = mat(classlabels).transpose()  # 1*100
    m, n = shape(dataMatrix)
    alpha = 0.001
    maxCycles = 500
    # 创建单位阵
    weights = ones((n, 1))

    # 频繁更新weights
    for k in range(maxCycles):
        # 矩阵内个元素运算 dataMatrix 100*3 weights 3*1 -> h 100*1
        h = sigmod(dataMatrix * weights)
        error = (labelMat - h)
        weights += alpha * dataMatrix.transpose() * error
    return weights


# 绘制决策边界
def plotBestFit(weights):
    # 加载数据
    dataMat, labelMat = loadDataSet()
    #
    dataArr = array(dataMat)
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
    #arange return list
    x = arange(-3.0, 3.0, 0.1)
    y = (-weights[0] - weights[1] * x) / weights[2]
    ax.plot(x, y)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.grid
    plt.show()


if __name__ == "__main__":
    dataMat, labelMat = loadDataSet()
    weights = gradAscent(dataMat,labelMat)
    plotBestFit(weights)