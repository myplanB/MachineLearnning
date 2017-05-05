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
import csv
from sklearn import preprocessing, tree
from sklearn.feature_extraction import DictVectorizer

if __name__ == '__main__':
    allElectronicsData = open("AllElectronics.csv")
    reader = csv.reader(allElectronicsData)
    # 获取表格的表头
    headers = reader.next()
    print (headers)

    # 特征列表
    featureList = []
    # 标签列表
    labelList = []

    for row in reader:
        # 标签元素存储标签列表
        labelList.append(row[-1])
        rowDict = {}
        for i in range(1,len(row)-1):
            print (row[i])
            rowDict[headers[i]] = row[i]
        featureList.append(rowDict)
    print ("featureList:{0}".format(featureList))
    print ("labelList:{0}".format(labelList))

    vec = DictVectorizer()
    # 转换成矩阵
    dummyX = vec.fit_transform(featureList).toarray()
    print ("dummyX:{0}".format(dummyX))
    print (vec.get_feature_names())

    # 转换成二进制标签化
    lb = preprocessing.LabelBinarizer()
    dummyY = lb.fit_transform(labelList)
    print ("dummyY:{0}".format(dummyY))

    clf = tree.DecisionTreeClassifier(criterion='entropy')
    clf = clf.fit(dummyX,dummyY)
    print ("clf:"+str(clf))

    with open("iris.dot", 'w') as f:
        f = tree.export_graphviz(clf, out_file=f)

