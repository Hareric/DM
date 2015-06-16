# coding=utf-8
__author__ = 'Eric_Chan'

import chardet
import urllib
import re

#收集新闻网址
a = []
file = open('News_url.txt','w')
for i in range(1,50,1):
    url = "http://roll.mil.news.sina.com.cn/col/zgjq/index_" + str(i) + ".shtml"
    text = urllib.urlopen(url).read() #读取网址的源代码
    charset = chardet.detect(text) #检测文件编码

    code = charset['encoding']

    text = str(text).decode(code,'ignore').encode("utf-8")
#str.decode('gb2312')#以gb2312编码对字符串str进行解码，以获取unicode
# u.encode('utf-8') #以utf-8编码对unicode对像进行编码
    f = re.findall('http://mil\.news\.sina\.com\.cn/\d{4}.\d{2}.\d{2}.\d*\.html',text)
    for i in range(len(f)):
        a.append(f[i])
        file.writelines(f[i]+'\n')
file.close()
print a
print len(a)



file1 = open(r'News_url.txt')
url_line = 1
for i in range(500):
     url_line = file1.readline()
     text = urllib.urlopen(url_line).read() #读取网址的源代码
     charset = chardet.detect(text) #检测文件编码
     code = charset['encoding']
     text = str(text).decode(code,'ignore').encode("utf-8")
     #获取标题
     pattern0 = re.compile('<title>(.*)</title>')
     f = re.findall(pattern0,text)#获取标题
     title = re.split('\|',f[0]) #以|分隔 第一位为标题
     #获取时间
     pattern1 = re.compile('published at (.*) from')
     time = re.findall(pattern1,text)
     #获取关键字
     pattern2 = re.compile('<meta name=keywords content="(.*)">')
     keyword = re.findall(pattern2,text)
     #获取正文
     pattern3 = re.compile('<p>(.*)</p>')
     description = re.findall(pattern3,text)


     #新建txt 存入标题 时间 关键字 正文
     file2 = open('NEWS/%s.txt'%title[0],'w') #新建文件名为标题的txt
     file2.write('标题:' + title[0] + '\n') #输入标题 换行
     file2.write('时间:' + time[0] + '\n') #输入时间 换行
     file2.write('关键字:' + keyword[0] + '\n')#输入关键字换行
     file2.write('正文:'+'\n')
     for c in range(len(description) - 7): #忽略最后产生的7行乱码
         temp = re.sub('<strong>|</strong>','',description[c]) #将出现在正文的<strong>和</strong>删除掉
         file2.write(temp+'\n')#输入正文

     file2.close()

file1.close()
