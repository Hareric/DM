#coding=utf-8
__author__ = 'Eric_Chan'
'''基于物品的协同过滤算法'''
'''
功能：通过分析电影间的相似度，再对用户喜欢的电影和评分进行分析，最后对其他电影进行预测评分。
基本数据集为：movies.dat ; ratings.dat ; users.dat
ItemSimilarity.txt ;ChangedSim.txt 为相似度矩阵和处理过的相似度矩阵
Recommendation_10.txt 为K为10的 用户对所有电影的预测评分（未处理）矩阵
predictRating.txt 最后导出为 用户名::电影名::实际评分::预测评分（已处理）
'''

from math import sqrt

def LodeMovie(filename):
    f = open(filename)
    line = f.readline()
    data = {}
    MovNum = 0
    while line:
        unit = [0,[]]
        temp = line.strip().split('::')
        unit[0] = int(temp[0])
        unit[1] = temp[2].strip().split('|')
        data[unit[0]] = unit[1]
        if unit[0] > MovNum:
            MovNum = unit[0] #计算电影的总数目
        line = f.readline()
    f.close()
    W = [[0 for i in range(MovNum)]for c in range(MovNum)] #构建物品关联矩阵
    W_ItemSimilarity = [[0 for i in range(MovNum)]for c in range(MovNum)]#构建物品关联度矩阵
    return data,W,W_ItemSimilarity

def LodeRating(filename):#构建关于 用户-电影-分数 的字典矩阵
     f = open(filename)
     line = f.readline()
     data = {}
     user_num = 0
     while line:
        temp = line.strip().split('::')
        temp[0],temp[1],temp[2] = int(temp[0]),int(temp[1]),int(temp[2])
        if data.has_key(temp[0]) == False:
            data[temp[0]] = []
        data[temp[0]].append([temp[1],temp[2]]) #构建关于用户喜欢的电影的字典，字典内容以二重数组呈现，内容包括喜欢的电影和对应等级
        if temp[0] > user_num:
            user_num = temp[0]
        line = f.readline()
     f.close()
     return data,user_num

def calculate_ItemSimilarity():#计算所有电影的相互相似度，返回相似度矩阵
    MovieData,W,W_ItemSimilarity = LodeMovie('movies.dat')
    RatingData,user_num = LodeRating('ratings.dat')

    for i in range(1,user_num+1): #首先构建用户对喜欢的电影的矩阵
        if RatingData.has_key(i): #判断是否存在此用户
            for j in range(len(RatingData[i])):

                for k in range(len(RatingData[i])):

                    if j == k:
                        continue
                    W[RatingData[i][j][0]-1][RatingData[i][k][0]-1] = W[RatingData[i][j][0]-1][RatingData[i][k][0]-1] + 1
    file1 = open('ItemSimilarity.txt','w')
    for i in range(len(W)):#然后根据用户喜欢电影的矩阵 构建各电影的物品相似度 W_ItemSimilarity[i][j]表示电影i和电影j的相似度
        for j in range(len(W)):
            if W[i][j] == 0:
                continue
            else:
                W_ItemSimilarity[i][j] = W[i][j] / sqrt(sum(W[i]) * sum(W[j]))
        file1.write(str(W_ItemSimilarity[i]) + '\n')
    file1.close()


    return W_ItemSimilarity

def change_ItemSimilarity():#将物品的相似度进行归一化 保留4为小树
    file1 = open('ItemSimilarity.txt','r')
    file2 = open('ChangedSim.txt','w')
    line = file1.readline()
    while line:
        temp = line.split(',')
        temp_max = 0
        temp_min = 1
        for i in range(len(temp)):
            temp[i] = float(temp[i])
            if temp[i] > temp_max:
                temp_max = temp[i]
            if temp[i] < temp_min:
                temp_min = temp[i]

        for i in range(len(temp)):
            h = temp_max - temp_min
            if h == 0:
                temp[i] = 0
            else:
                a = (temp[i] - temp_min) / h
                temp[i] = float( '%.4f' % a)
        file2.write(str(temp) + '\n')
        line = file1.readline()
    file1.close()
    file2.close()

