"""
Created on Tue Jan 29 12:37:06 2019

@author: mai
"""

import numpy as np
import os
import KNN
 
def img2vector(filename): 
    """函数将以文本格式出现的32*32的0-1图片，转变成一维特征数组，返回一维数组
    
    Keyword argument:
    filename -- 文本格式的图片文件
    """
    
    imgvect = np.zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        linestr = fr.readline()
        for j in range(32):
            imgvect[0, 32*i + j] = int(linestr[j])
    return imgvect

def handwriteClassfiy(testfile, trainfile, k):
    """函数将trainfile中的文本图片转换成样本特征集和样本类型集，用testfile中的测试样本测试，无返回值
    
    Keyword argument:
    testfile -- 测试图片目录
    trainfile -- 样本图片目录
    """
    
    trainFileList = os.listdir(trainfile)
    trainFileSize = len(trainFileList)
    labels = []
    trainDataSet = np.zeros((trainFileSize, 1024))
    for i in range(trainFileSize):
        filenameStr = trainFileList[i]
        digitnameStr = filenameStr.split('.')[0]
        digitLabels = digitnameStr.split('_')[0]
        labels.append(digitLabels)
        trainDataSet[i, :] = img2vector(trainfile + '/' + filenameStr)
    #testFileList = os.listdir(testfile)
    #testNumber = len(testFileList)
    #errorcount = 0.0
    #for testname in testFileList:
    #testname='%s.txt'%str(num)
    testdigit = img2vector(testfile + '/' + 'x.txt')
    classifyresult = KNN.classify(testdigit, trainDataSet, labels, k)
    #testStr = testname.split('.')[0]
    #testDigitLabel = testStr.split('_')[0]
        #if classifyresult != testDigitLabel:
            #errorcount += 1.0
    #print(classifyresult)
        #print('this test real digit is：%s, and the result is: %s' % (testDigitLabel, classifyresult))
    #print('k = %d, errorRatio is: %f' % (k, errorcount/float(testNumber)))
    return classifyresult
 
if __name__=='__main__':
    filename = '/home/mai/test/trainingDigits/0_0.txt'
    traindir= '/home/mai/test/mytrain'
    testdir = '/home/mai/test/mydigits'
    handwriteClassfiy(testdir, traindir, 3)
