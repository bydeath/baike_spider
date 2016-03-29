#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ===================================================================
#     FileName: urllib2Test.py
#       Author: bruc14
#        Email: bruc14@163.com
#   CreateTime: 2016-03-28 23:25
# ===================================================================

import urllib2, cookielib
url = "http://www.baidu.com"
print"第一种方法"
response1 = urllib2.urlopen(url)
print response1.getcode()
print len(response1.read())

print"第二种方法"
request = urllib2.Request(url)
request.add_header("user-agent", "Mozilla/5.0")
response2 = urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())

print"第三种方法"

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(request)
print response3.getcode()
print(cj)
print len(response3.read())
