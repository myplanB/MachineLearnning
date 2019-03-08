#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   sonny

@License :   (C) Copyright 2018-2019, sonny

@Contact :   715676363@qq.com

@Software:   PyCharm

@File    :   embedding.py

@Time    :   3/9/2019 12:52 AM

@Desc    :

'''

import tensorflow as tf
import numpy as np

...

if __name__ == '__main__':
    # [B,T],[1,3],1个样本，样本里面是3个字
    input_data = tf.constant(
        [[1,2,3]]
    )
    # [字符个数，Embedding_size]
    w = tf.constant(np.ones([30,128]))

    # [B,T,embeddingSize]->[1,3,128]
    inputs = tf.nn.embedding_lookup(w,input_data)

    sess = tf.Session()
    print(sess.run(inputs))