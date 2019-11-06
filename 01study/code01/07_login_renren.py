# coding=utf-8
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
    "Cookie": "anonymid=k2mwm6nvbg2go5; depovince=BJ; jebecookies=67632e34-5096-49b0-9d92-11fc8ccb3641|||||; _r01_=1; JSESSIONID=abcCcWvLYrrsmeWksA-4w; ick_login=3afe8121-3aec-45af-b7c3-cf68ea0b3d41; ick=d02878ad-307e-4078-bc03-61d47b4c94e6; _de=4C2E496AB1A9F8CDB1141F0AB71777CB; p=5c186c3c96d4fdd18686e1238266d6769; ap=972796369; first_login_flag=1; ln_uact=17733469095; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=fdbd6b46f92366edd6365da90a93bb9b9; societyguester=fdbd6b46f92366edd6365da90a93bb9b9; id=972796369; xnsid=c09646d0; ver=7.0; loginfrom=null; jebe_key=1bf25b88-b26f-45b0-9be8-fa0f11f54301%7Ce136b865e2fccf2f88643d2dd093a69e%7C1573021927164%7C1%7C1573021931041; wp_fold=0"
}

r = requests.get("http://www.renren.com/972796369/profile", headers=headers)

# 保存页面
with open("renren2.html", "w", encoding="utf-8") as f:
    f.write(r.content.decode())
