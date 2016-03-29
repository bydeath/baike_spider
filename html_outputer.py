#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ===================================================================
#     FileName: html_outputer.py
#       Author: bruc14
#        Email: bruc14@163.com
#   CreateTime: 2016-03-29 00:57
# ===================================================================

class HtmlOutputer(object):
    def __init__ (self):
        self.datas = []

    def collect_data (self, data):
        if data is not None:
            self.datas.append(data)
        else:
            return

    def output_html (self):
        fout = open('output.html', 'w')
        fout.write( "<html>")
        fout.write( "<head>")
        fout.write('<meta http-equiv="content-type" content="text/html; charset=UTF-8" >')
        fout.write( "</head>")

        fout.write( "<body>")
        fout.write( "<table>")
        for data in self.datas:
            fout.write("\n<tr>")
            fout.write("\n<td>%s</td>"%data['url'].encode('utf-8'))
            fout.write("\n<td>%s</td>"%data['title'].encode('utf-8'))
            fout.write("\n<td>%s</td>"%data['summary'].encode('utf-8'))
            fout.write("\n</tr>")
        fout.write( "</table>")
        fout.write( "</body>")
        fout.write( "</html>")
        fout.close()
