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
Create_Time = 2016/1/19
"""

from load_SQL import load_sql
from analyze_user_mood import *
from louvain import *
from community_identification import *
from mood_matrix import *
from follow_matrix import *
from result_save import *


def print_result(community_name, result_class):
    """
    print:社区内部详细结果
    :type result_class: MoodResult
    """
    print "_____________________________________________________________________________________________________________________________________\n" \
          "%s社区结果" % community_name
    print "社区大小:%i" % result_class.num
    print "社区情绪值:\n" \
          + "disgust sympathy like hate sad happy angry anxiety\n" \
          + str(result_class.valueOfMood)


if __name__ == '__main__':
    load_sql(user_num=None, time_to_analysis='03月07日'.decode('utf-8'))
    AnalyzeUserMood()
    link_matrix = FollowMatrix().get_result()
    link_matrix += MoodMatrix().get_result()
    bgll_result, modularity = Louvain(link_matrix).get_result()
    CommunityIdentification(bgll_result)

    print_result("厌恶", DisgustResult)
    print_result("同情", SympathyResult)
    print_result("喜欢", LikeResult)
    print_result("怨恨", HappyResult)
    print_result("悲伤", SadResult)
    print_result("愉快", HappyResult)
    print_result("愤怒", AngryResult)
    print_result("焦虑", AnxietyResult)
