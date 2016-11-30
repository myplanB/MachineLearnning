# encoding:utf-8
from _ast import operator

from numpy import *
import operator


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


def file2matrix(filename):
    fr = open(filename)
    arrayLines = fr.readlines()
    numberOfLines = len(arrayLines)
    returnMat = zeros((numberOfLines,3))
    print returnMat


if __name__ == "__main__":
    group, labels = createDataSet()
    print classify0([0, 0], group, labels, 3)
