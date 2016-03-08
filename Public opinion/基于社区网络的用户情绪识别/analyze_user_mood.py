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
Create_Time = 2016/1/20
input:单个用户规定时间内的博文
return:该用户的情绪值列表 0：厌恶  1：同情  2：喜欢  3：怨恨  4：悲伤  5：愉快  6：愤怒  7：焦虑
Instruction:
    该算法通过对博文进行简单的词语匹配分析情绪,并未考虑过多的句式结构等等
"""
'''
Time = 2016/1/23  放弃使用该类
'''
import jieba
import time
import sys

jieba.initialize()
time.sleep(1)

import numpy
from user_blog import *


class AnalyzeUserMood:
    emotion_word_dic = {}  # 情緒詞對應情緒詞字典
    stop_word_list = []  # 停用詞列表

    def __init__(self):
        AnalyzeUserMood.emotion_word_dic = self.create_emotion_dictionary('data/emotion_dic.txt')
        AnalyzeUserMood.stop_word_list = self.create_stop_word_list('data/stop_word.txt')
        start_time = time.time()
        d = 0.0
        for ID in User.IDs:
            d += 1
            print "  用户情绪分析中...%.2f%%" % (d / User.Num * 100),
            sys.stdout.write('\r')
            mood_value = self.__user_mood_analyze(User.Dict[ID].get_blog())
            User.Dict[ID].set_mood_value(mood_value)
            if max(mood_value) != 0:
                User.Dict[ID].set_mood(list(mood_value).index(max(mood_value)))

        end_time = time.time()
        print "用户情绪分析完毕,花费时间为:%.2fs" % (end_time - start_time)

    @classmethod
    def create_emotion_dictionary(cls, filename):
        """
        :param filename: 情绪词字典的路径
        :return: 情绪词:该词的情绪值 字典
        """
        f = open(filename, 'r')
        emotion_dic = {}
        line = f.readline()
        while line:
            word_value = line.strip().split('\t')
            value = [0] * 8
            for i in range(8):
                value[i] = int(word_value[i + 1])
            emotion_dic[word_value[0].decode('utf-8')] = value
            line = f.readline()
        f.close()
        return emotion_dic

    @classmethod
    def create_stop_word_list(cls, filename):
        """
        :param filename: 停用词的路径
        :return: 停用词列表
        """
        f = open(filename, 'r')
        stop_word_list = []
        line = f.readline()
        while line:
            stop_word_list.append(line.strip().decode('utf-8'))
            line = f.readline()
        f.close()
        return stop_word_list

    def __text_mood_analyze(self, text):
        """
        :param text: 一篇博文
        :return: 該篇博文的情緒值列表
        """
        text_mood_value = numpy.zeros(8)  # 一篇博文的情绪值列表
        word_list = list(jieba.cut(text, cut_all=False))

        for word in word_list:
            # if word in self.stop_word_list:
            #     continue
            try:
                text_mood_value += self.emotion_word_dic[word]
            except KeyError:
                continue
        return text_mood_value

    def __user_mood_analyze(self, origin_text):
        """
        :param origin_text: 用户日发博文列表
        :return: 输出该用户歸一化後该日的情绪值列表
        """
        l = len(origin_text)  # 用户日发博文量
        user_mood_value = numpy.zeros(8)  # 构建该用户的情绪值列表
        for i in range(l):  # 对该用户的每条博文进行分析
            user_mood_value += self.__text_mood_analyze(origin_text[i].get_text())
        # 對情緒值進行歸一化
        max_value = max(user_mood_value)
        if max_value == 0:
            return user_mood_value
        min_value = min(user_mood_value)
        user_mood_value = (user_mood_value - min_value) / (max_value - min_value)
        return user_mood_value
