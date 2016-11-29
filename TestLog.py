# _*_ coding:utf-8 _*_

import math
import matplotlib.pyplot as plt
import numpy as np

def plotsin():
    x = np.arange(0, 5, 0.1);
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()

def plotimg():
    x = [float(i) / 100.0 for i in range(1, 300)]
    y = [math.log(i) for i in x]
    plt.plot(x, y, 'r-', linewidth=3, label="log Curve")
    # a取值两个点
    a = [x[20], x[175]]
    # b取值两个点
    b = [y[20], y[175]]

    plt.plot(a, b, 'g-', linewidth=2, label="line")
    plt.plot(a, b, markersize=15, alpha=0.75)
    plt.legend(loc='upper left')
    # 显示网格
    plt.grid(True)
    # x坐标上标签
    plt.xlabel('x')
    # y坐标上标签
    plt.ylabel('log(x)')
    plt.show()

if __name__ == "__main__":
    plotsin()