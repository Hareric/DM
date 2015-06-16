#coding=utf-8
__author__ = 'Eric Chan'

import xlrd
from igraph import *
def lodedata(filename):
    bk = xlrd.open_workbook(filename)
    sh = bk.sheet_by_name("Sheet1")
    row = sh.nrows #行数
    v = sh._cell_values
    print v
    print type(v)
    from_num = [int(sh.cell_value(i,0)) for i in range(1,row)]
    user_num = max(from_num)+1
    matrix = [[0 for i in range(user_num)]for j in range(user_num)]
    for i in range(1,len(v)):
        matrix[int(v[i][0])][int(v[i][1])] = int(v[i][2]) #构建邻接矩阵
    for c in range(len(matrix)):
        print c,matrix[c]
    return user_num,matrix

def LPA():
    user_num,matrix = lodedata('class_data.xls')
    g = Graph(1) #首先构建只有一个点的图
    g.add_vertices(user_num - 1)#根据用户数 加入足够点
    weights = []#构建权值列表
    for i in range(user_num):
        for j in range(user_num):
            if matrix[i][j]>0:
                g.add_edge(i,j)#为点添加边
                weights.append(matrix[i][j])#为边记录权值
    result = g.community_label_propagation(weights=weights) #运用标签传播算法进行社区划分
    print result


LPA()