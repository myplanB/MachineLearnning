# encoding:utf-8

from math import log
import operator
import matplotlib.pyplot as plt


# 创建数据集和标签列表
def createDataSet():
    dataSet = [
        [1, 1, 'yes'],
        [1, 1, 'yes'],
        [1, 0, 'no'],
        [0, 1, 'no'],
        [0, 1, 'no']
    ]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels


# 根据最终条件（结果）计算香浓熵
def calcShannonEnt(dataSet):
    # 数组长度
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            # 对字典进行初始化
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    # 进行香浓定理计算
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


# 划分数据集
# axis 特征向量
# value 返回的特征向量
# 对数据集按照不同的规则进行分类
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet


# 选择最好的划分方式
def chooseBestFeatureToSplit(dataSet):
    # 排除最后一列的结果列，计算前n-1列的矩阵宽带值
    numFeature = len(dataSet[0]) - 1
    # 计算香农定理
    baseEntropy = calcShannonEnt(dataSet)
    baseInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeature):
        # 特征列表，按列提取
        featList = [example[i] for example in dataSet]
        # 去重
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            # 按照特征进行分类，提取子数据集
            subDataSet = splitDataSet(dataSet, i, value)
            # 计算信息熵
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        # 计算信息增益
        infoGain = baseEntropy - newEntropy
        if infoGain > baseInfoGain:
            baseInfoGain = infoGain
            bestFeature = i
    return bestFeature


# 递归构建决策树
# 本方法是依据最后一列的结果进行分类统计并按照倒叙排列，返回出现次数最多的分类名称
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount += 1
        # 按照第二列进行倒叙排列
        sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


# 创建树结构
def createTree(dataSet, labels):
    # 结果列表
    classList = [example[-1] for example in dataSet]
    # count 用于统计某个元素在列表中出现的次数，如果分类列表的长度与列表中第一个元素在列表中出现次数相等
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        # 计算出最接近的类别
        return majorityCnt(classList)
    # chooseBestFeatureToSplit返回的是特征序数，即：第几列特征值的序数
    bestFeat = chooseBestFeatureToSplit(dataSet)
    # 选取最好的特征标签值
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel: {}}
    # 删除最佳特征标签
    del (labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        # 递归调用计算子树
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree


# 首先选择根节点，然后遍历子节点，计算叶节点个数
def getNumLeaf(mytree):
    numLeafs = 0
    # 获取根节点
    rootStr = mytree.keys()[0]
    # 获取子节点
    childDict = mytree[rootStr]
    for key in childDict.keys():
        if type(childDict[key]).__name__ == 'dict':
            numLeafs += getNumLeaf(childDict[key])
        else:
            numLeafs += 1
    return numLeafs


# 首先选择根节点，然后遍历子节点，计算树的深度
def getTreeDepth(mytree):
    maxDepth = 0
    # 获取根节点
    rootStr = mytree.keys()[0]
    # 子节点
    childDict = mytree[rootStr]
    for key in childDict.keys():
        if type(childDict[key]).__name__ == 'dict':
            currentDepth = 1 + getTreeDepth(childDict[key])
        else:
            currentDepth = 1
        if currentDepth > maxDepth:
            maxDepth = currentDepth
    return maxDepth


if __name__ == "__main__":
    # dataSet, labels = createDataSet()
    # print calcShannonEnt(dataSet)
    # print chooseBestFeatureToSplit(dataSet)
    # str = {'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}
    # print createTree(dataSet,labels)
    fr = open('lenses.txt')
    lenses = [inst.strip().split("++") for inst in fr.readlines()]
    labels = ['age','prescript','astgmatic','tearRate']
    lensesTree = createTree(lenses,labels)
    print(lensesTree)