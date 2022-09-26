#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
用户登录界面
@Project ：CommonUseCase 
@File ：loginPage.py
@Author ：xie.xiaolan
@Date ：2022/7/7 18:06 
'''

from selenium.webdriver.common.by import By
from test_case.page_obj.base import page
from time import sleep


class login(page):
    url = '/'
    # 登录用户名的定位
    login_username_loc = (By.ID, 'basic_username')
    # 登录密码的定位
    login_password_loc = (By.ID, 'basic_password')
    # 登录按钮的定位
    login_button_loc = (By.CSS_SELECTOR, '.ant-btn.login-btn.ant-btn-primary')
    # 登录错误提示的定位
    login_error_loc = (By.CLASS_NAME, 'ant-form-item-explain')
    # 登录成功用户名信息
    login_user_success_loc = (By.XPATH, "//div[@class='ant-dropdown-trigger']/div/strong")

    # 登录用户名
    def login_username(self, username):
        self.find_element(*self.login_username_loc).clear()
        self.find_element(*self.login_username_loc).send_keys(username)

    # 登录密码
    def login_password(self, password):
        self.find_element(*self.login_password_loc).clear()
        self.find_element(*self.login_password_loc).send_keys(password)

    # 登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    # 统一登录入口
    def user_login(self, username="15816870496", password="a123456789"):
        """
        获取用户名和页面登录
        :param username: 账号
        :param password: 密码
        :return:
        """
        self.open()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(3)

    def login_error_hint(self):
        """登录错误提示信息"""
        return self.find_element(*self.login_error_loc).text

    def logins_error_hint(self):
        """多个错误提示元素相同定位"""
        result = []
        ele = self.find_elements(*self.login_error_loc)
        for ele_text in ele:
            ss = ele_text.text
            result.append(ss)
        return result

    def login_user_success(self):
        """登录成功用户名信息"""
        # return self.find_element(*self.login_user_success_loc).text
        username = self.find_element(*self.login_user_success_loc).text
        username = username.strip('您好：')
        return username
