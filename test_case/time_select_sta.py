#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
时间筛选
@Project ：CommonUseCase 
@File ：time_select_sta.py
@Author ：xie.xiaolan
@Date ：2022/8/30 11:28 
'''
from service.ApplicationMallService import ApplicationMallService
from test_case.models import myunit, function
from test_case.page_obj.applicationMallPage import applicationMallPage
from test_case.page_obj.timeSelectionPage import timeSelectionPage
from test_case.page_obj.pointScreenPage import pointScreenPage
from test_case.page_obj.loginPage import login
import random,time



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
        num = 0
        ap.check_card(num)
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        title_name = ap.successfully_entered()
        return title_name

    def test_datetime(self):
        """ 点击【日】筛选 """
        tl_name = self.public_part()
        # 选择菜单栏
        if tl_name != "智维U" and tl_name != "扬尘生态环境管理":
            me = pointScreenPage(self.driver)
            num = 1
            me.check_menu(num)
            ts = timeSelectionPage(self.driver)
            num_s = 0
            ts.check_data(tl_name,num_s)
            ts.check_time_frame()
            day = ts.check_data_time()
        else:
            print(tl_name + "不做<监测点筛选>功能测试")


