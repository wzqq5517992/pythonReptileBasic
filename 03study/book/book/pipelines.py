# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
class BookPipeline(object):
    # 爬虫开始时执行一次
    def open_spider(self, spider):
        MONGO_HOST = spider.settings.get("MONGO_HOST")
        client = MongoClient(host=MONGO_HOST, port=27017)
        self.collection = client["test"]["test"]

    def process_item(self, item, spider):
        print(item)
        # 插入一条数据
        self.collection.insert(dict(item))
        return item
