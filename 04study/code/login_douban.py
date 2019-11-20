# coding=utf-8
from selenium import webdriver
import time
import requests
from yundama.dama import indetify
import importlib
import urllib.parse


def ParseCookiestr(cookie_str):
    cookielist = []
    for item in cookie_str.split(';'):
        cookie = {}
        itemname = item.split('=')[0]
        iremvalue = item.split('=')[1]
        cookie['name'] = itemname
        cookie['value'] = urllib.parse.unquote(iremvalue)
        cookielist.append(cookie)
    return cookielist


# phantomjs_driver = r"E:\phantomjs-2.1.1-windows\bin\phantomjs.exe"
# browser = webdriver.PhantomJS(executable_path=phantomjs_driver)
chrome_driver = r"E:\chromedriver.exe"
browser = webdriver.Chrome(executable_path=chrome_driver)
# browser.get("https://yuese64.com/captcha/logon/")
browser.get("https://yuese64.com/login/")

cookies_str = ""
cookies_list = browser.get_cookies()
for cookies in cookies_list:
    cookies_str += cookies['name'] + "=" + cookies['value'] + ";"

print(cookies_str[:-1])
cookielist = ParseCookiestr(cookies_str[:-1])
browser.get("https://yuese64.com/login/")

for i in cookielist:
    cookie = {}
    # 3.对于使用add_cookie来说，参考其函数源码注释，需要有name,value字段来表示一条cookie，有点生硬
    cookie['name'] = i['name']
    cookie['value'] = i['value']
    # 4.这里需要先删掉之前那次访问时的同名cookie，不然自己设置的cookie会失效
    browser.delete_cookie(i['name'])
    # 添加自己的cookie
    browser.add_cookie(cookie)

browser.get("https://yuese64.com/login/")
browser.find_element_by_id("login_username").send_keys("wzq5517992@163.com")
browser.find_element_by_id("login_pass").send_keys("wzq5517992")

# 识别验证码
captcha_image_url = browser.find_element_by_xpath(".//div[@class='image']/img").get_attribute("src")
captcha_content = requests.get(captcha_image_url).content
captcha_code = indetify(browser.page_source)
print("验证码的识别结果为:", captcha_code)


# 输入验证码
# browser.find_element_by_id("login_code").send_keys(captcha_code)
time.sleep(5)
# browser.find_element_by_class_name("submit").click()
# print(browser.page_source)
# time.sleep(3)
# browser.get("https://yuese64.com/videos/24177/55d047cd3d624316843b211e7844a845/")
# time.sleep(5)

# 获取cookie
cookies = {i["name"]: i["value"] for i in browser.get_cookies()}
print(cookies)

time.sleep(3)
# browser.quit()
