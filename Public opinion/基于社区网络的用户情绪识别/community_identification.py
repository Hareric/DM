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
输入:社区检测结果
输出:8大情绪社区,并将各社区的人数,情绪值,用户ID保存
"""

from user_blog import *
from result_save import *
import numpy as np


class CommunityIdentification:
    def __init__(self, division_result):
        self.divisionResult = division_result
        self.moodDict = {0: 'disgust', 1: 'sympathy', 2: 'like', 3: 'hate', 4: 'sad', 5: 'happy', 6: 'angry',
                         7: 'anxiety'}
        self.identifying()

    @staticmethod
    def __identify_mood_community(community):
        """
        :param community: 一个社区的用户
        :return: 社区的情绪识别结果的编号,该社区的情绪值
        """
        community_mood_value = np.zeros(8)  # 合计整个社区的情绪值的总和
        for SY in community:
            community_mood_value += User.Dict[User.IDs[SY]].get_mood_value()
        if max(community_mood_value) == 0:
            community_mood_num = -1
        else:
            community_mood_num = list(community_mood_value).index(max(community_mood_value))
        return community_mood_num, community_mood_value

    def identifying(self):

        community_user_num = [0] * 8  # 记录每个情绪社区的人数
        for community in self.divisionResult:  # ignore the community which's the number is below 10
            if len(community) < 10:
                continue
            else:
                community_mood_num, community_mood_value = self.__identify_mood_community(community)
                if community_mood_num == -1 or community_user_num[community_mood_num] > len(community):
                    continue
                else:
                    community_user_num[community_mood_num] = len(community)

                    # 社区识别的结果保存txt
                    filename = "result/%s.txt" % self.moodDict[community_mood_num]
                    f = open(filename, 'w')
                    for SY in community:
                        f.write(str(User.IDs[SY]) + '\n')
                    f.write("社区大小:%i\n" % len(community))
                    f.write("情绪值:\ndisgust sympathy like hate sad happy angry anxiety\n")
                    for i in range(8):
                        f.write(str(community_mood_value[i]) + '\t')
                    f.close()

                    # 将结果保存在result_save.py
                    ids = []
                    for SY in community:
                        ids.append(User.IDs[SY])
                    if community_mood_num == 0:
                        mood_result = DisgustResult
                    elif community_mood_num == 1:
                        mood_result = SympathyResult
                    elif community_mood_num == 2:
                        mood_result = LikeResult
                    elif community_mood_num == 3:
                        mood_result = HateResult
                    elif community_mood_num == 4:
                        mood_result = SadResult
                    elif community_mood_num == 5:
                        mood_result = HappyResult
                    elif community_mood_num == 6:
                        mood_result = AngryResult
                    elif community_mood_num == 7:
                        mood_result = AnxietyResult
                    mood_result.IDs = ids
                    mood_result.num = len(community)
                    mood_result.valueOfMood = list(community_mood_value)
