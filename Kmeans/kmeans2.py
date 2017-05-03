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
        fltline = map(float, curLine)
        dataMat.append(fltline)
    return dataMat


def distEclud(vecA,vecB):
    return sqrt(power(vecA - vecB,2))


if __name__ == "__main__":
    print(loadDataSet('testSet.txt'))
