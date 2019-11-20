# -*- coding: utf-8 -*-
import scrapy
import re


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    # start_urls = ['http://www.renren.com/327550029/profile']
    start_urls = ['http://www.renren.com/972796369/profile']

    def start_requests(self):
        # cookies = "anonymid=jcokuqturos8ql; depovince=GW; jebecookies=f90c9e96-78d7-4f74-b1c8-b6448492995b|||||; _r01_=1; JSESSIONID=abcx4tkKLbB1-hVwvcyew; ick_login=ff436c18-ec61-4d65-8c56-a7962af397f4; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; p=90dea4bfc79ef80402417810c0de60989; first_login_flag=1; ln_uact=mr_mao_hacker@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn421/20171230/1635/main_JQzq_ae7b0000a8791986.jpg; t=24ee96e2e2301bf2c350d7102956540a9; societyguester=24ee96e2e2301bf2c350d7102956540a9; id=327550029; xnsid=e7f66e0b; loginfrom=syshome; ch_id=10016"
        cookies = "anonymid=k2nc34qa5q5z5r; _r01_=1; _ga=GA1.2.1281449736.1573048142; depovince=GW; jebecookies=6cd6f2da-0f32-4c96-8d36-1776dcdf9733|||||; JSESSIONID=abcqR6QYFkVx2cL0DSP5w; ick_login=be71047c-045c-47d3-8fe3-cf399634b777; _de=4C2E496AB1A9F8CDB1141F0AB71777CB; p=2ea3c4bcf6b25d3ee65464c38747462f9; first_login_flag=1; ln_uact=17733469095; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=e929838686f3376830666800dbd1ef1d9; societyguester=e929838686f3376830666800dbd1ef1d9; id=972796369; xnsid=964dd951; jebe_key=854cac39-eeec-4555-b3e5-45d769dfdbf9%7Ce136b865e2fccf2f88643d2dd093a69e%7C1573731314586%7C1%7C1573731317961; jebe_key=854cac39-eeec-4555-b3e5-45d769dfdbf9%7Ce136b865e2fccf2f88643d2dd093a69e%7C1573731314586%7C1%7C1573731317964; wp_fold=0; ver=7.0; loginfrom=null"
        cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}

        # headers = {"Cookie":cookies}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
            # headers = headers
        )

    def parse(self, response):
        # print(re.findall("魏志强", response.body.decode()))
        yield scrapy.Request(
            "http://www.renren.com/972796369/profile?v=info_timeline",
            callback=self.parse_detial
        )

    def parse_detial(self, response):
        print(re.findall("魏志强", response.body.decode()))
