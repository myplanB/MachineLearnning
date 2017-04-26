#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/26 15:15
# @Author  : Sonny
# @Site    : 
# @File    : recommend.py
# @Software: PyCharm Community Edition

from sklearn import svm
from sklearn import datasets

iris = datasets.load_iris()
clf = svm.SVC()
X,Y = iris.data,iris.target
clf.fit(X,Y)

import pickle
s = pickle.dumps(clf)
clf2 = pickle.loads(s)