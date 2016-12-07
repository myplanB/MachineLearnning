# encoding:utf-8

# 载入数据
from math import exp

from numpy import mat, shape, ones


def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split("\t")
        dataMat.append([1.0, float(lineArr[1]), float(lineArr[2])])
        labelMat.append(int(lineArr[-1]))
    return dataMat, labelMat

def sigmod(inX):
    return 1.0 / (1 + exp(-inX))


def gradAscent(dataMatIn,classlabels):
    # 转换成矩阵
    dataMatrix = mat(dataMatIn)
    # 矩阵转置
    labelMat = mat(classlabels).transpose()
    m,n = shape(dataMatrix)
    alpha = 0.001
    maxCycles = 500
    weights = ones((n,1))
    for k in range(maxCycles):
        h = sigmod(dataMatrix*weights)
        error = (labelMat - h)
        weights += alpha*dataMatrix.transpose()*error
    return weights

if __name__ == "__main__":
    dataMat,labelMat = loadDataSet()
    gradAscent(dataMat,labelMat)