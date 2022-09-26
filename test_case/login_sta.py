#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
登录测试用例
@Project ：CommonUseCase 
@File ：login_sta.py
@Author ：xie.xiaolan
@Date ：2022/7/8 9:51 
'''
from BeautifulReport import BeautifulReport
from time import sleep
import unittest, random, sys, importlib
from test_case.models import myunit, function
from test_case.page_obj.loginPage import login
from public_interface.ReportConn import ReportConn

sys.path.append("./models")
sys.path.append("./page_obj")
importlib.reload(sys)

@unittest.skip("暂时不运行")
class login_sta(myunit.launch_browser):

    def user_login_verify(self, username="", password=""):
        login(self.driver).user_login(username, password)

    # @unittest.skip("暂不执行")
    # @BeautifulReport.add_test_img("user_pawd_empty1")
    def test_login1(self):
        '''用户名、密码为空登录'''

        self.user_login_verify()
        po = login(self.driver)
        list_content = po.logins_error_hint()
        self.assertEqual(list_content[0], '账号不能为空')
        self.assertEqual(list_content[1], '密码不能为空')
        # 截图方法
        # ReportConn().save_img(self.driver, 'user_pawd_empty1')
        function.insert_img(self.driver, "user_pawd_empty.png")

    # @unittest.skip("暂不执行")
    def test_login2(self):
        '''用户名正确，密码为空登录验证'''

        self.user_login_verify(username="15816870496")
        po = login(self.driver)
        list_content = po.logins_error_hint()
        self.assertIn("密码不能为空",list_content,"《用户名正确，密码为空登录验证》用例运行失败")
        function.insert_img(self.driver, "password_empty.png")

    # @unittest.skip("暂不执行")
    def test_login3(self):
        '''用户名为空，密码正确'''

        self.user_login_verify(password="a123456789")
        po = login(self.driver)
        list_content = po.logins_error_hint()
        self.assertIn("账号不能为空", list_content, "《用户名为空，密码正确》用例运行失败")
        function.insert_img(self.driver, "user_empty.png")

    # @unittest.skip("暂不执行")
    def test_login4(self):
        '''用户名和密码错误'''

        character = random.choice('abcdefghijklmnopqrstuvwxyz')
        username = "sdw" + character
        self.user_login_verify(username=username, password="2sdfd")
        po = login(self.driver)
        list_content = po.logins_error_hint()
        self.assertIn("用户名或密码错误", list_content, "《用户名和密码错误》用例运行失败")
        function.insert_img(self.driver, "user_pass_error.png")

    # @unittest.skip("暂不执行")
    def test_login5(self):
        '''用户名、密码不匹配'''

        self.user_login_verify(username="15919425203", password="a123456789")
        sleep(3)
        po = login(self.driver)
        list_content = po.logins_error_hint()
        self.assertIn("用户名或密码错误", list_content, "《用户名、密码不匹配》用例运行失败")
        function.insert_img(self.driver, "user_pwd_mismatch.png")

    # @unittest.skip("暂不执行")
    def test_login6(self):
        '''用户名、密码正确'''
        ss = "15816870496"
        dd = "a123456789"
        self.user_login_verify(ss, dd)
        sleep(3)
        po = login(self.driver)
        self.assertEqual(po.login_user_success(), u'IRIS')
        function.insert_img(self.driver, "user_pwd_true.png")


if __name__ == '__main__':
    unittest.main()
