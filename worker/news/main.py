# -*- coding: utf-8 -*-
'''
Created on 2018-07-04 15:45
---------
@summary: 从master中取网页首地址
---------
@author: Boris
'''


import sys
sys.path.append('../')
import init
import pid
pid.record_pid(__file__)
import utils.tools as tools
from utils.log import log
from base.spider import Spider
from utils.export_data import ExportData

# 需配置
from news.parsers import *

def main():
    def begin_callback():
        log.info('\n********** news begin **********')

    def end_callback():
        log.info('\n********** news end **********')

    # 配置spider
    spider = Spider(tab_urls = 'news:news_urls', begin_callback = begin_callback, end_callback = end_callback)

    # 添加parser
    spider.add_parser(news_parser)

    spider.start()

if __name__ == '__main__':
    main()