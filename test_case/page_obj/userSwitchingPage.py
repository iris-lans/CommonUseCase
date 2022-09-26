#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
用户切换功能
@Project ：CommonUseCase 
@File ：userSwitchingPage.py
@Author ：xie.xiaolan
@Date ：2022/7/22 16:57 
'''
from selenium.webdriver.common.by import By

from test_case.page_obj.base import page
from time import sleep


class userSwitchingPage(page):

    url = "/"
    # 点击用户切换下拉框
    check_user_loc = (By.CLASS_NAME , 'header__company')
    # 输入用户名称
    fuzzy_query_loc = (By.CLASS_NAME , 'ant-input')
    # 省级切换下拉框
    provincial_switching_loc = (By.CSS_SELECTOR , '.ant-select.layer-header__dropdown.ant-select-single.ant-select-show-arrow')
    # 点击省级
    provincial_check_loc = (By.CSS_SELECTOR , '.ant-select-item.ant-select-item-option')
    # 获取点击用户的简称
    click_username_loc = (By.XPATH , '//h4[@class="ant-list-item-meta-title"]/span')
    # 点击用户
    click_options_loc = (By.XPATH , "//li[@class='ant-list-item']")
    # 判断成功依据
    # 获取需量管理节约费用
    demand_money_loc = (By.XPATH , "//div[@class='economy__card demand']/div[2]/div[2]/span[2]")
    # 获取费用单位
    expense_unit_loc = (By.XPATH , "//div[@class='economy__card demand']/div[2]/div[2]/span[3]")
    # 点击“进入内页”按钮
    check_into_page_loc = (By.CLASS_NAME , "top__btn")
    # 点击菜单栏
    check_menu_loc = (By.XPATH , "//div[@class='main__menu-container']/ul/li[2]")
    # ----  点击监测点  ----
    # 下拉式,知电U、安电U
    click_point_loc = (By.CSS_SELECTOR , '.ant-dropdown-link.ant-dropdown-trigger')
    get_point_sum_loc = (By.CSS_SELECTOR , ".ant-dropdown-menu-item.ant-dropdown-menu-item-only-child")
    # 知电U管理版、安电U管理版、识电U
    click_points_loc = (By.CLASS_NAME , 'cs__input-text')
    get_points_sum_loc = (By.XPATH , "//ul[@class='cs__checkbox-list']/li")
    # 安识U
    click_point_anshi_loc = (By.XPATH , "//div[@class='page-header']/div/div/span")
    get_point_anshi_sum_loc = (By.XPATH,"//ul[@class='select-list']/li")
    # 智电U
    click_point_zhidian_loc = (By.XPATH , "//div[@class='dropdown-select']/span")
    get_point_zhidian_sum_loc = (By.XPATH,"//ul[@class='card-list']/li")


    def check_user_select(self):
        """ 点击用户切换按钮，显示下拉框 """
        self.find_element(*self.check_user_loc).click()


    def check_user(self,num = 0):
        """ 选择用户工厂 """
        self.find_elements(*self.click_options_loc)[num].click()


    def fuzzy_query(self,username):
        """ 手动输入工厂用户名称 """
        self.find_element(*self.fuzzy_query_loc).clear()
        self.find_element(*self.fuzzy_query_loc).send_keys(username)

    def provincial_switching(self):
        """ 点击省份，显示下拉框 """
        self.find_element(*self.provincial_switching_loc).click()

    def provincial_check(self,num = 1):
        """ 选择省份 """
        self.find_elements(*self.provincial_check_loc)[num].click()

    def get_demand_money(self):
        """ 获取需量管理费用 """
        demand_money = self.find_element(*self.demand_money_loc).text
        return demand_money

    def get_expense_unit(self):
        """ 获取费用单位 """
        unit = self.find_element(*self.expense_unit_loc).text
        str = unit.split("/")
        unit = str[0]
        return unit

    def get_click_username(self,num=0):
        """ 获取用户点击简称 """
        username = self.find_elements(*self.click_username_loc)[num].text
        return username

    def enter_inside_page(self):
        """ 点击进入内页 """
        self.find_element(*self.check_into_page_loc).click()

    def check_menu(self):
        """ 点击菜单 """
        self.find_element(*self.check_menu_loc).click()

    def success_judgment(self,software_name = "知电U+"):
        """
        获取切换工厂后的监测点
        :param software_name: 软件平台名称
        :return: 返回监测点数组
        """
        text_point = []
        if software_name == "知电U+" or software_name == "安电U+":
            self.find_element(*self.click_point_loc).click()
            text_point = self.find_elements(*self.get_point_sum_loc)
        elif software_name == "知电U+管理版" or software_name == "安电U+管理版" or software_name == "识电U+":
            self.find_element(*self.click_points_loc).click()
            text_point = self.find_elements(*self.get_points_sum_loc)
        elif software_name == "安识U+":
            self.find_element(*self.click_point_anshi_loc).click()
            text_point = self.find_elements(*self.get_point_anshi_sum_loc)
        elif software_name == "智电U+":
            self.find_element(*self.click_point_zhidian_loc).click()
            text_point = self.find_elements(*self.get_point_zhidian_sum_loc)
        sleep(2)
        lists = []
        for name in text_point:
            a = name.text
            lists.append(a)

        return lists




