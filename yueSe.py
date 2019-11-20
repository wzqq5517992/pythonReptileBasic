# -*- coding: utf-8 -*-
import scrapy


class YueSeSpider(scrapy.Spider):
    name = 'yueSe'
    allowed_domains = ['yuese64.com']
    start_urls = ['http://yuese64.com/login/']

    def parse(self, response):
        post_data = dict(
            username="wzq5517992@163.com",
            passs="wzq5517992",
            action="login",
            format="json",
            mode="async",
            code="",
            email_link="https://yuese64.com/email/"
        )

        yield scrapy.FormRequest.from_response(
            response,  # 自动的从response中寻找from表单
            formdata={"username": "wzq5517992@163.com", "password": "wzq5517992"},
            callback=self.after_login
        )
