#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@version: latest
@author: sonny
@license: Apache Licence 
@contact: 71567636@qq.com
@site: 
@software: PyCharm
@file: logRegres.py
@time: 2017/5/5 16:19
"""
from LOGISTIC.gradientUP import stocGradAscentRandom
from LOGISTIC.logistic import sigmod
from numpy import *

def classifyVector(inX,weights):
    prob = sigmod(sum(inX*weights))
    if prob > 0.5:
        return 1.0
    else:
        return 0.0

def colicTest():
    frTrain = open('horseColicTraining.txt','r')
    frTest = open('horseColicTest.txt','r')
    trainingSet = []
    trainingLabel = []
    for line in frTrain.readlines():
        # 数组
        currLine = line.strip().split("\t")
        lineArr = []
        # 21为每条记录的列数
        for i in range(21):
            lineArr.append(float(currLine[i]))
        trainingSet.append(lineArr)
        # 每条记录的最后最后一行为标识符
        trainingLabel.append(float(currLine[-1]))

    trainWeights = stocGradAscentRandom(trainingSet,trainingLabel,500)
    errorCount = 0
    numTestVec = 0
    for line in frTest.readlines():
        numTestVec += 1.0
        currLine = line.strip().split("\t")
        lineArr = []
        for i in range(21):
            lineArr.append(currLine[i])
        if int(classifyVector(array(lineArr),trainWeights)) != int(currLine[-1]):
            errorCount += 1
    errorRate = float(errorCount) / numTestVec
    print ("the error rate of this test is : %f" %errorRate)
    return errorRate

def muliTest():
    numTests = 10
    errorSum = 0.0
    for k in range(numTests):
        errorSum += colicTest()
    print("after %d iterations the average error rate is :%f" % (numTests,errorSum/float(numTests)))

if __name__ == "__main__":
    muliTest()