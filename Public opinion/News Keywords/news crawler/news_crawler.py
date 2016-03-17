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
Create_Time = 2016/03/16
introduction:
爬取新浪滚动新闻
"""
import urllib2
import re
from BeautifulSoup import BeautifulSoup
import chardet


class SinaNewsCrawler:
    def __init__(self, num=100):
        """
        :param num: 爬取新闻的个数
        :return:
        """
        self.url = 'http://roll.news.sina.com.cn/s/channel.php?ch=01&num=' + str(num)
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6)'
                                     ' Gecko/20091201 Firefox/3.5.6'}
        self.news_url_list = []  # 新闻对应的url列表
        self.__get_news_url()

    def __get_news_url(self):
        """
        获得新浪滚动新闻的url
        :return:
        """
        req = urllib2.Request(url=self.url,
                              headers=self.header)
        res = urllib2.urlopen(req).read()
        res = unicode(res, 'GBK')
        soup = BeautifulSoup(res)
        all_news_url = soup.find("div", attrs={'id': 'd_list'}).findAll('a', attrs={'target': "_blank"})
        pattern_news_url = re.compile('href="(.*?)"')
        for each_news_url in all_news_url:
            self.news_url_list.append(re.findall(pattern_news_url, str(each_news_url))[0])
        print 'Get url finished!'

    def get_content(self, url):
        """
        获取新闻的详细内容
        :param url: 新闻的网址
        :return: content (保留 <p> 分段标识符)
        """
        req = urllib2.Request(url=url,
                              headers=self.header)
        res = urllib2.urlopen(req).read()
        type_encoding = chardet.detect(res)['encoding']  # 检测网页的编码
        if type_encoding is None:
            return None
        soup = BeautifulSoup(res)
        try:
            p_list = soup.find('div', attrs={'id': 'artibody'}).findAll('p')
        except AttributeError:  # 该页访问出错
            return None
        return_content = ''
        for p in p_list:
            return_content += str(p)
            return_content += '\n'
        return return_content


if __name__ == '__main__':
    Crawler = SinaNewsCrawler(num=500)
    i_num = 1
    for news_url in Crawler.news_url_list:
        print news_url
        content = Crawler.get_content(news_url)
        if content is not None:
            file_i = open('News/news_%i.txt' % i_num, 'w')
            file_i.write(str(content))
            file_i.close()
            i_num += 1

    # print SinaNewsCrawler().get_content('http://news.sina.com.cn/c/2016-03-17/doc-ifxqnnkr9399615.shtml')

