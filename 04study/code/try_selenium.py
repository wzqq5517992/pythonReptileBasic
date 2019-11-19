# coding=utf-8
from selenium import webdriver
import time
from yundama.captcha_image import getImage
from yundama.dama import indetify

phantomjs_driver = r"E:\phantomjs-2.1.1-windows\bin\phantomjs.exe"
browser = webdriver.PhantomJS(executable_path=phantomjs_driver)
res = getImage
browser.get("https://yuese64.com/login/")
browser.find_element_by_id("login_username").send_keys("wzq5517992@166.com")
browser.find_element_by_id("login_pass").send_keys("wzq5517992")
code = indetify(res)
browser.find_element_by_id("login_code").send_keys(code)

# yanzhengma = input('请输入验证码')

#
# # 元素定位的方法
# driver.find_element_by_id("su").click()
# #
# # # driver 获取html字符串
# print(driver.page_source)  # 浏览器中elements的内容
# print(driver.current_url)
#
# # driver获取cookie
# cookies = driver.get_cookies()
# print(cookies)
# print("*" * 100)
# cookies = {i["name"]: i["value"] for i in cookies}
# print(cookies)
#
# # 退出浏览器
time.sleep(3)
driver.quit()
