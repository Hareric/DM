#coding=utf-8

'''
基于词典的情绪化分法
'''
__author__ = 'Eric_Chan'
import re
import jieba
import chardet
import time

jieba.initialize() #手动启动结巴模块
print '结巴系统启动完毕'
mood_dist = { 0:'厌恶',1:'同情',2:'喜欢',3:'怨恨',4:'悲伤',5:'愉快',6:'愤怒',7:'焦虑',8:'其他'}


def load_word_data(filename):#获得情绪词条词典
    file1 = open('/Users/Har/Desktop/DM/舆情/学习/基于规则的情绪划分/emotion_words/情绪词/%s'%filename,'r')
    line = file1.readline().strip()
    words = []
    while line:
        charset = chardet.detect(line) #检测文件编码
        code = charset['encoding']
        # print code
        line = line.decode(code,'ignore')
        words.append(line)
        line = file1.readline().strip()
    file1.close()

    file2 = open('/Users/Har/Desktop/DM/舆情/学习/基于规则的情绪划分/emotion_words/网络新词/%s'%filename,'r')
    line = file2.readline().strip()
    while line:
        charset = chardet.detect(line) #检测文件编码
        code = charset['encoding']
        line = line.decode(code,'ignore')
        words.append(line)
        line = file2.readline().strip()
    file2.close()

    file3 = open('/Users/Har/Desktop/DM/舆情/学习/基于规则的情绪划分/emotion_words/表情/%s'%filename,'r')
    line = file3.readline().strip()
    while line:
        charset = chardet.detect(line) #检测文件编码
        code = charset['encoding']
        line = line.decode(code,'ignore')
        words.append(line)
        line = file3.readline().strip()
    file3.close()
    return words

def load_symbol(filename):
    biaodian = []
    file3 = open('/Users/Har/Desktop/DM/舆情/学习/基于规则的情绪划分/emotion_words/%s'%filename,'r')
    line = file3.readline().strip()
    while line:
        line = line.decode('utf-8')
        biaodian.append(line)
        line = file3.readline().strip()
    file3.close()
    return biaodian

def blog_crawling(filename):
    file1 = open('/Users/Har/Desktop/weibo_blog/%s'%filename+'.txt','r')
    unit_data = file1.read()
    file1.close()
    pattern0 = re.compile('text:(.*)')
    originText = re.findall(pattern0,unit_data)
    return originText

def load_privativewords(filename):
    file1 = open('/Users/Har/Desktop/DM/舆情/学习/基于规则的情绪划分/emotion_words/否定词/%s'%filename,'r')
    line = file1.readline()
    line = line.split('、')
    words = []
    for i in range(len(line)):
        line[i] = line[i].decode('utf-8')
        words.append(line[i])
    return words

def privativewords_analyze(sentence,No_words,biaodian):
    words_list = {}
    l = len(sentence)
    for i in range(l):
        # print sentence[i]
        if sentence[i] in No_words:
            words_list[i] = sentence[i]

    keys = words_list.keys()
    keys.sort()

    #否定词处理1：若否定词出现在句末，则忽略。   (例：‘我很开心，好不？’  否定词‘不’并没有改变句意)
    for j in keys:
        if (j>=l-2):
        # if (words_list[j] in sentence[-2:])|(sentence[j] in biaodian)|(sentence[j] in biaodian):
            del words_list[j]
            del keys[keys.index(j)]

    #否定词处理2：除去句末的否定词后，若仍存在多个否定词（双重否定），则作为普通句子继续匹配
    canReturn = True #是否可以返回
    if (len(words_list)>=2):

        for j in range(len(keys)-1):
            _bool =False
            temp = sentence[keys[j]:keys[j+1]]
            for i in range(len(temp)):
                if temp[i] in biaodian:#判断连续2个否定词中是否存在标点
                    _bool = True
                    canReturn = False
                    break

            if ((_bool==False)&(j==(len(keys)-2))&(canReturn==True)):#若不存在标点，且为最后一对否定词，则忽略并返回继续运行
                return sentence
            elif (_bool==False):    #若不存在标点，但不为最后一对，则删了这对否定词，继续进行下一组的否定词的判断
                if words_list.has_key(keys[j]):
                    del words_list[keys[j]]
                del words_list[keys[j+1]]
                canReturn = False   #2个否定词之间存在标点，不能返回，必须接下来处理

    #否定词处理3：否定词前后出现的情绪词，作为中性词处理
    keys = words_list.keys()#重新获得处理过后的所有否定词的索引
    for j in keys:
        if j>0:
            sentence[j-1:j+3] = [0]*4 #将否定词的前一位和后一位包括自身的所有词条都归为0（中性词）
        if j==0:
            sentence[j:j+2] = [0]*3
    return sentence

