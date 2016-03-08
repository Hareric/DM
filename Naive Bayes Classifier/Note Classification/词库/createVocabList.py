#coding=utf-8
'''
Author = Eric Chan
Create_Time = 2015/12/1
'''

import time
def loadData(filename,startNum,endNum,u=0): #输入读取的文件
    t1 = time.time()
    print "开始读取数据集..."

    file1 = open(filename,'r')
    line = file1.readline()
    messageList = [] #记录短信的列表
    classVec = [] #记录短信对应的属性, 1 代表垃圾短信 0 代表普通短信
    for i in range(startNum):
        line = file1.readline()
    for i in range(endNum):
        temp = line.split('\t')
        classVec.append(int(temp[1-u]))
        messageList.append(list(jieba.cut(temp[2-u])))
        line = file1.readline()
    file1.close()

    t2 = time.time()
    print "读取完毕,花费时间:%is\n"%(t2-t1)

    return messageList,classVec

def createVocabList(messageList):#创建一个词库,包含全部训练集中的所有词语
    t1 = time.time()
    print "开始构建词库..."

    vocabSet = set([])
    for i in messageList:
        vocabSet = vocabSet | set(i)

    t2 = time.time()
    print "词库构建完毕,花费时间:%is\n"%(t2-t1)
    return list(vocabSet)