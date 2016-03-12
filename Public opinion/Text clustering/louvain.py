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
Create_Time = 2016/03/07
使用igraph包中的BGLL算法对社区进行社区检测
输入用户-用户权值矩阵
输出社区检测结果和社区模块度
"""

import igraph


class Louvain:
    divide_result = None  # 社区划分结果
    modularity = None  # 社区模块度

    def __init__(self, users_links):
        self.users_link = users_links  # 用户权值矩阵
        self.divide()

    def __create_graph(self):
        """
        使用igraph构建图
        :return: graph, weights list
        """
        user_num = max([max([i[0] for i in self.users_link]), max([i[1] for i in self.users_link])]) + 1
        g = igraph.Graph(user_num)
        weights = []
        edges = []
        for line in self.users_link:
            edges += [(line[0], line[1])]
            weights.append(line[2])
        g.add_edges(edges)
        # node_value = g.authority_score(weights=weights)
        # self.node_value_dict = dict(zip(range(user_num), node_value))
        return g, weights

    def divide(self):
        """
        使用igraph包中BGLL算法对已构建好的图进行社区检测
        :return:
        """
        graph, weights = self.__create_graph()
        Louvain.divide_result = graph.community_multilevel(weights=weights)
        Louvain.modularity = Louvain.divide_result.modularity
