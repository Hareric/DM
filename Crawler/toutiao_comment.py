# coding=utf-8
import urllib2
import re
content = urllib2.urlopen('http://toutiao.com/group/6282837243963048194/comments/?count=901&format=json').read()
comment = re.findall('"text": "(.*?)",', content)
for index, j in enumerate(comment):
    print index, '\n', j.decode('unicode-escape').encode('utf-8')
