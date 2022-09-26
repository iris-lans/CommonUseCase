#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
应用商城界面
@Project ：CommonUseCase 
@File ：applicationMallPage.py
@Author ：xie.xiaolan
@Date ：2022/7/22 17:09 
'''
from selenium.webdriver.common.by import By
from test_case.page_obj.base import page


class applicationMallPage(page):

    url = "/"
    # 获取卡片
    card_element_loc = (By.CLASS_NAME, "item-wrap3")
    # 获取卡片名称
    card_name_loc = (By.XPATH , "//div[@class='content']/div[1]")
    # 获取用户user_id
    user_id_loc = (By.CLASS_NAME , "id")



    def get_userId(self):
        """ 获取用户id """
        user_id = self.find_element(*self.user_id_loc).text
        return user_id


    def card_num(self):
        """ 获取平台权限总个数 """
        applications_num = self.find_elements(*self.card_element_loc)
        hu = len(applications_num)
        return hu

    def get_card_name(self,num = 0):
        """ 获取点击卡片的文本 """
        card_name = self.find_elements(*self.card_name_loc)[num].text
        return card_name

    def check_card(self,num = 0):
        """ 点击卡片 """
        self.find_elements(*self.card_element_loc)[num].click()

    def successfully_entered(self):
        """ 成功跳转到指定页面 """
        new_text =  self.driver.title
        return new_text