def divide(user_mood,name,mood0,mood1,mood2,mood3,mood4,mood5,mood6,mood7,mood8):
            dd = sorted(user_mood) #情绪值排序
            if dd[8] == 0:#判断若最高情绪值为0，表明没有发表过任何博文，划分为其他社区
                mood = 8
            else:
                mood = user_mood.index(dd[8])#获得最大的情绪值的索引值
                if mood == 8: #若最大情绪值为 其他 时，则选择第二大的的情绪
                    mood = user_mood.index(dd[7])
                    if dd[7] == 0: #若第二大情绪值 为0  ，表明该用户没有发表有效微博 用于分析并划分情绪社区，所以划分为其他社区
                        mood = 8

            #将用户分到对应的社区列表
            if mood == 0:
                mood0.append(name)
            elif mood == 1:
                mood1.append(name)
            elif mood == 2:
                mood2.append(name)
            elif mood == 3:
                mood3.append(name)
            elif mood == 4:
                mood4.append(name)
            elif mood == 5:
                mood5.append(name)
            elif mood == 6:
                mood6.append(name)
            elif mood == 7:
                mood7.append(name)
            elif mood == 8:
                mood8.append(name)

            return mood_dist[mood]

#对一个用户的每条博文进行分析 输入博文（已分好词的列表），输入标点词典，否定词典和8个情绪词典，和8个列表进行统计用户
def eachblog_analyze(filename,originText,No_words,biaodian,yanwu,tongqing,xihuan,yuanheng,beishang,yukuai,fennu,jiaolv,mood0,mood1,mood2,mood3,mood4,mood5,mood6,mood7,mood8,):
        l = len(originText)
        # text_mood = [None for i in range(l)] #记录该用户每条博文的情绪所对应的索引
        user_mood = [0 for k in range(9)] #构建情绪值矩阵
        file2 = open('/Users/Har/Desktop/DM/舆情/学习/基于规则的情绪划分/社区划分/%s'%filename+'.txt','w')
        for i in range(l):#对该用户的每条博文进行分析
            mood_matrix = [ 0 for k in range(8)] #建立 博文数*八大情绪矩阵 顺序为 0：厌恶  1：同情  2：喜欢  3：怨恨  4：悲伤  5：愉快  6：愤怒  7：焦虑
            text_list = list(jieba.cut(originText[i],cut_all=False))
            for j in range(len(text_list)):#对博文的每条词条进行分析，若存在在词库中，则在对应情绪值 加1
                # print text_list[j]
                if text_list[j] in biaodian:#若该词条为标点符号则跳过情绪判断
                    continue
                if text_list[j] in No_words:#若该词为否定词，则对该语句进行否定处理
                    text_list = privativewords_analyze(text_list,No_words,biaodian)
                    continue
                if text_list[j] in yanwu:
                    if j > 0:                                   #若该字条非第一个字条
                        if text_list[j-1] == '[':               #且上一个字条为 '['
                            mood_matrix[0] = mood_matrix[0] + 3 #可判断为表情，情绪值另+3.
                    mood_matrix[0] = mood_matrix[0] + 1         #普通的情绪词则情绪值+1
                elif text_list[j] in tongqing:
                    if j > 0:
                        if text_list[j-1] == '[':
                            mood_matrix[1] = mood_matrix[1] + 3
                    mood_matrix[1] = mood_matrix[1] + 1
                elif text_list[j] in xihuan:
                    if j > 0:
                        if text_list[j-1] == '[':
                            mood_matrix[2] = mood_matrix[2] + 3
                    mood_matrix[2] = mood_matrix[2] + 1
                elif text_list[j] in yuanheng:
                    if j > 0:
                        if text_list[j-1] == '[':
                            mood_matrix[3] = mood_matrix[3] + 3
                    mood_matrix[3] = mood_matrix[3] + 1
                elif text_list[j] in beishang:
                    if j > 0:
                        if text_list[j-1] == '[':
                            mood_matrix[4] = mood_matrix[4] + 3
                    mood_matrix[4] = mood_matrix[4] + 1
                elif text_list[j] in yukuai:
                    if j > 0:
                        if text_list[j-1] == '[':
                            mood_matrix[5] = mood_matrix[5] + 3
                    mood_matrix[5] = mood_matrix[5] + 1
                elif text_list[j] in fennu:
                    if j > 0:
                        if text_list[j-1] == '[':
                            mood_matrix[6] = mood_matrix[6] + 3
                    mood_matrix[6] = mood_matrix[6] + 1
                elif text_list[j] in jiaolv:
                    if j > 0:
                        if text_list[j-1] == '[':
                            mood_matrix[7] = mood_matrix[7] + 3
                    mood_matrix[7] = mood_matrix[7] + 1

            Max = max(mood_matrix)
            g = mood_matrix.index(Max) #返回情绪值最高的索引
            if Max in (mood_matrix[:g]+mood_matrix[g+1:]):#若含有2个最高值，则该情绪定义为其他
                text_mood = 8
            else:
                text_mood = g
            user_mood[text_mood] = user_mood[text_mood] + 1 #在对应的情绪值加一

            #把该用户的具体每条博文写入对应的txt中
            file2.write('博文%i:'%(i+1) + originText[i] + '\n' + '该博文情绪值为:' + mood_dist[text_mood] + '\n'+ '\n')

        mood = divide(user_mood,filename,mood0,mood1,mood2,mood3,mood4,mood5,mood6,mood7,mood8)
        file2.write('\n' + "该用户属于" + mood + '社区')
        file2.close()





