# coding=utf-8
from selenium import webdriver
import time
import requests
from yundama.dama import indetify

phantomjs_driver = r"E:\phantomjs-2.1.1-windows\bin\phantomjs.exe"
browser = webdriver.PhantomJS(executable_path=phantomjs_driver)

browser.get("https://yuese64.com/login/")
browser.find_element_by_id("login_username").send_keys("wzq5517992@166.com")
browser.find_element_by_id("login_pass").send_keys("wzq5517992")
# code = indetify(res)



# 识别验证码
# captcha_image_url = browser.find_element_by_class_name("captcha_image").get_attribute("src")
captcha_image_url = browser.find_element_by_xpath(".//div[@class='image']/img").get_attribute("src")
captcha_content = requests.get(captcha_image_url).content
captcha_code = indetify(captcha_content)
print("验证码的识别结果为:", captcha_code)

# 输入验证码
browser.find_element_by_id("login_code").send_keys(captcha_code)

browser.find_element_by_class_name("submit").click()

# 获取cookie
cookies = {i["name"]: i["value"] for i in browser.get_cookies()}
print(cookies)

time.sleep(3)
browser.quit()
