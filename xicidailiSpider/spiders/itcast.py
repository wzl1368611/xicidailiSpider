# -*- coding: utf-8 -*-
import scrapy

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/83.0.4103.97 Safari/537.36 '
}


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']

    # start_urls = ['http://www.itcast.cn/']

    def start_requests(self):
        yield scrapy.Request(url='http://www.itcast.cn/', headers=headers,
                             callback=self.parse)

    def parse(self, response):
        #     < div
        #
        #     class ="main_bot" >
        #
        #     < h2 > 王老师 < span > 课程研究员 < / span > < / h2 >
        #     < h3 >
        #     < span > 北大毕业 < / span >
        #
        # < span > 中科软架构师 < / span >
        li_list = response.xpath('//ul[@class="clears cur"]//li')
        # some = response.xpath('//li/div[@class=main_bot]/h2/span/text()')[0]
        # print(some)             # 检查有没有获取到网页
        print('+++++++++++++++++++++++++++++++++++++++++++')
        print(li_list)
        for li in li_list:
            item = {}
            name = li.xpath('.//div[class="main_bot"]/h2/text()').extract_first()
            position = li.xpath('.//div[class="main_bot"]/h3/span/text()').extract_first()
            res = li.xpath('.//div[class="main_bot"]/p/text()').extract_first()
            item['name'] = name
            item['position'] = position
            item['res'] = res
            print(name, position)
            yield item