def emotional_division(user_num):
    #构建词典
    yanwu    = load_word_data('厌恶.txt')
    tongqing = load_word_data('同情.txt')
    xihuan   = load_word_data('喜欢.txt')
    yuanheng = load_word_data('怨恨.txt')
    beishang = load_word_data('悲伤.txt')
    yukuai   = load_word_data('愉快.txt')
    fennu    = load_word_data('愤怒.txt')
    jiaolv   = load_word_data('焦虑.txt')
    biaodian = load_symbol('biaodian.txt')
    Privative_words = load_privativewords('否定词.txt')

    #构建8个社区的列表
    Mood0 = []  #厌恶社区
    Mood1 = []  #同情社区
    Mood2 = []  #喜欢社区
    Mood3 = []  #怨恨社区
    Mood4 = []  #悲伤社区
    Mood5 = []  #愉快社区
    Mood6 = []  #愤怒社区
    Mood7 = []  #焦虑社区
    Mood8 = []  #其他社区

    jieba.enable_parallel(4)# 开启并行分词模式，参数为并行进程数
    start=time.time()

    for i in range(user_num):#分析多少用户
        texts = blog_crawling('blog%i'%(i+1))
        eachblog_analyze('Divide_result%i'%(i+1),texts,Privative_words,biaodian,yanwu,tongqing,xihuan,yuanheng,beishang,yukuai,fennu,jiaolv,Mood0,Mood1,Mood2,Mood3,Mood4,Mood5,Mood6,Mood7,Mood8)
        print '分析完第%s个用户'%(i+1)

    #将划分的社区写入sum.txt文档
    filet = open('sum%s.txt'%user_num,'w')
    filet.write('--------------------------情  绪  划  分  概  况--------------------------'+'\n')

    filet.write('\n'+'厌恶社区'+'\n')
    for i in range(len(Mood0)):
        filet.write(Mood0[i]+',')
    filet.write('\n'+'该社区共有'+str(len(Mood0))+'人')

    filet.write('\n'+'\n'+'同情社区'+'\n')
    for i in range(len(Mood1)):
        filet.write(Mood1[i]+',')
    filet.write('\n'+'该社区共有'+str(len(Mood1))+'人')

    filet.write('\n'+'\n'+'喜欢社区'+'\n')
    for i in range(len(Mood2)):
        filet.write(Mood2[i]+',')
    filet.write('\n'+'该社区共有'+str(len(Mood2))+'人')

    filet.write('\n'+'\n'+'怨恨社区'+'\n')
    for i in range(len(Mood3)):
        filet.write(Mood3[i]+',')
    filet.write('\n'+'该社区共有'+str(len(Mood3))+'人')

    filet.write('\n'+'\n'+'悲伤社区'+'\n')
    for i in range(len(Mood4)):
        filet.write(Mood4[i]+',')
    filet.write('\n'+'该社区共有'+str(len(Mood4))+'人')

    filet.write('\n'+'\n'+'愉快社区'+'\n')
    for i in range(len(Mood5)):
        filet.write(Mood5[i]+',')
    filet.write('\n'+'该社区共有'+str(len(Mood5))+'人')

    filet.write('\n'+'\n'+'愤怒社区'+'\n')
    for i in range(len(Mood6)):
        filet.write(Mood6[i]+',')
    filet.write('\n'+'该社区共有'+str(len(Mood6))+'人')

    filet.write('\n'+'\n'+'焦虑社区'+'\n')
    for i in range(len(Mood7)):
        filet.write(Mood7[i]+',')
    filet.write('\n'+'该社区共有'+str(len(Mood7))+'人')

    filet.write('\n'+'\n'+'其他社区'+'\n')
    for i in range(len(Mood8)):
        filet.write(Mood8[i]+',')
    filet.write('\n'+'该社区共有'+str(len(Mood8))+'人')

    end=time.time()
    filet.write('\n'+'\n'+'\n'+"              total time is:"+str(int((end-start)))+'s')
    filet.close()
    print('\n'+'\n'+'\n'+"              total time is:"+ str(end-start) + 's')



emotional_division(300)