def calculate_Interest(K,Team,Test = False):#确定是否为测试，并选择进行测试的用户组数
# 确定 选出K部最相似的电影 的K值 预测用户对所有电影的评分
    RatingData,user_num = LodeRating('ratings.dat')
    W_ItemSimilarity = []

    file1 = open('ChangedSim.txt','r')
    line = file1.readline()
    while line:
        temp = line.split(',')
        for i in range(len(temp)):
            temp[i] = float(temp[i])
        W_ItemSimilarity.append(temp)
        line = file1.readline()
    file1.close()

    MovNum = len(W_ItemSimilarity)
    highestSim = [{} for i in range(MovNum)]
    file2 = open('Recommendation_%s.txt'%K,'w')

    #先构造一个字典矩阵，找出每部电影最高相似度的K部
    for i in range(MovNum):
        temp_W = sorted(W_ItemSimilarity[i])[-1:(-K-1):-1]
        for j in range(K):
            highestSim[i][W_ItemSimilarity[i].index(temp_W[j])+1] = temp_W[j] #构建每个电影相似度最高的5部电影的 [{索引号：相似度}{索引号：相似度}{索引号：相似度}{索引号：相似度}{索引号：相似度}] 的字典列表

    P = [[0 for i in range(MovNum)] for c in range(user_num)]#构造 用户-电影 矩阵

    if Test:#判断是否在测试K值
        test_num = 50 #选择要测试的数目
        l = test_num * (Team-1)
        r = test_num * Team
    else:
        l = 0
        r = user_num
        test_num = user_num
    a = 0
    for i in range(l,r):
        if RatingData.has_key(i+1):
            for j in range(len(RatingData[i+1])):
                for k in range(MovNum):
                    if RatingData[i+1][j][0] in highestSim[k].keys():
                        P[i][k] = P[i][k] + (RatingData[i+1][j][1] * highestSim[k][RatingData[i+1][j][0]])
            # P[i][RatingData[i][j][0]-1] = float('%.4f'%P[i][RatingData[i][j][0]-1])

        for m in range(len(P[i])-1):
            P[i][m] = float('%.4f'%P[i][m])
            file2.write(str(P[i][m]) + '::')
        P[i][-1] = float('%.4f'%P[i][-1])
        file2.write(str(P[i][-1]))
        file2.write('\n')
        a = a + 1
        print '已分析完第%s个用户'%a + ',剩余%s个用户'%(test_num-a)
    file2.close()

def predictRating(filename):#将预测数值进行处理 分为6个等级
    RatingData , user_num = LodeRating('ratings.dat')
    file1 = open(filename,'r')
    file2 = open('predictRating','w')
    line = file1.readline()
    i = 0
    while line:
        i = i + 1
        predict = line.split('::')
        for d in range(len(predict)):
            predict[d] = float(predict[d])
            if  predict[d] >= 30:
                predict[d] = 5
            elif (predict[d]>=22)&(predict[d]<30):
                predict[d] = 4
            elif (predict[d]>=15)&(predict[d]<22):
                predict[d] = 3
            elif (predict[d]>= 7)&(predict[d]<15):
                predict[d] = 2
            elif (predict[d] > 0)&(predict[d]< 7):
                predict[d] = 1
            else:
                predict[d] = 0
            predict[d] = int(predict[d])

        for j in range(len(RatingData[i])):
            temp = [i,RatingData[i][j][0],RatingData[i][j][1],predict[RatingData[i][j][0]-1]]
            for k in range(3):
                file2.write(str(temp[k]) + '::')
            file2.write(str(temp[-1]))
            file2.write('\n')
        line = file1.readline()

# calculate_Interest(5,1,True)
# calculate_Interest(10,2,True)
# calculate_Interest(20,3,True)
# calculate_Interest(40,4,True)
# calculate_Interest(80,5,True)
# calculate_Interest(160,6,True)

# calculate_Interest(10,,False)
predictRating('Recommendation_10.txt')

