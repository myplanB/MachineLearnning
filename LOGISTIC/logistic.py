# encoding:utf-8

def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split("\t")
        dataMat.append([1.0,float(lineArr[1]),float(lineArr[2])])
        labelMat.append(int(lineArr[-1]))
    return dataMat,labelMat

if __name__ == "__main__":
    dataMat, labelMat = loadDataSet()
    print dataMat
    print "\n"
    print labelMat
