#coding=utf-8
'''
Author = Eric_Chan
Create_Time = 2015/11/29
'''
import jieba
import numpy as np
import time
import sys
from multiprocessing import Process,Queue
jieba.initialize()
time.sleep(1)

def loadData(filename,startNum,count,u=0): #输入读取的文件
    t1 = time.time()
    print "开始读取数据集..."

    file1 = open(filename,'r')
    line = file1.readline()
    messageList = [] #记录短信的列表
    classVec = [] #记录短信对应的属性, 1 代表垃圾短信 0 代表普通短信
    for i in range(startNum):
        line = file1.readline()
    for i in range(count):
        temp = line.split('\t')
        classVec.append(int(temp[1-u]))
        messageList.append(list(jieba.cut(temp[2-u])))
        line = file1.readline()
    file1.close()

    t2 = time.time()
    print "读取完毕,花费时间:%is\n"%(t2-t1)

    return messageList,classVec


def createVecInVocabList(message,vocabList):#输入一条短信,返回该短信基于某词库的向量
    returnVec = [0] * len(vocabList)
    for word in message:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
    return returnVec

def getNBO(): #获得贝叶斯分类器
    sumNum = float(open("finished.txt",'r').readline())
    p0Num = np.loadtxt("P0NUM.txt")
    p1Num = np.loadtxt("P1NUM.txt")
    f = open("datasave.txt",'r')
    nSpam = int(f.readline())
    p0Denom = float(f.readline())
    p1Denom = float(f.readline())
    f.close()
    p1Vect = np.log(p1Num / p1Denom)
    p0Vect = np.log(p0Num / p0Denom)
    # pSpam = 0.000000000000001  #垃圾短信查全率:1 总分0.91
    # pSpam = 0.00001 #垃圾短信查全率 0.993 总分0.981
    pSpam = 0.1
    '''
    pSpam = 0.000001
    垃圾短信准确率: 0.957537154989
    垃圾短信查全率: 0.997787610619
    正确短信准确率: 0.999779200707
    正确短信查全率: 0.995602462621
    总分: 0.979632572835
    '''
    return p0Vect,p1Vect,pSpam


def classifyNB(messageVec,p0Vec,p1Vec,pSpam):#输入 短信向量 普通短信的词语向量概率 垃圾短信的词语向量概率 垃圾短信出现的概率
    p0 = sum(messageVec * p0Vec) + np.log(1-pSpam)
    p1 = sum(messageVec * p1Vec) + np.log(pSpam)
    if p1 > p0:
        return 1
    else:return 0

def createMatrix(messageList,vocabList):#输入短信列表和词库 返回短信-短信向量矩阵
    t1 = time.time()
    print "开始构建向量矩阵..."

    num = len(messageList)
    n = num/3
    def Pro(N1,N2,getReturn=None,isP=False):
        returnMatrix = []
        if isP:
            for i in range(num)[N1:N2]:
                # print "    构建中...   %i%%"%(i/float(n)*100),       #?
                print "    构建中...   %i%%"%(i/float(num)*100),       #??
                sys.stdout.write("\r")
                returnMatrix.append(createVecInVocabList(messageList[i],vocabList=vocabList))
        else:
            for i in range(num)[N1:N2]:
                returnMatrix.append(createVecInVocabList(messageList[i],vocabList=vocabList))
        # getReturn.put(returnMatrix)                                 #?
        return returnMatrix
    # getReturn1 = Queue();getReturn2 = Queue();getReturn3 = Queue()  #?
    # P1 = Process(target=Pro,args=(0,n,getReturn1,True))             #?
    # P2 = Process(target=Pro,args=(n,2*n,getReturn2))                #?
    # P3 = Process(target=Pro,args=(2*n,3*n,getReturn3))              #?
    # P1.start()                                                      #?
    # P2.start()                                                      #?
    # P3.start()                                                      #?
    # matrix = getReturn1.get() + getReturn2.get() + getReturn3.get() #?
    matrix = Pro(0,num,None,True)

    t2 = time.time()
    print "矩阵构建完毕,花费时间:%is\n"%(t2-t1)
    return matrix

def getTestScore(realList,resultList):#输入原始数据和判定数据,得出评估得分
    num = len(realList)
    A = 0.
    B = 0.
    C = 0.
    D = 0.
    for i in range(num):
        if realList[i]==resultList[i]:
            if realList[i] == 0:
                A += 1
            else:
                D += 1
        else:
            if realList[i] == 0:
                C += 1
            else:
                B += 1
    print "A:",A," B:",B," C:",C," D:",D
    print "垃圾短信准确率:",D/(B+D)
    print "垃圾短信查全率:",D/(C+D)
    print "正常短信准确率:",A/(A+C)
    print "正常短信查全率:",A/(A+B)
    print "总分:" ,0.7*(0.65*(D/(B+D))+0.35*(D/(C+D))) + 0.3*(0.65*(A/(A+C)) + 0.35*(A/(A+B)))

def writeResult(fileName,resultList,startNum):
    file1 = open(fileName,'a')
    for i in range(len(resultList)):
        xuhao = str(startNum + i + 1)
        file1.write(xuhao+','+str(resultList[i])+'\n')
    file1.close()


file1 = open("VocabList.txt",'r')
line = file1.readline()
vocabList = []
while line:
    vocabList.append(line.strip().decode('utf8'))
    line = file1.readline()
file1.close()
p0_vect,p1_vect,p_spam = getNBO()

def startClass(startNum,count): #输入 训练集的起点 和 训练集的个数
    "读取训练集"
    # test_message,test_vec = loadData("database/80W.txt",startNum,count)
    test_message,test_vec = loadData("database/20W.txt",startNum,count,1)


    "构建词库"
    # file1 = open("VocabList.txt",'r')
    # line = file1.readline()
    # vocabList = []
    # while line:
    #     vocabList.append(line.strip().decode('utf8'))
    #     line = file1.readline()
    # file1.close()


    "构建短信-向量矩阵"
    test_matrix = createMatrix(test_message,vocabList)

    "取得训练结束后的分类器"
    # p0_vect,p1_vect,p_spam = getNBO()

    "开始对数据集进行分类"
    t1 = time.time()
    print "开始进行分类..."
    test_result = []
    for i in range(len(test_matrix)):
        print "分类中...  %i%%"%(((i+1)/float(count))*100),
        sys.stdout.write('\r')
        test_result.append(classifyNB(test_matrix[i],p0_vect,p1_vect,p_spam))
    t2 = time.time()
    print "分类结束,花费时间:%is\n"%(t2-t1)

    '''测试结果'''
    # getTestScore(test_vec,test_result)

    return test_result

for i in range(2000):
    print "------------------------------"
    print "开始进行第%i次分类,剩余%i次"%((i+1),(1999-i))
    statrNum = i*100
    count = 100
    test_result = startClass(statrNum,count)
    writeResult("result/result2.txt",test_result,(800000+i*count))
    # time.sleep(60)
# startClass(710000,5000)
# startClass(720000,5000)
# startClass(730000,5000)
# startClass(740000,5000)
# startClass(750000,5000)