# coding=utf-8

import urllib2
import json
import time
import chardet

header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Ubuntu Chromium/49.0.2623.108 Chrome/49.0.2623.108 Safari/537.36'}
url = 'http://club.jd.com/productpage/p-1748176-s-0-t-3-p-%d.html'


for i in range(200):
    print "---\npage%i" % i
    req = urllib2.Request(url % i, headers=header)
    res = urllib2.urlopen(req).read()
    while not res.startswith('{"productAttr'):
        print '无response值 重新请求'
        res = urllib2.urlopen(req).read()
        time.sleep(5)
    encoding_type = chardet.detect(res)['encoding']
    try:
        res = unicode(res, encoding_type, 'ignore')
    except UnicodeDecodeError:
        print '编码有误'
    res = json.loads(res)

    for i in res['comments']:
        print 'nickname:', i['nickname']
        print 'content:', i['content']

