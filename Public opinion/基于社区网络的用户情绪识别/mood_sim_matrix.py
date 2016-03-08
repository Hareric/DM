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
input:每个用户的情绪值
return:用户-用户情绪相似度矩阵
"""
'''
Time = 2016/01/23
    该类放弃使用
'''
from user_blog import *
import time
import sys


class MoodSimMatrix:
    def __init__(self):
        pass

    @classmethod
    def calculate_users_sim(cls, user_1_array, user_2_array):
        """
        :param user_1_array: 用户1的情绪值
        :param user_2_array: 用户2的情绪值
        :return: 用户1与用户2的情绪相似度
        """
        d = 0  # 表示 用户1 和 用户2 之间的距离  距离越大 相似度越低
        for i in range(8):
            d += (user_1_array[i] - user_2_array[i]) ** 2
        d **= 0.5
        return d

    def __create_mood_sim_matrix(self):
        mood_distance_matrix = []  # 用户情绪权值矩阵 [[a, b, 1]...] 用户a与用户b之间的距离矩阵
        max_value = -1.
        min_value = 100.
        for i in range(User.Num):
            if max(User.Dict[User.IDs[i]].get_mood_value()) == 0:  # 若用户无任何情绪值则不考虑与用户之间的情绪相似性
                continue
            for j in range(i):
                if max(User.Dict[User.IDs[j]].get_mood_value()) == 0:  # 若用户无任何情绪值则不考虑与用户之间的情绪相似性
                    continue
                d = self.calculate_users_sim(User.Dict[User.IDs[i]].get_mood_value(),
                                             User.Dict[User.IDs[j]].get_mood_value())
                if d < min_value:
                    min_value = d
                if d > max_value:
                    max_value = d
                mood_distance_matrix.append([i, j, d])
            print "   情绪相似度矩阵构建中...%.2f%%" % (float(i) / User.Num * 50),
            sys.stdout.write('\r')

        # 归一化
        mood_sim_matrix = []
        scope = max_value - min_value
        l = len(mood_distance_matrix)
        c = 0.0
        for unit in mood_distance_matrix:
            sim = (max_value - unit[2]) / scope  # 相似度
            mood_sim_matrix.append([unit[0], unit[1], sim])
            mood_sim_matrix.append([unit[1], unit[0], sim])
            c += 1
            print "   情绪相似度矩阵构建中...%.2f%%" % (c / l * 50 + 50),
            sys.stdout.write('\r')
        return mood_sim_matrix

    def get_result(self):
        start_time = time.time()
        mood_sim_matrix = self.__create_mood_sim_matrix()
        end_time = time.time()
        print "情绪相似度矩阵构建完毕! time:%is" % (end_time - start_time)
        return mood_sim_matrix
