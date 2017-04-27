#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/27 17:38
# @Author  : Sonny
# @Site    : 
# @File    : test.py
# @Software: PyCharm Community Edition

if __name__ == "__main__":
    maps = {'y': 3, 'x': 4, 's': 3, 'z': 5, 't': 3}
    result = [v for v in sorted(maps.items(),key=lambda p:p[1],reverse=True)]

    arr = ['z', 'x', 'y', 's', 't']
    for i in range(len(arr)):
        print arr[1::]