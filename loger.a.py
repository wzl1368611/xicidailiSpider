#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2020-8-9 23:11:00
# version: 1.0
# __author__: zhilong
import logging
# logging 模块的使用
# logging.basicConfig()
logging.basicConfig(level=logging.INFO,
                    filename='./log.txt',
                    filemode='w',
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

loger = logging.getLogger(__name__)
if __name__ == '__main__':
    loger.info('this is a loger info')
    loger.info('this is a loger b')
