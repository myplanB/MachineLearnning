#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/1/10 18:18
# @Author  : sonny
# @Site    : 
# @File    : kmeans.py
# @Software: PyCharm

import numpy as np


# x 数据集
# k 类别
# maxIt  迭代次数
def shouldStop(oldCentroids, centroids, iterations, maxIt):
    if iterations > maxIt:
        return True
    # 比较值相等
    return np.array_equal(oldCentroids, centroids)


def getLabelFromClosestCentroid(dataSetRow, centroids):
    label =centroids[0,-1]
    # 求导
    minDist = np.linalg.norm(dataSetRow - centroids[0,:-1])
    for i in range(1,centroids.shape[0]):
        dist = np.linalg.norm(dataSetRow - centroids[i,:-1])
        if dist < minDist:
            minDist = dist
            label = centroids[i,-1]
    print ("minDist:",minDist)
    return label


def updateLabels(dataSet, centroids):
    numPoints,numDim = dataSet.shape
    for i in range(0,numPoints):
        dataSet[i,-1] = getLabelFromClosestCentroid(dataSet[i,:-1],centroids)


def getCentroids(dataSet, k):
    result = np.zeros((k,dataSet.shape[1]))
    for i in range(1,k+1):
        oneCluster = dataSet[dataSet[:,-1] == i,:-1]
        result[i-1,:-1] = np.mean(oneCluster,axis=0)
        result[i-1,-1] = i

    return result


def keans(x, k, maxIt):
    # 获取数据集的行、列数
    numPoints, numDim = x.shape

    # 新建空数据集，并将x的数据集导入其中
    dataSet = np.zeros((numPoints, numDim + 1))
    dataSet[:, :-1] = x

    # 随机从数据集中选出k行
    centroids = dataSet[np.random.randint(numPoints, size=k), :]
    # 增加一列，标记为序号
    centroids[:, -1] = range(1, k + 1)

    iterations = 0
    oldCentroids = None

    while not shouldStop(oldCentroids, centroids, iterations, maxIt):
        print ("iteration: \n", iterations)
        print ("dataset: \n", dataSet)
        print ("centroid: \n", centroids)

        oldCentroids = np.copy(centroids)
        iterations += 1
        updateLabels(dataSet, centroids)
        centroids = getCentroids(dataSet, k)

    return dataSet


if __name__ == "__main__":
    x1 = np.array([1,1])
    x2 = np.array([2,1])
    x3 = np.array([4,3])
    x4 = np.array([5,4])
    testX = np.vstack((x1,x2,x3,x4))
    result = keans(testX,2,10)
    print ("final result:")
    print (result)
