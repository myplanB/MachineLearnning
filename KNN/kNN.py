# encoding:utf-8
from _ast import operator

from numpy import *
import operator
import matplotlib.pyplot as plt


def createDataSet():
    group = array([
        [1.0, 1.1],
        [1.0, 1.0],
        [0, 0],
        [0, 0.1]
    ])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(inX, dataSet, labels, k):
    # 获取行数
    dataSetSize = dataSet.shape[0]
    # 残差矩阵
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    # 按行求和
    sqDistances = sqDiffMat.sum(axis=1)
    # 取平方
    distances = sqDistances ** 0.5
    # 返回从小到大的序数
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        votelabel = labels[sortedDistIndicies[i]]
        # 对待检测的数据的相似度进行计算排序操作
        classCount[votelabel] = classCount.get(votelabel, 0) + 1
    # 按照矩阵第二列进行排序，逆序排列
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    # 结果取值[('B',2),('A',1)]
    return sortedClassCount[0][0]


# 将文件内的数据转化为矩阵
def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0
    fr = open(filename)
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split("\t")
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector


# 数据归一化处理
def autoNorm(dataSet):
    # 按列求取最大值和最小值，返回列向量
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet / tile(ranges, (m, 1))
    return normDataSet, ranges, minVals

def datingClassTest():
    hoRatio = 0.10
    datingDataMat,datingLabels = file2matrix("datingTestSet2.txt")
    normMat,ranges,minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVercs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVercs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVercs:m,:],datingLabels[numTestVercs:m,:],3)


if __name__ == "__main__":
    datingDataMat, datingLabels = file2matrix("datingTestSet2.txt")
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # ax.scatter(datingDataMat[:,1],datingDataMat[:,2])
    # plt.show()
    normDataSet, ranges, minVals = autoNorm(datingDataMat)
    print normDataSet
    print ranges
    print minVals
