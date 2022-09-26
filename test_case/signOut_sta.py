#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
登出测试用例
@Project ：CommonUseCase 
@File ：signOut_sta.py
@Author ：xie.xiaolan
@Date ：2022/7/22 14:29 
'''
import sys,importlib
import unittest

from test_case.models import myunit, function
from test_case.page_obj.sign_out_page import signOutPage
from test_case.page_obj.loginPage import login

sys.path.append("./models")
sys.path.append("./page_obj")
importlib.reload(sys)

@unittest.skip("暂时不运行")
class signOut_sta(myunit.launch_browser):


    def test_sign_out(self):
        """ 登出 """
        # 登录
        lo = login(self.driver)
        lo.user_login()
        # 登出
        signOutPage(self.driver).sign_out()
        po = signOutPage(self.driver)
        list_content = po.sign_out_success()
        self.assertIn("账号密码登录", list_content, "登出失败")
        function.insert_img(self.driver, "sign_out_success.png")

