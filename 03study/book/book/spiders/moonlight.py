# -*- coding: utf-8 -*-
import scrapy
import re
from book.items import MoonLightItem


class MoonlightSpider(scrapy.Spider):
    name = 'moonlight'
    allowed_domains = ['yuese64.com']
    start_urls = ['https://yuese64.com/']

    # kt_member=ee4be80e874927508d372ffdef802ff8;
    def start_requests(self):
        # cookies = "__cfduid=de695d50d361a925d55b51500282c00e91573735250; kt_ips=27.189.222.220; _ga=GA1.2.324235130.1573735253; _gid=GA1.2.276867563.1573735253; UM_distinctid=16e69ee471b475-0b3d26e80de462-335c4d7a-144000-16e69ee471c5b1; kt_tcookie=1; kt_is_visited=1; video_log=23964%3A1573781613%3B; PHPSESSID=f9s6cps9l7g33cn18pi8idhnh5; kt_member=ee4be80e874927508d372ffdef802ff8; _gat_gtag_UA_84734824_7=1; CNZZDATA1275431286=1348386881-1573734450-%7C1573788496; kt_qparams=mode%3Dasync%26action%3Djs_stats%26rand%3D1573788906781"
        cookies = "__cfduid=de695d50d361a925d55b51500282c00e91573735250; kt_ips=27.189.222.220; _ga=GA1.2.324235130.1573735253; _gid=GA1.2.276867563.1573735253; UM_distinctid=16e69ee471b475-0b3d26e80de462-335c4d7a-144000-16e69ee471c5b1; kt_tcookie=1; kt_is_visited=1; video_log=23964%3A1573781613%3B19980%3A1573789346%3B10619%3A1573789395%3B20687%3A1573789501%3B; kt_qparams=mode%3Dasync%26action%3Djs_stats%26rand%3D1573797661929; CNZZDATA1275431286=1348386881-1573734450-%7C1573874931; PHPSESSID=4fiqg6c39nek8212bih9se0tp1; kt_member=28e240c032a6ec2288222e0610863740"
        cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
        )

    def parse(self, response):
        print(re.findall("您好", response.body.decode()))
        # with open("c.html", "w", encoding="utf-8") as f:
        #     f.write(response.body.decode())
        item_list = response.xpath(
            "//div[@class='content']//div[@class='box']//div[1]//div[@class='margin-fix']//div[@class='item  ']")
        # print("获取到得集合", item_list)
        for element in item_list:
            item = MoonLightItem()
            item["title"] = element.xpath("./a/@title").extract_first()
            item["video_href"] = element.xpath("./a/@href").extract_first()
            item["img_href"] = element.xpath(
                ".//div[@class='img']//img[@class='thumb lazy-load']/@data-original").extract_first()

            yield scrapy.Request(
                item["video_href"],
                callback=self.parse_detail,  # 回调方法
                meta={"item": item}  # 回调入参
            )

    def parse_detail(self, response):  # 处理视频详情页
        item = response.meta["item"]
        # item["video_url"] = response.xpath("//div[@class='content']//div[1]//div[@class='video-holder']//div[0]//div[@class='player-holder']//div[@class='no-player']//img/@src").extract()
        item["video_url"] = response.xpath("//div[@class='player-holder']//img/@src").extract_first()
        with open(item["title"]+".html", "w", encoding="utf-8") as f:
            f.write(response.body.decode())
        yield item
