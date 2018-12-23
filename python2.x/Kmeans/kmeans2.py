"""
@version: latest
@author: sonny
@license: Apache Licence 
@contact: 715676363@qq.com
@site: 
@software: PyCharm Community Edition
@file: kmeans2.py
@time: 2017/5/3 22:04
"""
from numpy import *


def loadDataSet(filename):
    dataMat = []
    fr = open(filename)
    for line in fr.readlines():
        curLine = line.strip().split("\t")
        dataMat.append(curLine)
    return dataMat


def distEclud(vecA, vecB):
    vecA = mat(vecA)
    vecB = mat(vecB)
    return sqrt(power(vecA - vecB, 2))


# dataSet:数据集
# k: 指定分类数
def randCent(dataSet, k):
    n = shape(dataSet)[1]  # 获取列数
    dataSet = mat(dataSet)
    centroids = mat(zeros((k, n)))
    for j in range(n):
        minJ = float(min(dataSet[:, j])[0, 0])
        maxJ = float(max(dataSet[:, j])[0, 0])
        rangeJ = maxJ - minJ
        centroids[:, j] = minJ + rangeJ * random.rand(k, 1)
    return centroids


def kmeans(dataSet, k,createCent=randCent):
    # 和数据集相同结构的
    clusterAssment = mat(zeros_like(dataSet))
    m = shape(dataSet)[0]
    centroids = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = inf
            minIndex = -1
            # 计算最小距离
            for j in range(k):
                distJI = distEclud(centroids[j, :], dataSet[i, :])
                if distJI < minDist:
                    minDist = distJI
                    minIndex = j
            #
            if clusterAssment[i, 0] != minIndex:
                clusterChanged = True
            clusterAssment[i, :] = minIndex, minDist ** 2
        print(centroids)
        for cent in range(k):
            ptsInclust = dataSet[nonzero(clusterAssment).A == cent]
            centroids[cent, :] = mean(ptsInclust, axis=0)
    return centroids, clusterAssment


if __name__ == "__main__":
    dataMat = loadDataSet('testSet.txt')
    kmeans(dataMat, 4)
