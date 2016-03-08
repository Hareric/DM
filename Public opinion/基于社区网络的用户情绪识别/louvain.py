# coding=utf-8
#        ┏┓　　　┏┓+ +
# 　　　┏┛┻━━━┛┻┓ + +
# 　　　┃　　　　　　　┃ 　
# 　　　┃　　　━　　　┃ ++ + + +
# 　　 ████━████ ┃+
# 　　　┃　　　　　　　┃ +
# 　　　┃　　　┻　　　┃
# 　　　┃　　　　　　　┃ + +
# 　　　┗━┓　　　┏━┛
# 　　　　　┃　　　┃　　　　　　　　　　　
# 　　　　　┃　　　┃ + + + +
# 　　　　　┃　　　┃　　　　Codes are far away from bugs with the animal protecting　　　
# 　　　　　┃　　　┃ + 　　　　神兽保佑,代码无bug　　
# 　　　　　┃　　　┃
# 　　　　　┃　　　┃　　+　　　　　　　　　
# 　　　　　┃　 　　┗━━━┓ + +
# 　　　　　┃ 　　　　　　　┣┓
# 　　　　　┃ 　　　　　　　┏┛
# 　　　　　┗┓┓┏━┳┓┏┛ + + + +
# 　　　　　　┃┫┫　┃┫┫
# 　　　　　　┗┻┛　┗┻┛+ + + +
"""
Author = Eric_Chan
Create_Time = 2016/01/22
使用igraph包中的BGLL算法对社区进行社区检测
输入用户-用户权值矩阵
输出社区检测结果和社区模块度
"""

import igraph
from user_blog import *
import time
import sys


class Louvain:
    def __init__(self, users_link):
        self.users_link = users_link

    def __create_graph(self):
        g = igraph.Graph(User.Num)  # 首先构建点的个数为用户数目的图
        weights = []
        edges = []
        for line in self.users_link:
            edges += [(line[0], line[1])]
            weights.append(line[2])
        g.add_edges(edges)
        return g, weights

    def get_result(self):
        start_time = time.time()
        print "开始划分社区...",
        sys.stdout.write('\r')
        graph, weights = self.__create_graph()
        bgll_result = graph.community_multilevel(weights=weights)  # 社区划分结果
        end_time = time.time()
        print "划分完成,花费时间为:%0.2fs" % (end_time - start_time)

        modularity = bgll_result.modularity  # 社区模块度
        # print 'louvain社区探测算法' , '\n',bgll_result , '\n'
        # print "社区模块度:", modularity
        return bgll_result, modularity
