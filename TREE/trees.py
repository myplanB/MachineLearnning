# encoding:utf-8

from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import preprocessing
from sklearn import tree
from sklearn.externals.six import StringIO


def readDataFromCSV():
    allElectronicsData = open("AllElectronics.csv")
    reader = csv.reader(allElectronicsData)
    headers = reader.next()
    print headers

    featureList = []
    labelList = []
    for row in reader:
        labelList.append(row[len(row) - 1])
        rowDict = {}
        for i in range(1, len(row) - 1):
            rowDict[headers[i]] = row[i]
        featureList.append(rowDict)
    print featureList

    vec = DictVectorizer()  # 字典向量化
    dummyX = vec.fit_transform(featureList).toarray()

    print "dummyX:" + str(dummyX)
    print (vec.get_feature_names())
    print "labellist:" + str(labelList)

    lb = preprocessing.LabelBinarizer
    dummyY = lb.fit_transform(labelList)
    print "dummyY:" + str(dummyY)


if __name__ == '__main__':
    readDataFromCSV()
