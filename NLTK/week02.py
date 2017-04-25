#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/25 9:55
# @Author  : sonny
# @Site    : 
# @File    : week02.py
# @Software: PyCharm
import nltk

nltk.download()

from nltk.book import *

# 搜索文本
# 搜索单词
text1.concordance("monstrous")
text2.concordance("affection")
text3.concordance("lived")
text4.concordance("lol")

#搜索共同上下文
text2.common_contexts(["citizens","democracy"])

#词汇分布图
text4.dispersion_plot(["monstrous","very"])

#自动生成文章
text3.generate(["monstrous","very"])

#计数词汇
len(text3)

sorted(set(text3))

#重复词密度
# from __future__ import division
len(text3)/len(set(text3))

# 关键词密度
text3.count("smote")

100 * text4.count("a")/len(text4)

def lexical_diversity(text):
    return len(text)/len(set(text))

def percentage(count,total):
    return 100 *count/total

###词链表
sent1 = ['call','me','Ishmael',',']

# 链接join
sent3+sent4

# append
sent4.append("some")

# index
text4.index("awaken")

#频率分布
fdist1 = FreqDist(text1)
fdist1

# 最常出现的50个词语
fdist1.plot(50,cumulative=True)

#获取低频词
fdist1.hapaxes()

# 细粒度选择词
v = set(text1)

long_words = [w for w in v if len(w) > 15]

v = set(text5)
long_words = [w for w in v if len(w) > 15]
sorted(long_words)
