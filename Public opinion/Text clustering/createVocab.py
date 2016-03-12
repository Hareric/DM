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
Create_Time = 2016/03/11
introduction:
从博文数据集中,提取每条博文的关键词并取并集获得关键词词库列表
"""

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import jieba


def load_data(file_name):
    """
    读取文件,获得博文列表
    :param file_name: 文件路径
    :return: 博文列表
    """
    file_0 = open(file_name, 'r')
    text_list = []
    line = file_0.readline().strip()
    while line:
        if not line.strip():
            line = file_0.readline()
            continue
        text_list.append(line.decode('utf-8').strip())
        line = file_0.readline()
    return text_list


class Vocab:
    def __init__(self, blog_text, each_get_num=None):
        self.blog_list = blog_text  # 博文列表
        self.stop_words = load_data('dataSet/stop_words.txt')  # 停用词列表
        if each_get_num is None:
            self.each_get_num = 3  # 每条博文提取关键词的个数
        else:
            self.each_get_num = each_get_num

    @staticmethod
    def calculate_tf_idf(text_list_cut):
        """
        计算每篇文本中出现的词语的TF-IDF
        :param text_list_cut: 已分词的文本矩阵(每条文本的分词结果用空格隔开)
        :return: 词语列表, tf_idf 矩阵
        """
        vectorized = CountVectorizer()
        transformer = TfidfTransformer()
        word_frequency_matrix = vectorized.fit_transform(text_list_cut)  # 将文本中的词语转换为词频矩阵
        tf_idf = transformer.fit_transform(word_frequency_matrix)  # 根据词频矩阵计算tf-idf
        word_list = vectorized.get_feature_names()  # 获取词袋模型中的所有词语
        weight_array = tf_idf.toarray()  # 将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重
        # for i in range(len(weight_array)):
        #     print "-------这里输出第", i + 1, "类文本的词语tf-idf权重------"
        #     for j in range(len(word_list)):
        #         print word_list[j], weight_array[i][j]
        return word_list, weight_array

    def __create_blog_list_cut(self):
        """
        对输入的博文列表进行分词处理,并去除停用词
        :return: 已分词博文列表
        """
        blog_list_cut = []
        for blog in self.blog_list:
            blog_cut = jieba.cut(blog)  # 对每条博文进行分词
            blog_cut_new = []
            for w in blog_cut:  # 去除停用词
                if w in self.stop_words:
                    continue
                blog_cut_new.append(w)
            blog_list_cut.append(" ".join(blog_cut_new))
        return blog_list_cut

    def create_vocab_list(self, words, weights):
        """
        提取每条文章的tf_idf最高的值作为关键词, 并将所有关键词组合成为一个关键词库
        :param words: 原词库
        :param weights: 权值矩阵
        :return: 关键词列表
        """
        index_list = []  # 记录关键词的索引列表
        for weight in weights:
            weight = weight.tolist()
            index_team = []  # 记录一条博文提取到的关键词索引
            while index_team.__len__() < self.each_get_num:
                max_index = weight.index(max(weight))
                index_team.append(max_index)
                del weight[max_index]
            index_list += index_team
        index_list = set(index_list)  # 消重
        word_list = []  # 关键词列表
        for i in index_list:
            word_list.append(words[i])
        return word_list

    def get_vocab(self):
        """
        获取关键词词库
        :return:
        """
        blog_list_cut = self.__create_blog_list_cut()
        word_list, weight_array = Vocab.calculate_tf_idf(blog_list_cut)
        vocab = self.create_vocab_list(words=word_list, weights=weight_array)
        return vocab


# if __name__ == '__main__':
#     vocab_list = Vocab(load_data('dataSet/text.txt')).get_vocab()
#     for word in vocab_list:
#         print word
#     print vocab_list.__len__()
