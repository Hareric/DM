# coding=utf-8
# #        ┏┓　　　┏┓+ +
# # 　　　┏┛┻━━━┛┻┓ + +
# # 　　　┃　　　　　　　┃ 　
# # 　　　┃　　　━　　　┃ ++ + + +
# # 　　 ████━████ ┃+
# # 　　　┃　　　　　　　┃ +
# # 　　　┃　　　┻　　　┃
# # 　　　┃　　　　　　　┃ + +
# # 　　　┗━┓　　　┏━┛
# # 　　　　　┃　　　┃　　　　　　　　　　　
# # 　　　　　┃　　　┃ + + + +
# # 　　　　　┃　　　┃　　　　Codes are far away from bugs with the animal protecting　　　
# # 　　　　　┃　　　┃ + 　　　　神兽保佑,代码无bug　　
# # 　　　　　┃　　　┃
# # 　　　　　┃　　　┃　　+　　　　　　　　　
# # 　　　　　┃　 　　┗━━━┓ + +
# # 　　　　　┃ 　　　　　　　┣┓
# # 　　　　　┃ 　　　　　　　┏┛
# # 　　　　　┗┓┓┏━┳┓┏┛ + + + +
# # 　　　　　　┃┫┫　┃┫┫
# # 　　　　　　┗┻┛　┗┻┛+ + + +
# """
# Author = Eric_Chan
# Create_Time = 2016/1/19
# """
#
# import xlrd
#
#
# def create_emotion_word(filename):
#     """
#     { 0:disgust,1:sympathy,2:like,3:hate,4:sad,5:happy,6:angry,7:anxiety }
#     :return:{'情绪词':该词对应8大情绪值} 如{'脏乱":[7,0,0,0,0,0,0,0] , ...}
#     """
#     data = xlrd.open_workbook(filename)
#     table = data.sheet_by_index(0)
#     all_data = table._cell_values
#     emotion_dic = {}
#     for i in range(1, table.nrows):
#         mood_value = [0] * 8
#         if all_data[i][4] == u'NN' or all_data[i][4] == u'NK' or all_data[i][4] == u'NL':
#             mood_value[0] = int(all_data[i][5])
#         elif all_data[i][4] == u'PD' or all_data[i][4] == u'PH' or all_data[i][4] == u'PG' or all_data[i][4] == u'PB' or \
#                 all_data[i][4] == u'PK':
#             mood_value[2] == int(all_data[i][5])
#         # elif all_data[i][4] == 'ND':
#         #     mood_value[3] = int(all_data[i][5])
#         # elif all_data[i][4] == 'NB' | all_data[i][4] == 'NJ' | all_data[i][4] == 'NH' | all_data[i][4] == 'PF':
#         #     mood_value[4] = int(all_data[i][5])
#         # elif all_data[i][4] == 'PA' | all_data[i][4] == 'PE':
#         #     mood_value[5] = int(all_data[i][5])
#         # elif all_data[i][4] == 'NA':
#         #     mood_value[6] = int(all_data[i][5])
#         # elif all_data[i][4] == 'NI' | all_data[i][4] == 'NC' | all_data[i][4] == 'NG' | all_data[i][4] == 'NE':
#         #     mood_value[7] = int(all_data[i][5])
#         #
#         # if all_data[i][7] != '':
#         #     if all_data[i][7] == 'NN' | all_data[i][7] == 'NK' | all_data[i][7] == 'NL':
#         #         mood_value[0] = int(all_data[i][5])
#         #     elif all_data[i][7] == 'PD' | all_data[i][7] == 'PH' | all_data[i][7] == 'PG' | all_data[i][7] == 'PB' | \
#         #             all_data[i][7] == 'PK':
#         #         mood_value[2] == int(all_data[i][5])
#         #     elif all_data[i][7] == 'ND':
#         #         mood_value[3] = int(all_data[i][5])
#         #     elif all_data[i][7] == 'NB' | all_data[i][7] == 'NJ' | all_data[i][7] == 'NH' | all_data[i][7] == 'PF':
#         #         mood_value[4] = int(all_data[i][5])
#         #     elif all_data[i][7] == 'PA' | all_data[i][7] == 'PE':
#         #         mood_value[5] = int(all_data[i][5])
#         #     elif all_data[i][7] == 'NA':
#         #         mood_value[6] = int(all_data[i][5])
#         #     elif all_data[i][7] == 'NI' | all_data[i][7] == 'NC' | all_data[i][7] == 'NG' | all_data[i][7] == 'NE':
#         #         mood_value[7] = int(all_data[i][5])
#         emotion_dic[all_data[i][0]] = mood_value
#         print mood_value
#     # for i in emotion_dic:
#     #     print i
#
# if __name__ == '__main__':
#     create_emotion_word('data/emotion_word.xlsx')

# class Kls(object):
#     no_inst = 0
#     def __init__(self):
#         Kls.no_inst = Kls.no_inst + 1
#     @staticmethod
#     def get_no_of_instance():
#         return Kls.no_inst
# # ik1 = Kls()
# # ik2 = Kls()
# # print ik1.get_no_of_instance()
# # print Kls.get_no_of_instance()
import numpy as np
# # # a = np.array([12,12])
# # # b = [1,1]
# # # c = a + b
# # # print c
# # # a = [21, 31, 23, 1, 23, 23, 12]
# # b = np.array([1, 2., 3.])
# # # c = set(a) - (set(a) & set(b))
# # # print c
# # M = max(b)
# # # m = min(b)
# # # print (b-m)/(M-m)
# # for i in range(10):
# #     for j in range(i):
# #         print '(%i,%i)'%(i,j),
# #
print [12].index(2)