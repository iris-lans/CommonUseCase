#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
封装浏览器的启动和关闭操作
@Project ：CommonUseCase
@File ：LoginController.py
@Author ：xie.xiaolan
@Date ：2022/7/7 14:43
'''
import unittest
# from webbrowser import browser
from test_case.models import driver
import importlib,sys

# 启动浏览器
importlib.reload(sys)


class launch_browser(unittest.TestCase):
    def setUp(self):
        # self.driver = browser()
        self.driver = driver.browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
