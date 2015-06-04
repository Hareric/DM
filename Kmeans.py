# coding=utf-8
__author__ = 'Eric-Chan'

import random

def loadDataSet(fileName):#导入数据集
    datemat = []
    file1 = open(fileName)
    line = file1.readline()
    while line:
        line = file1.readline()
        temp = line.strip().split(',')
        datemat.append(temp)
    file1.close()
    datemat.pop()
    return datemat

def changeDateSet(datemat):#对数据集进行预处理
    dict1 = {'FEMALE' : 0,'MALE' : 1,'INNER_CITY' : 0,'TOWN' : 1,'RURAL' : 2,'SUBURBAN':3,'YES':1,'NO':0}

    for i in range(len(datemat)):
         for j in range(len(datemat[i])):
            if datemat[i][j] in dict1:
               datemat[i][j] =  dict1[datemat[i][j]]
    #归一化处理
    for i in [1,3,4,6]:
          lmax = max([float(x[i]) for x in datemat])
          lmin = min([float(x[i]) for x in datemat])

          for j in range(len(datemat)):
              datemat[j][i] = float(datemat[j][i])
              datemat[j][i] = ((datemat[j][i] - lmin) / (lmax - lmin))
    return datemat

def randCent(dataSet,k): #构建一个包含k个随机簇中心的集合
    m = len(dataSet)    #行数   数据集个数
    n = len(dataSet[1]) #列数  （特征数量）
    centroids = [[0 for a in range(n)] for b in range(k)]
    rams = []
    for i in range(k):#创建k个 0~1的随机数
        ram = random.uniform(0,1)
        rams.append(ram)

    for c in range(k):
        centroids[c][0] = str(c+1)  #k个簇 每个簇为一个列表 第一值为序号 其余为特征
        for j in range(1,n):
            minJ = min([x[j] for x in dataSet])
            maxJ = max([x[j] for x in dataSet])
            rangeJ=float(maxJ - minJ)
            centroids[c][j] = minJ+rangeJ*rams[c] #产生k个坐标随机的簇
    return centroids

def updateCentroids(teamdate,centroids,k):   #更新簇中心的位置

    n = 12 #列数  （特征数量)
    new = [[0 for a in range(n)] for b in range(k)] #新建k个簇坐标
    for c in range(k):
        new[c][0] = str(c+1)

    for kk in range(k):
        m = len(teamdate[kk])
        for i in range (1,n):
            distance = 0
            for j in range(m):
                distance += teamdate[kk][j][i]
            if m != 0 :
              distance/=m
              new[kk][i] = distance

    return new

def kmeams(k):
    #导入数据集
    datemat = loadDataSet('bank-data.csv')
    datemat = changeDateSet(datemat)
    #生成随机位置的k个族 每个族第一个数字为编号
    clusts = randCent(datemat,k)
    m = len(datemat) #数据集数量
    n = len(datemat[0]) #特征数量
    clusterChanged=True
    xhcs = 0
    while clusterChanged:
        xhcs = xhcs + 1
        team = [[] for i in range(k)] #建立k个分组 对样点进行分组
    #利用欧氏距离公式寻找每个样本与之最近的簇 并进行分组
        for c in range(m):
            dis = [0 for i in range(k)]
            for i in range(k):
                for j in range(1,n):
                     dis[i]=( dis[i] + (datemat[c][j] - clusts[i][j])**2)

            g = dis.index(min(dis)) #获得最小值的索引 根据索引分配
            team[g].append(datemat[c])

        New_clusts = updateCentroids(team,clusts,k)

    #判断 质心是否改变 若不再改变则停止循环
        Change = 0
        Changes = 0
        for kk in range(k):
            for i in range(1,n):
               Change +=(New_clusts[kk][i] - clusts[kk][i])**2

            Changes += Change


        if Changes <= 0.0000001:
            clusterChanged=False
        else:
            clusts = New_clusts
    print '￥￥￥￥￥共循环%s次￥￥￥￥￥'%xhcs
    for kk in range(k):

        print '\n簇%s：'%(kk+1)
        for i in range(len(team[kk])):
           print team[kk][i][0],
        print '\n','该簇共获得%s个数据'%len(team[kk])

kmeams(6)