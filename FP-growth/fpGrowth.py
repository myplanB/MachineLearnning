#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/27 15:08
# @Author  : Sonny
# @Site    : 
# @File    : fpGrowth.py
# @Software: PyCharm Community Edition

def loadSimpDat():
    simDat = [
        ['r', 'z', 'h', 'j', 'p'],
        ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
        ['r', 'x', 'n', 'o', 's'],
        ['z'],
        ['y', 'r', 'x', 'z', 'q', 't', 'p'],
        ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']
    ]
    return simDat


def createInitSet(dataSet):
    retDict = {}
    for trans in dataSet:
        retDict[frozenset(trans)] = 1
    return retDict


class treeNode:
    def __init__(self, nameValue, numOccur, parentNode):
        # 名称
        self.name = nameValue
        # 计数
        self.count = numOccur
        # 链接
        self.nodeLink = None
        # 父类节点
        self.parent = parentNode
        # 子节点
        self.children = {}

    def inc(self, numOccur):
        self.count += numOccur

    def disp(self, ind=1):
        print '  ' * ind, self.name, '  ', self.count
        for child in self.children.values():
            child.disp(ind + 1)


#
def updateHeader(nodeTest, targetNode):
    while (nodeTest.nodeLink != None):
        nodeTest = nodeTest.nodeLink
    nodeTest.nodeLink = targetNode


def updateTree(items, inTree, headerTable, count):
    if items[0] in inTree.children:
        inTree.children[items[0]].inc(count)
    else:
        inTree.children[items[0]] = treeNode(items[0], count, inTree)
        if headerTable[items[0]][1] == None:
            headerTable[items[0]][1] = inTree.children[items[0]]
        else:
            updateHeader(headerTable[items[0]][1], inTree.children[items[0]])
    if len(items) > 1:
        # 每次调用就会删除items中的一个元素
        updateTree(items[1::], inTree.children[items[0]], headerTable, count)


def createTree(dataSet, minSup=1):
    headerTable = {}
    for trans in dataSet:
        for item in trans:
            # 对每个字母计数
            headerTable[item] = headerTable.get(item, 0) + dataSet[trans]
    # 使用阈值将不符合要求的字母去掉
    for k in headerTable.keys():
        if headerTable[k] < minSup:
            del (headerTable[k])
    # 取出字典的键值
    freqItemzSet = set(headerTable.keys())
    # 判断如果全部删除字母，则集合不符合要求
    if len(freqItemzSet) == 0:
        return None, None
    # 遍历字符集合（去掉不符合条件的）
    for k in headerTable:
        headerTable[k] = [headerTable[k], None]
    # 根树节点
    retTree = treeNode('Null Set', 1, None)
    # 遍历原始数据集合
    for tranSet, count in dataSet.items():
        localID = {}
        for item in tranSet:
            if item in freqItemzSet:  # freqItemzSet 满足条件的元素数组
                localID[item] = headerTable[item][0]
        if len(localID) > 0:
            # sorted 返回的数据v是一个tuple数组
            orderedItem = [v[0] for v in sorted(localID.items(), key=lambda p: p[1], reverse=True)]
            # orderedItem 是localID 按照value倒序排列的key数组, retTree是根节点，headerTable是原始数据的字典结构,count是dataSet字典结构的value值
            updateTree(orderedItem, retTree, headerTable, count)
    return retTree, headerTable

# 迭代上溯整个树
def ascendTree(leafNode, prefixPath):
    if leafNode.parent is not None:
        prefixPath.append(leafNode.name)
        ascendTree(leafNode.parent, prefixPath)

# 查找前缀节点
def findPrefixpath(basepat, treeNode):
    condPats = {}
    while treeNode is not None:
        prefixPath = []
        ascendTree(treeNode, prefixPath)
        if len(prefixPath) > 1:
            condPats[frozenset(prefixPath[1:])] = treeNode.count
        treeNode = treeNode.nodeLink
    return condPats


if __name__ == "__main__":
    dataSet = loadSimpDat()
    initSet = createInitSet(dataSet)
    myTree, myHeadertab = createTree(initSet, 3)
    myTree.disp()

    print findPrefixpath('x',myHeadertab['x'][1])
