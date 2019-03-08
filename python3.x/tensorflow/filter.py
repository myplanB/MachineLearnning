#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   sonny

@License :   (C) Copyright 2018-2019, sonny

@Contact :   715676363@qq.com

@Software:   PyCharm

@File    :   filter.py

@Time    :   3/8/2019 11:42 PM

@Desc    :

'''

import cv2
import numpy as np
import tensorflow as tf
...

if __name__ == '__main__':
    img = cv2.imread('timg.jpg')
    h,w,c = np.shape(img)
    # -1的含义是在此维度上可以是任意数
    img = np.reshape(img,[-1,h,w,c])

    # 卷积核心 [ks1,ks2,c1,c2]
    kernal_np = np.zeros([4,4,3,3])
    kernal_np[:,:,0,0] = 1/16
    kernal_np[:,:,0,1] = 1/16
    kernal_np[:,:,0,2] = 1/16

    img_tf = tf.constant(img,dtype=tf.float32)
    knl_tf = tf.constant(kernal_np,dtype=tf.float32)

    #  out：[1,H,W,C]
    out_tf = tf.nn.conv2d(
        img_tf,  # [B,H,W,C]
        knl_tf,  # 自定义的卷积核心
        strides=[1,1,1,1],
        padding='SAME'
    )

    sess = tf.Session()
    out = sess.run(out_tf)  # [1,H,W,C]

    cv2.namedWindow("w")
    cv2.imshow('w',out[0])
    cv2.waitKey(0)