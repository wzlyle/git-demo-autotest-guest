#coding=utf-8
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.action_chains import ActionChains

# 麦子学院登陆
def maizi_login(self,username,password):
    driver = self.driver
    driver.find_element_by_link_text(u"登录").click()
    driver.find_element_by_id("id_account_l").clear()
    driver.find_element_by_id("id_account_l").send_keys(username)
    driver.find_element_by_id("id_password_l").clear()
    driver.find_element_by_id("id_password_l").send_keys(password)
    driver.find_element_by_id("login_btn").click()

# 麦子学院退出
def maizi_logout(self):
    driver = self.driver
    driver.find_element_by_link_text(u"退出").click()

# 发布会签到系统登录模块
def guest_login(self,username,password):
    driver = self.driver
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_id("btn").click()


# 发布会签到系统退出登录模块
def guest_logout(self):
    driver = self.driver
    driver.find_element_by_link_text(u"退出").click()
