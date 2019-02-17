#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 22:46:30 2019

@author: mai
"""

import operator
import numpy as np
 
def createdataset():
    """该函数用于产生kNN实验用列,返回样本数据集（numpy数组）和样本类型集（列表）
    
    Keyword arguments:
    None
    """
    group = np.array([[1.0, 1.1], 
                      [1.0, 1.0],
                      [0, 0], 
                      [0, 0.1]
                      ])
    labels = ['A', 'A', 'B', 'B']
    return group, labels
 
def classify(testData, dataSet, labels, k):
    """应用KNN方法对测试点进行分类，返回一个结果类型
    
    Keyword argument:
    testData: 待测试点，格式为数组
    dataSet： 训练样本集合，格式为矩阵
    k： 近邻点数
    """
    dataSetSize = dataSet.shape[0]
    multitestData = np.tile(testData, (dataSetSize, 1))
    diffMat = multitestData - dataSet
    sqdiffMat = diffMat**2
    sqdistance = sqdiffMat.sum(axis=1)
    #print(sqdistance)
    distance = sqdistance**0.5
    sortedDistIndex = distance.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndex[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    #print(sortedClassCount)
    return sortedClassCount[0][0]
 
 
if __name__ == '__main__':
    import matplotlib.pyplot as plt
    group, labels = createdataset()
    print('group is:')
    print(group)
    print(labels)
    plt.plot(group[:, 0], group[:, 1], 'o')
    plt.xlim(-0.1, 1.2)
    plt.ylim(-0.1, 1.2)
    plt.show()
    test = [0, 0]
    print('test is:')
    print(test)
    print('classify result is:')
    print(classify(test, group, labels, 3))