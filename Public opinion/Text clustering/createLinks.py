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
Create_Time = 2016/03/12
introduction:
若博文1与博文2共同存在一个词,则博文1与博文2之间的关系权值为1 link = [1, 2, 1]
"""

import numpy
import jieba


class Link:
    def __init__(self, blog_list, vocab_list):
        self.links = []  # 记录博文之间的权值矩阵
        self.blog_list = blog_list  # 博文列表
        self.vocab_list = vocab_list  # 词库列表

    def word_link(self, word_blog_array):
        """
        博文与博文之间若存在共同词,则这2两篇博文之间的权值+1
        :param word_blog_array: 基于某词的博文索引列表  如 [0, 1, 1, 0] 表示博文1与博文2存在该词
        """
        index_list = numpy.where(word_blog_array == 1)[0]
        for i in index_list:
            for j in index_list:
                if i == j:
                    continue
                else:
                    self.links.append([i, j, 1])

    def create_vector(self, text):
        """
        输入一条博文,返回基于词库的向量
        :param text: 已分词的一条博文
        :return: 博文向量
        """
        blog_word_list = jieba.cut(text)
        return_vec = [0] * len(self.vocab_list)
        for word in blog_word_list:
            if word in self.vocab_list:
                return_vec[self.vocab_list.index(word)] = 1
        return return_vec

    def create_blog_vector_matrix(self):
        """
        创建博文的向量矩阵
        :return: 博文的向量矩阵
        """
        blog_vector_matrix = []
        for blog in self.blog_list:
            blog_vector_matrix.append(self.create_vector(blog))
        return numpy.array(blog_vector_matrix)

    def get_links(self):
        blog_vector_matrix = self.create_blog_vector_matrix()
        for word_index in range(len(self.vocab_list)):
            # print blog_vector_matrix[:, word_index]
            self.word_link(blog_vector_matrix[:, word_index])
        return self.links


# if __name__ == '__main__':
#     blogs = load_data('dataSet/text.txt')
#     vocab = Vocab(blogs, each_get_num=5).get_vocab()
#     links = Link(blog_list=blogs, vocab_list=vocab).get_links()
#     for word in vocab:
#         print word,
#     for i in links:
#         print i
