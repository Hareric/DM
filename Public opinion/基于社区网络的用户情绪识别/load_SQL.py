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
"""

import MySQLdb
from user_blog import *
import sys
import time


def load_sql(user_num=None, time_to_analysis=None):
    """
    利用数据库中的 用户ID-用户名 创建相应的User实例
    为每个用户实例 添加用户的关注,用户的粉丝,用户规定时间内所发的博文
    """
    if time_to_analysis is None:
        time_to_analysis = "%.2i" % time.localtime()[1]  # 导入某个月的博文,默认为本月
    start_time = time.time()
    print "开始连接数据库...",
    sys.stdout.write('\r')
    # 打开数据库连接
    db = MySQLdb.connect(
        host='192.168.235.36',
        port=3306,
        user='fig',
        passwd='fig',
        db='fig',
        charset='utf8', )

    cursor = db.cursor()
    print "数据库连接成功"

    # 获取Id-用户名 构建用户字典
    print "构造用户名单...",
    sys.stdout.write('\r')
    cursor.execute("SELECT * from sinauser")
    data = cursor.fetchall()
    for row in data:
        id = row[1]
        name = row[2]
        id = int(id)
        User(id=id, name=name)
        if User.Num == user_num:
            break
    print "用户名单构造完毕,共有%i名用户" % User.Num

    # 获取每个用户的关注用户,若不在用户名单 则忽略,接着下一个数据的读取
    print "读取用户的关注名单...",
    sys.stdout.write('\r')
    cursor.execute("SELECT * from gdfollow")
    data = cursor.fetchall()
    for row in data:
        user_id = int(row[1])  # 用户的ID
        follow_id = int(row[2])  # 该用户关注的用户的ID
        try:
            User.Dict[user_id].add_follows(follow_id)
        except KeyError:
            # print "      id:",user_id," 的用户不在用户名单中,关注名单写入失败"
            continue
    print "所有用户的关注写入完成"

    # 获取每个用户的关注用户,若不在用户名单 则忽略,接着下一个数据的读取
    print "读取用户的粉丝名单...",
    sys.stdout.write('\r')
    cursor.execute("SELECT * from gdfan")
    data = cursor.fetchall()
    for row in data:
        user_id = int(row[1])  # 用户的ID
        fan_id = int(row[2])  # 该用户的粉丝的ID
        try:
            User.Dict[user_id].add_fans(fan_id)
        except KeyError:
            # print "      id:",user_id," 的用户不在用户名单中,粉丝名单写入失败"
            continue
    print "所有用户的粉丝写入完成"

    # 获取每个用户的博文,每篇博文由博文内容和博文发布的时间构成
    print "读取用户的所有博文...",
    sys.stdout.write('\r')
    cursor.execute("SELECT * from weibotext WHERE TIME LIKE %s" % ("'" + time_to_analysis + '%' + "'"))
    data = cursor.fetchall()
    for row in data:
        blog_time = row[3]  # 该博文发布的时间
        content = row[2]  # 单条微博博文
        user_id = int(row[1])  # 发该博文的用户ID
        try:
            unit_blog = Blog(content=content, time=blog_time)
            User.Dict[user_id].add_blog(unit_blog=unit_blog)
        except KeyError:
            # print "      id:",user_id," 的用户不在用户名单中,博文写入失败"
            continue
    print "所有用户的博文写入完成"

    db.close()  # 关闭数据库连接
    end_time = time.time()
    print "数据库读取完成 时间:%is" % (end_time - start_time)
    print '----------------------------------'
