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
    Create_Time = 2016/03/17
    introduction:
    获得新闻的关键词
    """
import jieba
import numpy
import igraph


def load_data(file_name):
    """
        读取文件,获得列表
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


class KeyWords:
    def __init__(self):
        self.stop_words_list = load_data('dataSet/stop_words.txt')  # 停用词
        space = [u' ', u'　']
        self.stop_words_list += space
    
    def __text_process(self, text):
        """
            对导入的文章进行分词和去除停用词处理,并按照段落,划分为二元列表
            :return:
            """
        # pattern_paragraph = re.compile('<[Pp]>(.*?)</[Pp]>')
        # paragraph_list = re.findall(pattern_paragraph, text)
        paragraph_list = text.split('\n')
        return_text = []
        for paragraph in paragraph_list:
            paragraph_words = []
            for w in jieba.cut(paragraph):
                if w in self.stop_words_list:  # 去除停用词
                    continue
                elif w.__len__() == 1:
                    continue  # 单个字不作关键词分析
                else:
                    paragraph_words.append(w)
            return_text.append(paragraph_words)
        return return_text
    
    @staticmethod
    def create_vocab_list(text_matrix):
        """
            创建词库
            :param text_matrix: 一篇文章分段分词的文字矩阵
            :return:
            """
        return_vocab_list = []
        for p in text_matrix:
            return_vocab_list += p
        return return_vocab_list
    
    class Link:
        def __init__(self, vocab_list, text_matrix):
            """
                :param vocab_list: 词库列表
                :param text_matrix: 分段分词矩阵
                :return: 向量矩阵
                """
            self.vocab_list = vocab_list
            self.text_matrix = text_matrix
            self.links = []
        
        def __create_vector(self, text):
            """
                输入一段文字,返回基于词库的向量
                :param text: 已分词的一条博文
                :return: 向量
                """
            return_vec = [0] * len(self.vocab_list)
            for word in text:
                if word in self.vocab_list:
                    return_vec[self.vocab_list.index(word)] = 1
            return return_vec
        
        def __create_text_vector_matrix(self):
            """
                创建一篇文章的向量矩阵
                :return: 文章的向量矩阵
                """
            text_vector_matrix = []
            for p in self.text_matrix:
                text_vector_matrix.append(self.__create_vector(p))
            return numpy.array(text_vector_matrix)
        
        def __word_link(self, paragraph_vec):
            """
                段落中若有两个词共现,则这两个词之间的权值+1
                :param paragraph_vec: [0, 1, 0, 2] 表示 vocab[1] 在本段出现1次, vocab[3] 在本段出现了2词
                """
            index_list = numpy.where(paragraph_vec > 0)[0]
            for i in index_list:
                for j in index_list:
                    if i == j:
                        continue
                    else:
                        self.links.append([i, j, max([paragraph_vec[i], paragraph_vec[j]])])
        
        def get_links(self):
            text_vector_matrix = self.__create_text_vector_matrix()
            for paragraph_vec in text_vector_matrix:
                # print blog_vector_matrix[:, word_index]
                self.__word_link(paragraph_vec)
            return self.links

class Graph:
    def __init__(self, vocab_list, links):
        self.node_value_dict = {}  # 节点的中心度值
            self.vocab_list = vocab_list
            self.__create_graph(word_num=len(vocab_list), links=links)
    
        def __create_graph(self, word_num, links):
            """
                使用igraph构建图
                :param word_num: 词库的词的个数
                :links: 词与词
                :return: graph, weights list
                """
            g = igraph.Graph(word_num)
            weights = []
            edges = []
            for line in links:
                edges += [(line[0], line[1])]
                weights.append(line[2])
            g.add_edges(edges)
            node_value = g.authority_score(weights=weights)
            self.node_value_dict = dict(zip(range(word_num), node_value))
        
        def get_centrality(self, num=None):
            """
                :param num: the number of the centrality will be got
                :return: the centrality of the cluster
                """
            if num is None:
                num = 1
            centrality_dict = {}  # 核心节点的 id:中心度值
            for node in range(len(self.vocab_list)):
                if centrality_dict.__len__() < num:
                    centrality_dict[node] = self.node_value_dict[node]
                elif self.node_value_dict[node] > min(centrality_dict.values()):
                    centrality_dict = {k: v for k, v in centrality_dict.iteritems()
                        if v != min(centrality_dict.values())}  # 移去最小值
                    centrality_dict[node] = self.node_value_dict[node]
            return centrality_dict.keys()

def get_keywords(self, content, num=None):
    """
        :param content: 一篇文章
        :param num: 提取关键词的个数
        :return: 关键词列表
        """
            if num is None:
            num = 5
                content = self.__text_process(content)
                    vocab = self.create_vocab_list(content)
                        links = self.Link(vocab_list=vocab, text_matrix=content).get_links()
                            nodes = self.Graph(vocab_list=vocab, links=links).get_centrality(num)
                                keyword_list = []
                                    for node in nodes:
                                        keyword_list.append(vocab[node])
                                            return keyword_list


if __name__ == '__main__':
    news = open('dataSet/Text/news_33.txt', 'r').read()
    KW = KeyWords()
    f = open('test_result.txt', 'w')
    for i in range(36)[1:]:
        news = open('dataSet/Text/news_%i.txt' % i, 'r').read()
        keywords = KW.get_keywords(news)
        print ' '.join(keywords)
        f.write(news + '\n')
        f.write('关键词:\n')
        f.write(' '.join(keywords).encode('utf-8'))
        f.write('\n' + '-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n\n')

# news = open('news.txt', 'r').read()
# KW = KeyWords()
# print ' '.join(KW.get_keywords(news))