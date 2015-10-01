#coding=utf-8
__author__ = 'Eric Chan'

import nltk
import chardet

def loadDataSet(): #导入垃圾邮件和正常邮件作为训练集
    test_list = []
    for i in range(21)[1:]:
        file1 = open(r'spam/%s.txt'%i)
        text = file1.read()
        code = chardet.detect(text)['encoding']
        text = text.decode(code).lower()
        words = nltk.word_tokenize(text)
        test_list.append(words)
        file1.close()

    for i in range(21)[1:]:
        file1 = open(r'ham/%s.txt'%i)
        text = file1.read()
        code = chardet.detect(text)['encoding']
        text = text.decode(code).lower()
        words = nltk.word_tokenize(text)
        test_list.append(words)
        file1.close()
    classVec = [1 for i in range(20)]
    classVec.extend([0 for j in range(20)])#1 代表垃圾邮件 0代表普通邮件
    return test_list,classVec

def createVocabList(dataSet):#创建词库
    vocabSet = set([])
    for i in dataSet:
        vocabSet = vocabSet | set(i) #取并集，消除重复集
    return list(vocabSet)

def createVector(unit,vocabList): #对每条邮件创建向量
    vector = [0]*len(vocabList)
    for i in unit:
        if i in vocabList:
            vector[vocabList.index(i)] = 1
        else:
            print "the word %s is not in my vocabList"%i
            continue
    return vector

def trainNBO(train_matrix,train_bool):
    train_num = len(train_matrix)
    words_num = len(train_matrix[0])
    sum_1 = [0 for i in range(words_num)]
    sum_0 = [0 for i in range(words_num)]
    _1_num = 0  #是垃圾邮件的邮件数
    _0_num = 0  #非垃圾邮件的邮件数
    for i in range(train_num):  #将训练矩阵向量进行相加
        if train_bool[i]==1:
            for j in range(words_num):
                sum_1[j] += train_matrix[i][j]
            _1_num = _1_num + 1

        if train_bool[i]==0:
            for j in range(words_num):
                sum_0[j] += train_matrix[i][j]
            _0_num = _0_num + 1

    print "正常邮件数：",_0_num," 垃圾邮件数：",_1_num
    p1Vect = [(float(sum_1[j])/_1_num) for j in range(words_num)]
    p0Vect = [(float(sum_0[j])/_0_num) for j in range(words_num)]
    p1 = float(_1_num)/train_num
    p0 = float(_0_num)/train_num

    return p1Vect,p0Vect,p1,p0
vocabList = []   #定义全局变量 创建词库
def createClassifier():
    mail_list,spam_bool = loadDataSet()
    global vocabList
    vocabList =  createVocabList(mail_list)
    vocabList.sort()

    train_matrix = [] #训练贝叶斯分类器的数据集  向量矩阵
    for i in range(len(mail_list)):
        train_matrix.append(createVector(mail_list[i],vocabList))

    return trainNBO(train_matrix,spam_bool)

def classing(p1Vect,p0Vect,P1,P0,unitVector):
    p1 = 1.
    p0 = 1.
    words_num = len(unitVector)
    for i in range(words_num):
        if unitVector[i]==1:
            p1 *= p1_vect[i]
            p0 *= p0_vect[i]
    p1 *= P1
    p0 *= P0
    if p1>p0:
        return 1
    else:return 0

text_data = []
for i in [21,22,23,24,25]:
    file1 = open(r'spam/%s.txt'%i)
    text = file1.read()
    code = chardet.detect(text)['encoding']
    text = text.decode(code).lower()
    words = nltk.word_tokenize(text)
    text_data.append(words)
    file1.close()

for i in [21,22,23,24,25]:
    file1 = open(r'ham/%s.txt'%i)
    text = file1.read()
    code = chardet.detect(text)['encoding']
    text = text.decode(code).lower()
    words = nltk.word_tokenize(text)
    text_data.append(words)
    file1.close()

p1_vect,p0_vect,p1,p0 = createClassifier()
print vocabList
for i in text_data:
    temp = createVector(i,vocabList)
    print classing(p1_vect,p0_vect,p1,p0,temp)," "

