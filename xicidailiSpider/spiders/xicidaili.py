# -*- coding: utf-8 -*-
import scrapy
import time


class XicidailiSpider(scrapy.Spider):
    name = 'kuaidaili'
    allowed_domains = ['kuaidaili.com']
    start_urls = ['https://www.kuaidaili.com/free/inha/1/',
                  ]

    # def start_requests(self):
    #     for page in range(1, 4):
    #         start_url = 'https://www.kuaidaili.com/free/inha/{}'.format(page)
    #         print(start_url, '-------------------')
    #         yield scrapy.Request(url=start_url, callback=self.parse)

    def parse(self, response):
        print(response.url)
        # 提取数据
        # 提取ip
        address = ''
        selectors = response.xpath('//tbody/tr')
        for selector in selectors:
            ip = selector.xpath('./td[1]/text()').getall()[0]
            port = selector.xpath('./td[2]/text()').getall()[0]
            address = address + ip + ' ' + port + '\n'
            # ip = selector.xpath('./td[1]/text()').extract_first()
            # port = selector.xpath('./td[2]/text()').extract_first()
            print(ip, port)

            # items = {
            #     'ip': ip,
            #     'port': port
            # }
            # yield items

        with open('ip_proxies_002.txt', 'a') as f:
            f.write(address)

        # base_url = 'https://www.kuaidaili.com'
        next_urls = response.xpath("//div[@id='listnav']/ul/li/a/@href").getall()
        if next_urls:
            for next_url in next_urls:
                uurl = response.urljoin(next_url)
                time.sleep(0.5)
                yield scrapy.Request(url=uurl, callback=self.parse)



