#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
监测点选择
@Project ：CommonUseCase 
@File ：point_select_sta.py
@Author ：xie.xiaolan
@Date ：2022/8/18 14:48 
'''

from test_case.models import myunit, function
from test_case.page_obj.loginPage import login
from test_case.page_obj.applicationMallPage import applicationMallPage
from service.ApplicationMallService import ApplicationMallService
from test_case.page_obj.pointScreenPage import pointScreenPage
import random,time,unittest



class point_select_sta(myunit.launch_browser):

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

    # @unittest.skip("暂时跳过")
    def test_check_radio(self):
        """ 筛选单个监测点是否成功 """
        tl_name = self.public_part()
        if tl_name != "智维U" and tl_name != "扬尘生态环境管理":
            me = pointScreenPage(self.driver)
            num = 1
            me.check_menu(num)
            num_s = me.check_point(tl_name)
            if num_s == 1:
                function.insert_img(self.driver, "check_radio_success.png")
            else:
                print("监测点选择失败")
        else:
            print(tl_name + "不做<监测点筛选>功能测试")

    # @unittest.skip("暂时跳过")
    def test_check_box(self):
        """ 监测点多选 """
        # 知电、安电、安识U、智电U 单选
        list_not_run = ["知电U+","安电U+","安识U+","智电U+","智维U","扬尘生态环境管理"]
        tl_name = self.public_part()
        if tl_name not in list_not_run:
            me = pointScreenPage(self.driver)
            num = 1
            me.check_menu(num)
            num_s = me.check_point(tl_name,num)
            if num_s == 1:
                function.insert_img(self.driver, "check_box_success.png")
            else:
                print("监测点选择失败")
        else:
            print(tl_name + "没有<监测点多选>该功能测试")

    def test_select_none(self):
        """ 全不选 """
        list_not_run = ["知电U+", "安电U+", "安识U+", "智电U+", "智维U", "扬尘生态环境管理"]
        tl_name = self.public_part()
        if tl_name not in list_not_run:
            me = pointScreenPage(self.driver)
            num = 1
            me.check_menu(num)
            me.check_drop_box_s()
            me.check_selectNone()
            me.check_define()
            num_text = me.check_tips()
            if num_text != "" or num_text != None:
                function.insert_img(self.driver, "check_select_none.png")
            else:
                print("全不选时，未做提示")
        else:
            print(tl_name + "没有<全不选>功能测试")




