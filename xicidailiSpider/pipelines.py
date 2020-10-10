# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class XicidailispiderPipeline:
    def process_item(self, item, spider):
        if spider.name == 'zhihu':
            pass
        print(item)
        item['hello'] = 'world'
        return item


class XicidailispiderPipeline1:
    def process_item(self, item, spider):
        if spider.name == 'itcast':  # 分别处理不同spider传过来的数据

            print(item)
        return item

