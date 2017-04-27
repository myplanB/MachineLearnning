#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/25 23:29
# @Author  : Sonny
# @Site    :
# @File    : svd.py
# @Software: PyCharm Community Edition
# -*- coding: utf-8 -*-
from numpy import *
import matplotlib.pyplot as plt


# 载入数据
def loadDataSet(fileName, delim="\t"):
    fr = open(fileName)
    stringArr = [line.strip().split(delim) for line in fr.readlines()]
    # 将所有数据转换成浮点型数据
    datArr = [map(float, line) for line in stringArr]
    return mat(datArr)


def pca(dataMat, topNfeat=9999999):
    # 计算平均值
    meanVals = mean(dataMat, axis=0)
    # 减去平均值
    meanRemoved = dataMat - meanVals
    # numpy.cov()的作用是计算协方差矩阵,rowvar=True--行代表一个变量，rowvar=False---列代表一个变量
    convMat = cov(meanRemoved, rowvar=False)
    # 计算协方差矩阵的特征值和特征向量
    eigVals, eigVects = linalg.eig(mat(convMat))
    # 讲特征值进行排序（小 --> 大）并输出序号
    eigValInd = argsort(eigVals)
    # 取排序数组中的前N个特征
    eigValInd = eigValInd[:-(topNfeat + 1):-1]
    redEigVects = eigVects[:, eigValInd]
    lowDDataMat = meanRemoved * redEigVects
    reconMat = (lowDDataMat * redEigVects.T) + meanVals
    return lowDDataMat, reconMat


def replaceNanWithMean(path):
    datMat = loadDataSet(path, " ")
    numFeat = datMat.shape[1]
    for i in range(numFeat):
        meanVal = mean(datMat[nonzero(~isnan(datMat[:, i].A))[0], i])

        datMat[nonzero(isnan(datMat[:, i].A))[0], i] = meanVal
    return datMat


if __name__ == "__main__":
    dataMat = loadDataSet("testSet.txt")
    lowDMat, reconMat = pca(dataMat, 2)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(dataMat[:, 0].flatten().A[0], dataMat[:, 1].flatten().A[0], marker='^', s=90)
    ax.scatter(reconMat[:, 0].flatten().A[0], reconMat[:, 1].flatten().A[0], marker='o', s=50, c='red')
    plt.show()
