# -*- coding: utf-8 -*-
import scrapy
import logging
logger = logging.getLogger(__name__)


class Demo01Spider(scrapy.Spider):
    name = 'demo01'  # 爬虫名称
    allowed_domains = ['itcast.cn']  # 允许爬取的网址范围
    start_urls = ['http://itcast.cn/channel/teacher.shtml']  # 最开始爬取的url

    def parse(self, response):
        # ret = response.xpath("//div[@class='tea_con']//li//h3/text()").extract()
        # print(ret)

        li_list = response.xpath("//div[@class='tea_con']//li")
        for li in li_list:
            item = {
                "name": li.xpath(".//h3/text()").extract()[0],
                "title": li.xpath(".//h4/text()").extract()[0]

            }
            yield item
            logging.info("结束爬取")
