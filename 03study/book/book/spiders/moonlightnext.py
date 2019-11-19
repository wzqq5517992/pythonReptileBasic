# -*- coding: utf-8 -*-
import scrapy
import re
import time
from book.items import MoonLightItem
from book.utils.captcha_image import getImage
import book.utils.yundama_requests   as  code


def do_ydm():
    username = 'wzqq5517992'  # 用户名
    password = 'wzq5517992'  # 密码
    appid = 9474  # 软件ＩＤ，开发者分成必要参数。登录开发者后台【我的软件】获得！
    appkey = 'b52011394e2ec6e7631626ee3f622c2e'  # 软件密钥，开发者分成必要参数。登录开发者后台【我的软件】获得！
    filename = "F:\\MyOwnCode\\pythonStudy\\pythonReptileBasic\\03study\\book\\book\\images\\captcha.jpg"  # 图片文件
    # 验证码类型，# 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。在此查询所有类型 http://www.yundama.com/price.html
    codetype = 5000  # 超时时间，秒
    timeout = 60
    # 初始化
    yundama = code.YDMHttp(username, password, appid, appkey)
    # 登陆云打码
    uid = yundama.login();
    print('uid: %s' % uid)
    # 登陆云打码
    uid = yundama.login();
    print('uid: %s' % uid)
    # 查询余额
    balance = yundama.balance();
    print('balance: %s' % balance)
    # 开始识别，图片路径，验证码类型ID，超时时间（秒），识别结果
    text = yundama.decode(filename, codetype, timeout);
    print("验证码结果为:", text)
    return text


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
            formdata={"username": "wzq5517992@163.com", "pass": "wzq5517992", "code": text},
            callback=self.after_login
        )

    def login_ing(self, response):
        global text
        # verification_url = response.xpath("//div[@class='captcha-control']//div[@class='image']//img/@src").extract_first()
        verification_url = "https://yuese64.com/captcha/logon/"
        print("验证码获取地址：", verification_url)
        post_data = {
            "username": "wzq5517992@163.com",
            "pass": "wzq5517992",
            "code": ""
        }

        # code = getImage()
        # if code == "success":
        #     text = do_ydm()
        yield scrapy.Request(
            verification_url,
            meta={"post_data": post_data},
            callback=self.login_after_captcha
        )

    def login_after_captcha(self, response):
        with open("captcha.jpg", "wb") as f:
            f.write(response.body)
            f.close()

    # def after_login(self, response):
    #     print(re.findall("您好", response.body.decode()))
    #     print(re.findall("wzq5517992@163.com|Wzq5517992@163.com", response.body.decode()))
