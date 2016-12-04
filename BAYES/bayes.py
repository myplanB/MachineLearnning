# encoding:utf-8
from numpy import zeros


def loadDataSet():
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]  # 1 is abusive, 0 not
    return postingList, classVec


# 创建一个空集用来对数据集去重
def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet |= set(document)
    return list(vocabSet)


# 将输入数据集按照结果数值化
def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print "the word :%s is not in my Vocabulary!" % word
    return returnVec


# trainMatrix 数值化处理后的全量数据集
# trainCategory 训练集的分类结果
# 计算出p(w|c1)和p(w|c0)
def trainNBO(trainMatrix, trainCategory):
    # 定义每行为文档
    numTrainDocs = len(trainMatrix)
    # 获取文档中含有的单词数
    numWords = len(trainMatrix[0])
    # p(w)含有侮辱语言的概率
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    p0Num = zeros(numWords)
    p1Num = zeros(numWords)
    p0Denom = 0.0
    p1Denom = 0.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = p1Num / p1Denom
    p0Vect = p0Num / p0Denom
    return p0Vect, p1Vect, pAbusive


if __name__ == "__main__":
    trainMat = []
    dataSet, classVec = loadDataSet()
    # 去重数据
    uniqueData = createVocabList(dataSet)
    for doc in dataSet:
        # 数值化数据数组
        trainMat.append(setOfWords2Vec(uniqueData, doc))
    p0Vect, p1Vect, pAbusive = trainNBO(trainMat, classVec)
    print p0Vect
    print "\n"
    print p1Vect
    print "\n"
    print pAbusive
