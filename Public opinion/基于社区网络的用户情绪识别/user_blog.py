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
Create_Time = 2016/01/20
"""


class User:
    """
    该类用来记录单个微博用户的ID,博文,关注用户的ID,粉丝用户的ID,用戶當日情緒值;
    以及提供访问和修改的方法
    """

    Dict = {}  # 记录所有用户的字典,用户的ID作为字典的keys
    IDs = []  # 记录所有用户的ID
    Num = 0  # 用户数

    def __init__(self, id, name):  # 用户的ID和用户名在实例化后便固定不能修改
        self.__id = id
        self.__name = name
        self.__blog = []  # 用户发的博文
        self.__fans = []  # 用户的粉丝
        self.__follows = []  # 用户的关注
        self.__mood = -1  # 记录用户当日的情绪 0:'厌恶',1:'同情',2:'喜欢',3:'怨恨',4:'悲伤',5:'愉快',6:'愤怒',7:'焦虑',8:'其他'
        self.__mood_value = [0] * 8  # 記錄用戶當日的情緒值
        User.Dict[id] = self
        User.Num += 1
        User.IDs.append(id)

    def get_name(self):
        return self.__name

    def set_blog(self, blog):
        self.__blog = blog

    def get_blog(self):
        return self.__blog

    def add_blog(self, unit_blog):
        self.__blog.append(unit_blog)

    def set_fans(self, fans):
        self.__fans = fans

    def get_fans(self):
        return self.__fans

    def add_fans(self, unit_fan):
        self.__fans.append(unit_fan)

    def set_follows(self, follows):
        self.__follows = follows

    def get_follows(self):
        return self.__follows

    def add_follows(self, unit_follow):
        self.__follows.append(unit_follow)

    def set_mood(self, mood):
        self.__mood = mood

    def get_mood(self):
        return self.__mood

    def set_mood_value(self, value):
        self.__mood_value = value

    def get_mood_value(self):
        return self.__mood_value


class Blog:
    """
    记录博文的内容以及博文的发布时间
    """
    JAN = "01"
    FEB = "02"
    MAR = "03"
    APR = "04"
    MAY = "05"
    JUN = "06"
    JUL = "07"
    AUG = "08"
    SEP = "09"
    OCT = "10"
    NOV = "11"
    DEC = "12"
    import time
    LAST_YEAR = str(time.localtime()[0] - 1)
    LAST_JAN = LAST_YEAR + "-01"
    LAST_FEB = LAST_YEAR + "-02"
    LAST_MAR = LAST_YEAR + "-03"
    LAST_APR = LAST_YEAR + "-04"
    LAST_MAY = LAST_YEAR + "-05"
    LAST_JUN = LAST_YEAR + "-06"
    LAST_JUL = LAST_YEAR + "-07"
    LAST_AUG = LAST_YEAR + "-08"
    LAST_SEP = LAST_YEAR + "-09"
    LAST_OCT = LAST_YEAR + "-10"
    LAST_NOV = LAST_YEAR + "-11"
    LAST_DEC = LAST_YEAR + "-12"

    def __init__(self, content, time):
        self.__time = time  # 博文发布的时间
        self.__text = content  # 博文的内容

    def get_time(self):
        return self.__time

    def get_text(self):
        return self.__text
