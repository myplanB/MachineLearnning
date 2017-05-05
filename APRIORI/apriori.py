#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/28 10:03
# @Author  : Sonny
# @Site    : 
# @File    : apriori.py
# @Software: PyCharm Community Edition

def loadDataSet():
    return [
        [1, 3, 5],
        [2, 3, 4],
        [1, 2, 3, 5],
        [2, 5]
    ]


# 创建一阶频繁集
def createC1(dataset):
    C1 = []
    for transaction in dataset:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    return map(frozenset, C1)


# D 数据集
# Ck 候选项列表
# minSupport 最小支持度
def scanD(D, Ck, minSupport):
    ssCnt = {}
    for tid in D:
        for can in Ck:
            if can.issubset(can):
                if not ssCnt.has_key(can):
                    ssCnt[can] = 1
                else:
                    ssCnt[can] += 1
    # 计算数据集合的大小
    numItems = float(len(D))
    retList = []
    # 支持的数据集合
    supportData = {}
    # 计算支持度
    for key in ssCnt:
        support = ssCnt[key] / numItems
        if support >= minSupport:
            # insert(index,key)始终在index之前插入key值
            retList.insert(0, key)
        supportData[key] = support
    # 返回retlist属于商品信息，以及商品对应的支持度
    return retList, support


# Lk 频繁项集列表和个数
def aprioriGen(Lk, k):
    retList = []
    lenLk = len(Lk)
    # 产生不重复的数据子集
    for i in range(lenLk):
        for j in range(i + 1, lenLk):
            L1 = list(Lk[i])[:k - 2]
            L2 = list(Lk[j])[:k - 2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                retList.append(Lk[i] | Lk[j])
    return retList


def apriori(dataSet, minSupport=0.5):
    C1 = createC1(dataSet)
    D = map(set, dataSet)
    L1, supportData = scanD(D, C1, minSupport)
    L = [L1]
    k = 2
    while (len(L[k - 2]) > 0):
        Ck = aprioriGen(L[k - 2], k)
        Lk, supK = scanD(D, Ck, minSupport)
        supportData.update(supK)
        k += 1
    return L, supportData

def calcConf(freqSet,H,supportData,brl,minConf=0.7):
    prunedH = []
    for conseq in H:
        conf = supportData[freqSet] / supportData[freqSet - conseq]
        if conf >= minConf:
            print freqSet-conseq,'-->',conseq,'conf:',conf
            brl.append((freqSet-conseq,conseq,conf))
            prunedH.append(conseq)
    return prunedH

def rulesFromConseq(freqSet,H,supportData,brl,minConf = 0.7):
    m = len(H[0])
    if(len(freqSet) > (m+1)):
        Hmp1 = aprioriGen(H,m+1)
        Hmp1 = calcConf(freqSet,Hmp1,supportData,brl,minConf)
        if (len(Hmp1) > 1):
            rulesFromConseq(freqSet, H, supportData, brl, minConf)

def generdateRules(L,supportData,minConf=0.7):
    bigRuleList = []
    for i in range(1,len(L)):
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in freqSet]
            if(i > 1):
                rulesFromConseq(freqSet,H1,supportData,bigRuleList)
            else:
                calcConf(freqSet,H1,supportData,bigRuleList,minConf)
    return bigRuleList

if __name__ == "__main__":
    dataSet = loadDataSet()
    L,supportData = apriori(dataSet,minSupport=0.5)
