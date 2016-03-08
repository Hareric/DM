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

import xlrd
import igraph


def load_data(file_name):
    """
    读取xls文件,获得矩阵.
    :param file_name: xls文件路径
    :return: 除去表头后的二元列表
    """
    data = xlrd.open_workbook(file_name)  # 打开xls
    table = data.sheet_by_index(0)  # 打开sheet1
    all_data = table._cell_values  # 将所有数据 以二元列表进行构造
    all_data = all_data[1:]  # 除去表头
    for i in range(all_data.__len__()):  # 将表中数据的整数转化为int类型
        for j in range(all_data[0].__len__()):
            try:
                if all_data[i][j] == int(all_data[i][j]):
                    all_data[i][j] = int(all_data[i][j])
            except UnicodeEncodeError:
                continue
    return all_data


class Louvain:
    divide_result = None  # 社区划分结果
    modularity = None  # 社区模块度

    def __init__(self, users_links):
        self.users_link = users_links  # 用户权值矩阵
        self.node_value_dict = {}  # 节点的中心度值 字典
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
        node_value = g.authority_score(weights=weights)
        self.node_value_dict = dict(zip(range(user_num), node_value))
        return g, weights

    def divide(self):
        """
        使用igraph包中BGLL算法对已构建好的图进行社区检测
        :return:
        """
        graph, weights = self.__create_graph()
        Louvain.divide_result = graph.community_multilevel(weights=weights)
        Louvain.modularity = Louvain.divide_result.modularity

    def get_centrality(self, cluster, num=None):
        """
        :param cluster: the cluster
        :param num: the number that how many centrality want to get
        :return: the centrality of the cluster
        """
        cluster = list(cluster)
        if num is None:
            num = 1
        centrality_dict = {}  # 核心用户的 id:中心度值
        for node in cluster:
            if centrality_dict.__len__() < num:
                centrality_dict[node] = self.node_value_dict[node]
            elif self.node_value_dict[node] > min(centrality_dict.values()):
                centrality_dict = {k: v for k, v in centrality_dict.iteritems()
                                   if v != min(centrality_dict.values())}  # 移去最小值
                centrality_dict[node] = self.node_value_dict[node]
        return centrality_dict.keys()


if __name__ == '__main__':
    links = load_data('dataSet/class_data.xls')
    labels = dict(load_data('dataSet/class_label.xls'))
    Class_6 = Louvain(links)
    # print Class_6.divide_result
    # print 'modularity:', Class_6.modularity

    for cluster in Class_6.divide_result:
        for node in cluster:
            print labels[node],
        print '\ncentrality:',
        for cen_node in Class_6.get_centrality(cluster, 1):
            print labels[cen_node],
        print '\n'



