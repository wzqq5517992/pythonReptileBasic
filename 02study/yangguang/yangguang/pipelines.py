# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
from yangguang.settings import MONGO_HOST as ffff
from pymongo import MongoClient
import logging

logger = logging.getLogger(__name__)


class YangguangPipeline(object):
    # 爬虫开始时执行一次
    def open_spider(self, spider):
        MONGO_HOST = spider.settings.get("MONGO_HOST")
        client = MongoClient(host=MONGO_HOST, port=27017)
        self.collection = client["test"]["test"]

    def process_item(self, item, spider):
        item["content"] = self.process_content(item["content"])
        print(item)

        # 插入一条数据
        self.collection.insert(dict(item))
        return item

    def process_content(self, content):
        content = [re.sub(r"\xa0|\s", "", i) for i in content]  # 正则过滤空字符串及无效字符串
        content = [i for i in content if len(i) > 0]  # 去除列表中的空字符串
        return content
