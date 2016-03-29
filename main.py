#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ===================================================================
#     FileName: main.py
#       Author: bruc14
#        Email: bruc14@163.com
#   CreateTime: 2016-03-28 23:37
# ===================================================================
import url_manager, html_downloader, html_parser, html_outputer
import traceback
import pdb
class SpiderMain(object):
    def __init__ (self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw (self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print("craw %d: %s"%(count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
            except Exception as e:
                print("craw failed")
                print(traceback.print_exc())
                print(e)
            if count == 1000:
                break
            count += 1
        self.outputer.output_html()
        
if __name__ == '__main__':
    root_url = "http://baike.baidu.com/view/13621.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)