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
Create_Time = 2016/1/15
"""
'''
该py文件包含8个类,分别保存社区检测出来的8个情绪社区的结果
(0:'disgust',1:'sympathy',2:'like',3:'hate',4:'sad',5:'happy',6:'angry',7:'anxiety')
IDs = 存在于该社区的用户的IDs的集合列表
num = 该社区的人数
valueOfMood = 该社区的情绪值 形如: [1,3,12,3,12,31,3,6]
'''


class DisgustResult:
    """
    该类用来记录厌恶社区的详细结果
    IDs 记录该社区的用户的ID
    num 记录该社区的用户的人数
    valueOfMood 记录该社区的情绪值
    """

    def __init__(self):
        pass

    IDs = []
    num = 0
    valueOfMood = [0] * 8


class SympathyResult:
    """
    该类用来记录同情社区的详细结果
    IDs 记录该社区的用户的ID
    num 记录该社区的用户的人数
    valueOfMood 记录该社区的情绪值
    """

    def __init__(self):
        pass

    IDs = []
    num = 0
    valueOfMood = [0] * 8


class LikeResult:
    """
    该类用来记录喜欢社区的详细结果
    IDs 记录该社区的用户的ID
    num 记录该社区的用户的人数
    valueOfMood 记录该社区的情绪值
    """

    def __init__(self):
        pass

    IDs = []
    num = 0
    valueOfMood = [0] * 8


class HateResult:
    """
    该类用来记录怨恨社区的详细结果
    IDs 记录该社区的用户的ID
    num 记录该社区的用户的人数
    valueOfMood 记录该社区的情绪值
    """

    def __init__(self):
        pass

    IDs = []
    num = 0
    valueOfMood = [0] * 8


class SadResult:
    """
    该类用来记录悲伤社区的详细结果
    IDs 记录该社区的用户的ID
    num 记录该社区的用户的人数
    valueOfMood 记录该社区的情绪值
    """

    def __init__(self):
        pass

    IDs = []
    num = 0
    valueOfMood = [0] * 8


class HappyResult:
    """
    该类用来记录悲伤社区的详细结果
    IDs 记录该社区的用户的ID
    num 记录该社区的用户的人数
    valueOfMood 记录该社区的情绪值
    """

    def __init__(self):
        pass

    IDs = []
    num = 0
    valueOfMood = [0] * 8


class AngryResult:
    """
    该类用来记录愤怒社区的详细结果
    IDs 记录该社区的用户的ID
    num 记录该社区的用户的人数
    valueOfMood 记录该社区的情绪值
    """

    def __init__(self):
        pass

    IDs = []
    num = 0
    valueOfMood = [0] * 8


class AnxietyResult:
    """
    该类用来记录焦虑社区的详细结果
    IDs 记录该社区的用户的ID
    num 记录该社区的用户的人数
    valueOfMood 记录该社区的情绪值
    """

    def __init__(self):
        pass

    IDs = []
    num = 0
    valueOfMood = [0] * 8

# class DisgustResult:
#     """
#     该类用来记录厌恶社区的详细结果
#     IDs 记录该社区的用户的ID
#     num 记录该社区的用户的人数
#     valueOfMood 记录该社区的情绪值
#     """
#     __IDs__ = []
#     __num__ = 0
#     __valueOfMood__ = [0] * 8
#
#     def getIDs(self):
#         return DisgustResult.__IDs__
#
#     def setIDs(self, IDs):
#         DisgustResult.__IDs__ = IDs
#
#     def setNum(self, num):
#         DisgustResult.__num__ = num
#
#     def getNum(self):
#         return DisgustResult.__num__
#
#     def setValueOfMood(self, valueOfMood):
#         DisgustResult.__valueOfMood__ = valueOfMood
#
#     def getValueOfMood(self):
#         return DisgustResult.__valueOfMood__
#
#
# class SympathyResult:
#     """
#     该类用来记录同情社区的详细结果
#     IDs 记录该社区的用户的ID
#     num 记录该社区的用户的人数
#     valueOfMood 记录该社区的情绪值
#     """
#     __IDs__ = []
#     __num__ = 0
#     __valueOfMood__ = [0] * 8
#
#     def getIDs(self):
#         return SympathyResult.__IDs__
#
#     def setIDs(self, IDs):
#         SympathyResult.__IDs__ = IDs
#
#     def setNum(self, num):
#         SympathyResult.__num__ = num
#
#     def getNum(self):
#         return SympathyResult.__num__
#
#     def setValueOfMood(self, valueOfMood):
#         SympathyResult.__valueOfMood__ = valueOfMood
#
#     def getValueOfMood(self):
#         return SympathyResult.__valueOfMood__
#
#
# class LikeResult:
#     """
#     该类用来记录喜欢社区的详细结果
#     IDs 记录该社区的用户的ID
#     num 记录该社区的用户的人数
#     valueOfMood 记录该社区的情绪值
#     """
#     __IDs__ = []
#     __num__ = 0
#     __valueOfMood__ = [0] * 8
#
#     def getIDs(self):
#         return LikeResult.__IDs__
#
#     def setIDs(self, IDs):
#         LikeResult.__IDs__ = IDs
#
#     def setNum(self, num):
#         LikeResult.__num__ = num
#
#     def getNum(self):
#         return LikeResult.__num__
#
#     def setValueOfMood(self, valueOfMood):
#         LikeResult.__valueOfMood__ = valueOfMood
#
#     def getValueOfMood(self):
#         return LikeResult.__valueOfMood__
#
#
# class HateResult:
#     """
#     该类用来记录怨恨社区的详细结果
#     IDs 记录该社区的用户的ID
#     num 记录该社区的用户的人数
#     valueOfMood 记录该社区的情绪值
#     """
#     __IDs__ = []
#     __num__ = 0
#     __valueOfMood__ = [0] * 8
#
#     def getIDs(self):
#         return HateResult.__IDs__
#
#     def setIDs(self, IDs):
#         HateResult.__IDs__ = IDs
#
#     def setNum(self, num):
#         HateResult.__num__ = num
#
#     def getNum(self):
#         return HateResult.__num__
#
#     def setValueOfMood(self, valueOfMood):
#         HateResult.__valueOfMood__ = valueOfMood
#
#     def getValueOfMood(self):
#         return HateResult.__valueOfMood__
#
#
# class SadResult:
#     """
#     该类用来记录悲伤社区的详细结果
#     IDs 记录该社区的用户的ID
#     num 记录该社区的用户的人数
#     valueOfMood 记录该社区的情绪值
#     """
#     __IDs__ = []
#     __num__ = 0
#     __valueOfMood__ = [0] * 8
#
#     def getIDs(self):
#         return SadResult.__IDs__
#
#     def setIDs(self, IDs):
#         SadResult.__IDs__ = IDs
#
#     def setNum(self, num):
#         SadResult.__num__ = num
#
#     def getNum(self):
#         return SadResult.__num__
#
#     def setValueOfMood(self, valueOfMood):
#         SadResult.__valueOfMood__ = valueOfMood
#
#     def getValueOfMood(self):
#         return SadResult.__valueOfMood__
#
#
# class HappyResult:
#     """
#     该类用来记录悲伤社区的详细结果
#     IDs 记录该社区的用户的ID
#     num 记录该社区的用户的人数
#     valueOfMood 记录该社区的情绪值
#     """
#     __IDs__ = []
#     __num__ = 0
#     __valueOfMood__ = [0] * 8
#
#     def getIDs(self):
#         return HappyResult.__IDs__
#
#     def setIDs(self, IDs):
#         HappyResult.__IDs__ = IDs
#
#     def setNum(self, num):
#         HappyResult.__num__ = num
#
#     def getNum(self):
#         return HappyResult.__num__
#
#     def setValueOfMood(self, valueOfMood):
#         HappyResult.__valueOfMood__ = valueOfMood
#
#     def getValueOfMood(self):
#         return HappyResult.__valueOfMood__
#
#
# class AngryResult:
#     """
#     该类用来记录愤怒社区的详细结果
#     IDs 记录该社区的用户的ID
#     num 记录该社区的用户的人数
#     valueOfMood 记录该社区的情绪值
#     """
#     __IDs__ = []
#     __num__ = 0
#     __valueOfMood__ = [0] * 8
#
#     def getIDs(self):
#         return AngryResult.__IDs__
#
#     def setIDs(self, IDs):
#         AngryResult.__IDs__ = IDs
#
#     def setNum(self, num):
#         AngryResult.__num__ = num
#
#     def getNum(self):
#         return AngryResult.__num__
#
#     def setValueOfMood(self, valueOfMood):
#         AngryResult.__valueOfMood__ = valueOfMood
#
#     def getValueOfMood(self):
#         return AngryResult.__valueOfMood__
#
#
# class AnxietyResult:
#     """
#     该类用来记录焦虑社区的详细结果
#     IDs 记录该社区的用户的ID
#     num 记录该社区的用户的人数
#     valueOfMood 记录该社区的情绪值
#     """
#     __IDs__ = []
#     __num__ = 0
#     __valueOfMood__ = [0] * 8
#
#     def getIDs(self):
#         return AnxietyResult.__IDs__
#
#     def setIDs(self, IDs):
#         AnxietyResult.__IDs__ = IDs
#
#     def setNum(self, num):
#         AnxietyResult.__num__ = num
#
#     def getNum(self):
#         return AnxietyResult.__num__
#
#     def setValueOfMood(self, valueOfMood):
#         AnxietyResult.__valueOfMood__ = valueOfMood
#
#     def getValueOfMood(self):
#         return AnxietyResult.__valueOfMood__
