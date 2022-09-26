#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
监测点选择
@Project ：CommonUseCase 
@File ：pointScreenPage.py
@Author ：xie.xiaolan
@Date ：2022/8/16 10:48 
'''
from test_case.page_obj.base import page
from selenium.webdriver.common.by import By
from time import sleep
import random




class pointScreenPage(page):

    url = "/"
    # 点击菜单栏
    check_menu_loc = (By.XPATH, "//div[@class='main__menu-container']/ul/li")
    # --- 监测点 ---
    # 下拉式,知电U、安电U
    click_point_loc = (By.CSS_SELECTOR, '.ant-dropdown-link.ant-dropdown-trigger')
    get_point_sum_loc = (By.CSS_SELECTOR, ".ant-dropdown-menu-item.ant-dropdown-menu-item-only-child")
    # 知电U管理版、安电U管理版、识电U
    click_points_loc = (By.CLASS_NAME, 'cs__input-text')
    get_points_sum_loc = (By.XPATH, "//ul[@class='cs__checkbox-list']/li")
    all_or_one_loc = (By.XPATH , "//div[@class='cs__button']/label/span")  # 全选/全不选
    is_sure_loc = (By.CSS_SELECTOR , '.ant-btn.ant-btn-primary.ant-btn-sm')  # 点击下拉框确定按钮
    # 安识U
    click_point_anshi_loc = (By.XPATH, "//div[@class='page-header']/div/div/span")
    get_point_anshi_sum_loc = (By.XPATH, "//ul[@class='select-list']/li")
    # 智电U
    click_point_zhidian_loc = (By.XPATH, "//div[@class='dropdown-select']/span")
    get_point_zhidian_sum_loc = (By.XPATH, "//ul[@class='card-list']/li")


    # 定位提示框
    tips_loc = (By.CLASS_NAME , "ant-message")

    # 成功判断
    # success_text_loc = (By.XPATH,'//*[contains(text(),"'+point_text+'")]')

    def check_menu(self,num):
        """
        点击菜单
        :param num: 第几个菜单
        :return:
        """
        self.find_elements(*self.check_menu_loc)[num].click()

    def check_drop_box(self):
        """ 点击下拉框（知电U、安电U） """
        self.find_element(*self.click_point_loc).click()

    def check_drop_box_s(self):
        """ 点击下拉框（管理版、识电U） """
        self.find_element(*self.click_points_loc).click()

    def check_selectNone(self):
        """ 点击全选/全不选输入框 """
        self.find_element(*self.all_or_one_loc).click()

    def check_define(self):
        """ 监测点【确认】按钮 """
        self.find_element(*self.is_sure_loc).click()

    def get_point_text(self,software_name,num_type):
        """
        点击监测点，获取点击监测点的文本
        :param loc_type:定位监测点位置
        :param option_num:定位下拉选项参数
        :param num_type:多个监测点,不等于0
        :return:文本
        """
        length_point = ""
        point_num = ""
        point_text = ""
        if software_name == "知电U+" or software_name == "安电U+":
            self.check_drop_box()
            text_point = self.find_elements(*self.get_point_sum_loc)
            length_point = len(text_point)
            point_num = random.randint(0, length_point - 1)
            point_text = self.find_elements(*self.get_point_sum_loc)[point_num].text
            self.find_elements(*self.get_point_sum_loc)[point_num].click()
        elif software_name == "知电U+管理版" or software_name == "安电U+管理版" or software_name == "识电U+":
            self.check_drop_box_s()
            self.check_selectNone()
            text_point = self.find_elements(*self.get_points_sum_loc)
            length_point = len(text_point)
            point_num = random.randint(0, length_point - 1)
            point_text = self.find_elements(*self.get_points_sum_loc)[point_num].text
            self.find_elements(*self.get_points_sum_loc)[point_num].click()
        if num_type != 0:
            flag = True
            point_nums = 0
            point_text_s = ""
            while flag:
                point_nums = random.randint(0, length_point - 1)
                if point_nums != point_num : flag = False
            if software_name == "知电U+" or software_name == "安电U+":
                point_text_s = self.find_elements(*self.click_point_loc)[point_nums].text
                self.find_elements(*self.click_point_loc)[point_nums].click()
            elif software_name == "知电U+管理版" or software_name == "安电U+管理版" or software_name == "识电U+":
                point_text_s = self.find_elements(*self.get_points_sum_loc)[point_nums].text
                self.find_elements(*self.get_points_sum_loc)[point_nums].click()
            self.check_define()
            a = []
            a.append(point_text)
            a.append(point_text_s)
            point_text = a
        return point_text

    def check_point(self,software_name,num_type=0):
        """
        点击监测点,并判断是否成功
        :param software_name: 平台名称
        :param num_type: 是否是多选 0，不是多选；1，多选
        :return: 0、不成功 1、成功
        """
        # type_ele = ""
        # option_num = ""
        # if software_name == "知电U+" or software_name == "安电U+":
        #     type_ele = self.click_point_loc
        #     option_num = self.get_point_sum_loc
        # elif software_name == "知电U+管理版" or software_name == "安电U+管理版" or software_name == "识电U+":
        #     type_ele  = self.click_points_loc
        #     option_num = self.get_points_sum_loc
        text = self.get_point_text(software_name,num_type)
        sleep(2)
        if num_type != 0:
            text = text[0]
        list_point = self.find_elements(By.XPATH,'//*[contains(text(),"'+text+'")]')
        list_length = len(list_point)
        if list_length > 0:
            success_num = 1
        else:
            success_num = 0
        return success_num


    def check_tips(self):
        """ 反误提示框 """
        tips_text = self.find_element(*self.tips_loc).text
        return tips_text
