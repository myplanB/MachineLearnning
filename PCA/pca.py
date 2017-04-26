"""
@version: latest
@author: sonny
@license: Apache Licence 
@contact: 715676363@qq.com
@site: 
@software: PyCharm Community Edition
@file: pca.py
@time: 2017/4/26 22:24
"""
from numpy import *
import matplotlib.pyplot as plt

def loadDataSet(fileName, delim="\t"):
    fr = open(fileName)
    stringArr = [line.strip().split(delim) for line in fr.readlines()]
    datArr = [map(float,line) for line in stringArr]
    return mat(datArr)

def pca(dataMat,topNfeat=9999999):
    meanVals = mean(dataMat,axis=0)
    meanRemoved = dataMat - meanVals
    convMat = cov(meanRemoved,rowvar=0)
    eigVals,eigVects = linalg.eig(mat(convMat))
    eigValInd = argsort(eigVals)
    eigValInd = eigValInd[:-(topNfeat+1):-1]
    redEigVects = eigVects[:,eigValInd]
    lowDDataMat = meanRemoved * redEigVects
    reconMat = (lowDDataMat * redEigVects.T) + meanVals
    return lowDDataMat,reconMat

if __name__ == "__main__":
    dataMat = loadDataSet("testSet.txt")
    lowDMat,reconMat = pca(dataMat,1)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(dataMat[:,0].flatten().A[0],reconMat[:,1].flatten().A[0],marker='o',s=50,c='red')
    plt.show()