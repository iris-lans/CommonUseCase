#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
时间筛选
@Project ：CommonUseCase 
@File ：time_select_sta.py
@Author ：xie.xiaolan
@Date ：2022/8/30 11:28 
'''
import unittest

from public_interface.DateTimeUtil import DateTimeUtil
from service.ApplicationMallService import ApplicationMallService
from test_case.models import myunit, function
from test_case.page_obj.applicationMallPage import applicationMallPage
from test_case.page_obj.timeSelectionPage import timeSelectionPage
from test_case.page_obj.pointScreenPage import pointScreenPage
from test_case.page_obj.loginPage import login
import random
from time import sleep

from test_case.page_obj.userSwitchingPage import userSwitchingPage


class time_select_sta(myunit.launch_browser):

    def public_part(self):
        """ 公共部分 """
        lo = login(self.driver)
        lo.user_login()
        # 跳转平台
        ap = applicationMallPage(self.driver)
        # 随机点击平台
        user_id = ap.get_userId()
        user_id = user_id.split(":")
        user_id = user_id[1].strip()
        sql_num = ApplicationMallService().user_mall_num(user_id)
        num = random.randint(0, sql_num - 1)
        # num = 0
        ap.check_card(num)
        sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        title_name = ap.successfully_entered()
        return title_name

    def again_check_user(self):
        """ 如果数据为空，重新选择用户 """
        us = userSwitchingPage(self.driver)
        load_text = us.judgment_load()
        # while load_text == '0':
        if load_text == '0':
            us.check_user_select()
            sleep(2)
            # num_s = random.randint(0, 10)
            us.check_user(num = 4)
            # load_text = us.judgment_load()


    @unittest.skip("暂时跳过")
    def test_datetime(self):
        """ 点击【日】筛选 """
        tl_name = self.public_part()
        # 选择菜单栏
        if tl_name != "智维U" and tl_name != "扬尘生态环境管理":
            sleep(2)
            self.again_check_user()
            sleep(2)
            me = pointScreenPage(self.driver)
            num = 1
            me.check_menu(num)
            ts = timeSelectionPage(self.driver)
            num_s = 0
            ts.check_data(tl_name,num_s)
            ts.check_time_frame()
            ts.check_data_time()
            judge_data = ts.judge_success_money()
            isTure = DateTimeUtil().datetime_verify(judge_data,num_s)
            if isTure == False:
                print("【日】时间筛选有误")
        else:
            print(tl_name + "不做<监测点筛选>功能测试")


    @unittest.skip("暂时跳过")
    def test_month(self):
        """ 点击月选择 """
        tl_name = self.public_part()
        if tl_name != "智维U" and tl_name != "扬尘生态环境管理":
            sleep(2)
            self.again_check_user()
            sleep(2)
            me = pointScreenPage(self.driver)
            num = 1
            me.check_menu(num)
            ts = timeSelectionPage(self.driver)
            num_s = 1  # 时间按钮下标
            ts.check_data(tl_name,num_s)
            ts.check_time_frame()
            sleep(2)
            ts.check_data_month()
            sleep(2)
            judge_data = ts.judge_success_money()
            isTure = DateTimeUtil().datetime_verify(judge_data, num_s)
            if isTure == False:
                print("【月】时间筛选有误")
        else:
            print(tl_name + "不做<监测点筛选>功能测试")


    @unittest.skip("暂时跳过")
    def test_year(self):
        """ 点击年选择 """
        tl_name = self.public_part()
        if tl_name != "智维U" and tl_name != "扬尘生态环境管理":
            sleep(2)
            self.again_check_user()
            sleep(2)
            me = pointScreenPage(self.driver)
            num = 1
            me.check_menu(num)
            ts = timeSelectionPage(self.driver)
            num_s = 2  # 时间按钮下标
            ts.check_data(tl_name,num_s)
            sleep(2)
            ts.check_time_frame()
            sleep(2)
            ts.check_data_year()
            sleep(2)
            judge_data = ts.judge_success_money()
            isTure = DateTimeUtil().datetime_verify(judge_data, num_s)
            if isTure == False:
                print("【年】时间筛选有误")
        else:
            print(tl_name + "不做<监测点筛选>功能测试")

    @unittest.skip("暂时跳过")
    def test_customize(self):
        """ 点击【自定义】【时】选择 """
        tl_name = self.public_part()
        if tl_name != "智维U" and tl_name != "扬尘生态环境管理":
            sleep(2)
            self.again_check_user()
            sleep(2)
            me = pointScreenPage(self.driver)
            num = 1
            me.check_menu(num)
            ts = timeSelectionPage(self.driver)
            num_s = 3  # 时间按钮下标
            ts.check_data(tl_name, num_s)
            sleep(2)
            ts.check_time_frame()
            sleep(2)
            ts.check_hour_customize()
            sleep(2)
            judge_data = ts.judge_hour_customize()
            isTure = DateTimeUtil().datetime_customize_hour(judge_data[0])
            if isTure == False:
                print("【自定义】【时】时间筛选有误")
        else:
            print(tl_name + "不做<监测点筛选>功能测试")

    # @unittest.skip("暂时跳过")
    def test_customize_day(self):
        """ 点击【自定义】【日】选择 """
        tl_name = self.public_part()
        if tl_name != "智维U" and tl_name != "扬尘生态环境管理":
            sleep(2)
            self.again_check_user()
            sleep(2)
            me = pointScreenPage(self.driver)
            num = 1
            me.check_menu(num)
            ts = timeSelectionPage(self.driver)
            num_s = 3  # 时间按钮下标
            ts.check_data(tl_name, num_s)
            sleep(2)
            ts.check_day_customize()
            sleep(2)
            ts.check_day_customize_input()
            sleep(2)
            judge_data = ts.judge_day_customize()
            isTure = DateTimeUtil().datetime_customize_hour(judge_data,"day")
            if isTure == False:
                print("【自定义】【日】时间筛选有误")
        else:
            print(tl_name + "不做<监测点筛选>功能测试")




