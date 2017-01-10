#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/14 10:59
# @Author  : sonny
# @Site    : 
# @File    : sk_knn.py
# @Software: PyCharm
import csv
import random
import math
import operator


# 载入数据
def loadDataSet(filename, split):
    trainingSet = []
    testSet = []
    with open(filename, 'rb') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset) - 1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])
    return trainingSet, testSet


def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow(instance1[x] - instance2[x], 2)
    return math.sqrt(distance)


def getNeighbors(trainingSet,testInstance,k):
    distance = []
    length = len(testInstance) - 1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance,trainingSet[x],length)
        distance.append(trainingSet[x],dist)
    # 正向排序
    distance.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distance[x][0])
    return neighbors

def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedVotes[0][0]

if __name__ == "__main__":
    trainingSet, testSet = loadDataSet("irisdata.txt", ",")
    print trainingSet
