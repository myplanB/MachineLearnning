# encoding:utf-8
import random


def loadData(filename):
    dataMat = []
    labelMat = []
    fr = open(filename)
    for line in fr.readlines():
        lineArr = line.strip().split("\t")
        dataMat.append([float(lineArr[0]), float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat, labelMat


def selectJrand(i, m):
    j = i
    while (j == i):
        j = int(random.uniform(0, m))
    return j


def clipAlpha(aj,H,L):
    if aj > H:
        aj = H
    if aj < L:
        aj = L
    return aj

if __name__ == "__main__":
    dataMat, labelMat = loadData("testSet.txt")
    print dataMat
