# coding=utf-8


def create_emotion_dictionary(filename):
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


emotion_dic = create_emotion_dictionary('emotion_dic.txt')
moodDict = {0: 'disgust', 1: 'sympathy', 2: 'like', 3: 'hate', 4: 'sad', 5: 'happy', 6: 'angry',
            7: 'anxiety'}


def loadData(i):  # 读取文字
    fileName = "emotion_words/%s.txt" % str(moodDict[i])
    file1 = open(fileName, 'r')
    line = file1.readline().strip()
    words = []
    while line:
        line = line.decode('utf-8')
        words.append(line)
        line = file1.readline().strip()
    file1.close()
    return words


for i in range(8):
    words = loadData(i)
    for word in words:
        if not emotion_dic.has_key(word):
            emotion_dic[word] = [0] * i + [5] + [0] * (7 - i)

f = open("emotion_dic.txt", 'w')
words = emotion_dic.keys()
for w in words:
    f.write(w.encode('utf8') + '\t')
    for i in range(8):
        f.write(str(emotion_dic[w][i]) + '\t')
    f.write('\n')
f.close()
