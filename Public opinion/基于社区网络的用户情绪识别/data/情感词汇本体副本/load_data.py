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

import xlrd


def create_emotion_word(filename):
    """
    { 0:disgust,1:sympathy,2:like,3:hate,4:sad,5:happy,6:angry,7:anxiety }
    :return:{'情绪词':该词对应8大情绪值} 如{'脏乱":[7,0,0,0,0,0,0,0] , ...}
    """
    data = xlrd.open_workbook(filename)
    table = data.sheet_by_index(0)
    all_data = table._cell_values
    emotion_dic = {}
    for i in range(1, table.nrows):
        mood_value = [0] * 8
        if all_data[i][4] == u'NN' or all_data[i][4] == u'NK' or all_data[i][4] == u'NL':
            mood_value[0] += int(all_data[i][5])
        elif all_data[i][4] == u'PD' or all_data[i][4] == u'PH' or all_data[i][4] == u'PG' or all_data[i][4] == u'PB' or \
                        all_data[i][4] == u'PK':
            mood_value[2] += int(all_data[i][5])
        elif all_data[i][4] == u'ND':
            mood_value[3] += int(all_data[i][5])
        elif all_data[i][4] == u'NB' or all_data[i][4] == u'NJ' or all_data[i][4] == u'NH' or all_data[i][4] == u'PF':
            mood_value[4] += int(all_data[i][5])
        elif all_data[i][4] == u'PA' or all_data[i][4] == u'PE':
            mood_value[5] += int(all_data[i][5])
        elif all_data[i][4] == u'NA':
            mood_value[6] += int(all_data[i][5])
        elif all_data[i][4] == u'NI' or all_data[i][4] == u'NC' or all_data[i][4] == u'NG' or all_data[i][4] == u'NE':
            mood_value[7] += int(all_data[i][5])

        if all_data[i][7] != ' ':
            if all_data[i][7] == u'NN' or all_data[i][7] == u'NK' or all_data[i][7] == u'NL':
                mood_value[0] += int(all_data[i][8])
            elif all_data[i][7] == u'PD' or all_data[i][7] == u'PH' or all_data[i][7] == u'PG' or all_data[i][
                7] == u'PB' or \
                            all_data[i][7] == u'PK':
                mood_value[2] += int(all_data[i][8])
            elif all_data[i][7] == u'ND':
                mood_value[3] += int(all_data[i][8])
            elif all_data[i][7] == u'NB' or all_data[i][7] == u'NJ' or all_data[i][7] == u'NH' or all_data[i][
                7] == u'PF':
                mood_value[4] += int(all_data[i][8])
            elif all_data[i][7] == u'PA' or all_data[i][7] == u'PE':
                mood_value[5] += int(all_data[i][8])
            elif all_data[i][7] == u'NA':
                mood_value[6] += int(all_data[i][8])
            elif all_data[i][7] == u'NI' or all_data[i][7] == u'NC' or all_data[i][7] == u'NG' or all_data[i][
                7] == u'NE':
                mood_value[7] += int(all_data[i][8])
        emotion_dic[all_data[i][0]] = mood_value
        # print mood_value

    return emotion_dic


if __name__ == '__main__':
    dic = create_emotion_word('data/emotion_word.xlsx')
    f = open("emotion_dic.txt", 'w')
    words = dic.keys()
    for w in words:
        print w
        f.write(w.encode('utf8') + '\t')
        for i in range(8):
            f.write(str(dic[w][i]) + '\t')
        f.write('\n')
    f.close()
