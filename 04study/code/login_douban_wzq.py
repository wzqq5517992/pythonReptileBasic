# coding=utf-8
from selenium import webdriver
import time
import requests
from yundama.dama import indetify
from selenium.webdriver.chrome.options import Options

chrome_options = Options()


# 设置chrome浏览器无界面模式
# 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
# chrome_options.add_argument('--headless')
chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
# phantomjs_driver = r"E:\phantomjs-2.1.1-windows\bin\phantomjs.exe"
chrome_driver = r"E:\chromedriver.exe"
browser = webdriver.Chrome(executable_path=chrome_driver)

browser.get("https://yuese64.com/")
with open("index.html", "w", encoding="utf-8") as f:
    f.write(browser.page_source)
print(("=" * 10) + "首页保存成功")
browser.find_element_by_id("login").click()
time.sleep(3)
browser.find_element_by_id("login_username").send_keys("wzq5517992@163.com")
browser.find_element_by_id("login_pass").send_keys("wzq5517992")

# 识别验证码
captcha_image_url = browser.find_element_by_xpath(".//div[@class='image']/img").get_attribute("src")
captcha_content = requests.get(captcha_image_url).content
captcha_code = indetify(captcha_content)
print("验证码的识别结果为:", captcha_code)
time.sleep(5)

# 输入验证码
browser.find_element_by_id("login_code").send_keys(captcha_code)

browser.find_element_by_class_name("submit").click()

# 获取cookie
cookies = {i["name"]: i["value"] for i in browser.get_cookies()}
print(cookies)
browser.get("https://yuese64.com/videos/24177/55d047cd3d624316843b211e7844a845/")
time.sleep(5)
browser.get("https://yuese64.com/videos/24177/55d047cd3d624316843b211e7844a845/")
print(browser.page_source)

time.sleep(3)
# browser.quit()
