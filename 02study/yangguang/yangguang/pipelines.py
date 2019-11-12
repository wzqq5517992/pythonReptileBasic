# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
from yangguang.settings import MONGO_HOST
from pymongo import MongoClient
import logging
logger = logging.getLogger(__name__)


class YangguangPipeline(object):
    def open_spider(self, spider):
        # spider.hello = "world"
        client = MongoClient()
        self.collection = client["test"]["test"]

    def process_item(self, item, spider):
        logger.warning("=============")
        logging.warning(item)
        print("=======")
        spider.settings.get("MONGO_HOST")
        item["content"] = self.process_content(item["content"])
        print(item)

        self.collection.insert(dict(item))
        return item

    def process_content(self, content):
        content = [re.sub(r"\xa0|\s", "", i) for i in content]  # 正则过滤空字符串及无效字符串
        content = [i for i in content if len(i) > 0]  # 去除列表中的空字符串
        return content
