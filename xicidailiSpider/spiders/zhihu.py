# -*- coding: utf-8 -*-
import scrapy
import logging
loger = logging.getLogger(__name__)

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['http://zhihu.com/']
    custom_settings = {
        'COOKIES_ENABLED': True,
    }

    def parse(self, response):
        for i in range(10):
            item = {}
            item['hello'] = 'world'
            item['come_from'] = 'zhihu'
            loger.warning(item)

