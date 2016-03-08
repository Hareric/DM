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
Create_Time = 2015/11/7
根据用户的关注,分析用户的关注矩阵,若用户1关注用户2,则matrix(1,2)=1(非对称矩阵)
输入:用户字典
输出:用户SY-用户SY-权值  UserNum*3 矩阵
"""

from user_blog import *
import time


class FollowMatrix:
    def __init__(self):
        self.follow_matrix = []

    def __create_follow_matrix(self):
        for i in range(User.Num):
            follow_users = User.Dict[User.IDs[i]].get_follows()  # 关注的用户
            for j in follow_users:
                try:  # 若关注的用户在用户名单中,则为这2个用户 添加权值
                    line = [i, User.IDs.index(j), 1]
                    self.follow_matrix.append(line)
                except ValueError:
                    continue

    def get_result(self):
        start = time.time()
        self.__create_follow_matrix()
        end = time.time()
        print "用户-用户关注矩阵构建完毕,花费时间为:%.4fs" % (end - start)
        return self.follow_matrix
