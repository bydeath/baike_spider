#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ===================================================================
#     FileName: html_downloader.py
#       Author: bruc14
#        Email: bruc14@163.com
#   CreateTime: 2016-03-28 23:59
# ===================================================================
import urllib2
class HtmlDownloader(object):
    def download (self, url):
        if url is not None:
            response = urllib2.urlopen(url)
            if response.getcode() != 200:
                return None
            return response.read()
        else:
            return None
