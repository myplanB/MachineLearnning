# encoding:utf-8

from math import log


# 创建数据集
import operator


def createDataSet():
    dataSet = [
        [1, 1, 'yes'],
        [1, 1, 'yes'],
        [1, 0, 'no'],
        [0, 1, 'no'],
        [0, 1, 'no']
    ]
    return dataSet


# 根据最终条件（结果）计算香浓熵
def calcShannonEnt(dataSet):
    # 数组长度
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            # 首先对字典进行初始化
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


# 划分数据集
# axis 特征向量
# value 返回的特征向量
def splitData(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet


# 选择最好的划分方式
def chooseBestFeatureToSplit(dataSet):
    # 排除最后一列的结果列
    numFeature = len(dataSet[0]) - 1
    # 计算香农定理
    baseEntropy = calcShannonEnt(dataSet)
    baseInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeature):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitData(dataSet,i,value)
            prob = len(subDataSet)/float(len(subDataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if (infoGain > baseInfoGain):
            baseInfoGain = infoGain
            bestFeature = i
    return bestFeature

# 递归构建决策树
#本方法是依据最后一列的结果进行分类统计并按照倒叙排列，返回出现次数较多的分类名称
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount += 1
        # 按照第二列进行倒叙排列
        sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def createTree():
    pass

if __name__ == "__main__":
    dataSet = createDataSet()
    # print calcShannonEnt(dataSet)
    print chooseBestFeatureToSplit(dataSet)
