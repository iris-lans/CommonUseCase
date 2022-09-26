#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
登出界面
@Project ：CommonUseCase 
@File ：sign_out_page.py
@Author ：xie.xiaolan
@Date ：2022/7/21 17:28 
'''
from selenium.webdriver import ActionChains

from test_case.page_obj.base import page
from selenium.webdriver.common.by import By
from time import sleep


class signOutPage(page):

    url = '/'
    # 光标停留用户个人信息
    suspension_user_info_loc = (By.CLASS_NAME , 'ant-dropdown-trigger')
    # 点击“退出登录”
    check_out_loc = (By.CSS_SELECTOR , '.ant-dropdown-menu-item.ant-dropdown-menu-item-only-child')
    # 退出成功后的界面
    sign_out_success_loc = (By.XPATH , "//div[@class='switch-login-method']/div/label[1]/span[2]")



    def move_element(self):
        """ 鼠标悬浮到个人信息，展示“退出登录”按钮 """
        ele = self.find_element(*self.suspension_user_info_loc)
        ActionChains(self.driver).move_to_element(ele).perform()
        sleep(1)

    def check_element(self,):
        """ 点击【退出登录】按钮 """
        self.find_elements(*self.check_out_loc)[1].click()
        # for span in sum_ele:
        #     # 获取当前循环到的文本
        #     ele_text = span.text
        #     if ele_text == "退出登录":
        #         span.cleck()


    def sign_out_success(self):
        """成功退出到登录界面"""
        username = self.find_element(*self.sign_out_success_loc).text
        return username


    def sign_out(self):
        """ 统一登出接口 """
        # self.open()
        self.move_element()
        self.check_element()
