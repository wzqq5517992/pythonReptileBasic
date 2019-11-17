# -*- coding: utf-8 -*-
import scrapy
import re
import time
from book.items import MoonLightItem


class MoonlightnextSpider(scrapy.Spider):
    name = 'moonlightnext'
    allowed_domains = ['yuese64.com/']
    start_urls = ['https://yuese64.com/login/']
    headers = {
        "HOST": "www.zhihu.com",
        "Referer": "https://www.zhizhu.com",
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
    }

    def start_requests(self):
        return [scrapy.Request(self.start_urls[0], callback=self.login_ing)]

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response,  # 自动的从response中寻找from表单进行提交
            formdata={"login": "wzqq5517992", "pass": "wzq5517992"},
            callback=self.after_login
        )

    def login_ing(self, response):
        verification_url = response.xpath(
            "//div[@class='captcha-control']//div[@class='image']//img/@src").extract_first()

        t = str(int(time.time() * 1000))
        hou = "?rand={0}".format(t)
        print("验证码获取地址：", verification_url)
        yield scrapy.Request(
            verification_url,
            callback=self.login_after_captcha  # 回调方法
            # meta={"item": item}  # 回调入参
        )

    def login_after_captcha(self, response):
        print(response.status_code)
        with open("G:\\wzq\\captcha.jpg", "wb") as f:
            f.write(response.body.decode)
            f.close()
        with open("G:\\wzq\\captcha.jpg", "w", encoding="utf-8") as f:
            f.write(response.body)

    def after_login(self, response):
        print(re.findall("您好", response.body.decode()))
        print(re.findall("wzq5517992@163.com|Wzq5517992@163.com", response.body.decode()))
