#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：CommonUseCase 
@File ：user_switch_sta.py
@Author ：xie.xiaolan
@Date ：2022/7/28 10:48 
'''
from public_interface.DateTimeUtil import DateTimeUtil
from service.ApplicationMallService import ApplicationMallService
from service.UserSwitchingService import UserSwitchingService
from test_case.models import myunit, function
from test_case.page_obj.loginPage import login
from test_case.page_obj.userSwitchingPage import userSwitchingPage
from test_case.page_obj.applicationMallPage import applicationMallPage
import unittest,time,random


class user_switch_sta(myunit.launch_browser):

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
        ap.check_card(num)
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        title_name = ap.successfully_entered()
        return title_name


    @unittest.skip("暂时跳过")
    def test_normal_user_switching(self):
        """ 用户正常切换 """
        tl_name = self.public_part()
        if tl_name != "智维U" and tl_name != "扬尘生态环境管理":
            us = userSwitchingPage(self.driver)
            if tl_name == "智电U+" or tl_name == "安电U+管理版":
                us.enter_inside_page()
                time.sleep(2)
            us.check_user_select()
            username = us.get_click_username()
            us.check_user()
            time.sleep(3)
            if tl_name == "智电U+" or tl_name == "安电U+管理版":
                us.enter_inside_page()
                time.sleep(2)
            sql_point_num = UserSwitchingService().get_all_platform_point(tl_name,username)
            us.check_menu()
            page_point_num = us.success_judgment(tl_name)
            if set(page_point_num) > set(sql_point_num):
            # money = us.get_demand_money()
            # last_month = DateTimeUtil().get_last_month()
            # unit = us.get_expense_unit()
            # sql_money = UserSwitchingService().acquisition_costs(username,last_month)
            # if sql_money != 0:
            #     if unit == "万元":
            #         sql_money = round(sql_money / 10000, 2)
            #         self.assertEqual(sql_money ,money ,msg="用户切换失败："+username)
            # else:
            #     self.assertEqual("--", money, msg="空字符串处理错误")
                function.insert_img(self.driver, "user_normal_switch_success.png")
            else:
                print(tl_name+" -- "+username + " 监测点数据不正确")
        else:
            print(tl_name + "没有该功能")

    @unittest.skip("暂时跳过")
    def test_userCheck_provincial(self):
        """ 根据省级切换用户 """
        tl_name = self.public_part()
        if tl_name != "智维U" and tl_name != "扬尘生态环境管理" and tl_name != "知电U+管理版" and tl_name != "安电U+管理版" :
            us = userSwitchingPage(self.driver)
            if tl_name == "智电U+":
                us.enter_inside_page()
                time.sleep(2)
            us.check_user_select()
            us.provincial_switching()
            us.provincial_check()
            username = us.get_click_username()
            us.check_user()
            time.sleep(3)
            if tl_name == "智电U+":
                us.enter_inside_page()
                time.sleep(2)
            sql_point_num = UserSwitchingService().get_all_platform_point(tl_name,username)
            us.check_menu()
            page_point_num = us.success_judgment(tl_name)
            if set(page_point_num) > set(sql_point_num):
                function.insert_img(self.driver, "provincial_switch_success.png")
            else:
                print(tl_name+" -- "+username + " 监测点数据不正确")
        else:
            print(tl_name + "没有该功能")

    # @unittest.skip("暂时跳过")
    def test_fuzzy_query(self):
        """ 模糊查询 """
        tl_name = self.public_part()
        if tl_name != "智维U" and tl_name != "扬尘生态环境管理":
            us = userSwitchingPage(self.driver)
            if tl_name == "智电U+" or tl_name == "安电U+管理版":
                us.enter_inside_page()
                time.sleep(2)
            us.check_user_select()
            like_name = UserSwitchingService().get_chinese(tl_name)
            us.fuzzy_query(like_name)
            time.sleep(2)
            username = us.get_click_username()
            us.check_user()
            time.sleep(3)
            if tl_name == "智电U+" or tl_name == "安电U+管理版":
                us.enter_inside_page()
                time.sleep(2)
            sql_point_num = UserSwitchingService().get_all_platform_point(tl_name,username)
            us.check_menu()
            page_point_num = us.success_judgment(tl_name)
            if set(page_point_num) > set(sql_point_num):
                function.insert_img(self.driver, "user_normal_switch_success.png")
            else:
                print(tl_name+" -- "+username + " 监测点数据不正确")
        else:
            print(tl_name + "没有该功能")

if __name__ == '__main__':
    unittest.main()



