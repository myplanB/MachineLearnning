#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: sonny
@license: Apache Licence 
@contact: 715676363@qq.com
@site: 
@software: PyCharm
@file: sk_logistc.py
@time: 2016/12/13 22:26
"""
import numpy as np
import random

# x,y 为
# m 为向量个数
def gradientDescent(x,y,thera,alpha,m,numIterations):
    # 转置
    xTrans = x.transpose()
    # 迭代次数
    for i in xrange(0,numIterations):
        # 参数模型
        hypothesis = np.dot(x,thera)
        # 残差
        loss = hypothesis - y
        # cost函数
        cost = np.sum(loss**2)/(2*m)
        print ("Iteration %d| Cost: %f" % (i,cost))

        # 梯度下降核心
        gradient = np.dot(xTrans,loss)/ m
        thera = thera - alpha * gradient
    return thera

# numPoints   实例数
# bias        偏好值
# variance    方差
def loadData(numPoints,bias,variance):
    # 生成numPoints 行 2列的二维数组
    x = np.zeros(shape=(numPoints,2))
    # 生成 numPoints 行 1列的二维数组
    y = np.zeros(shape=numPoints)
    for i in xrange(0,numPoints):
        x[i][0] = 1
        x[i][1] = i
        # uniform 指定范围的随机数
        y[i] = (i+bias) + random.uniform(0,1)*variance
    return x,y

if __name__=="__main__":
    x,y = loadData(100, 25, 10)
    m,n = np.shape(x)
    print m
    print n

    numIterations = 100000
    alpha = 0.0005
    theta = np.ones(n)
    theta = gradientDescent(x,y,theta,alpha,m,numIterations)
    print theta

#思路：
# 第一步：先生成模拟数据，行数相同

# 第二步：