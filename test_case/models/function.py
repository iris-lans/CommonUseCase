#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
截图函数
@Project ：CommonUseCase 
@File ：function.py
@Author ：xie.xiaolan
@Date ：2022/7/7 17:40 
'''

from selenium import webdriver
import importlib, sys, os

# 启动浏览器
importlib.reload(sys)


# 截图函数
def insert_img(driver, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    base = base_dir.split('test_case')[0]
    file_path = base + "report/image/" + file_name
    driver.get_screenshot_as_file(file_path)

# def insert_png(driver,filename):
#     base_s = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
# 	base_ss = base_s.split('public_interface')[0]
#     file_path = base_ss + '/report/image/' + filename
#     driver.get_screenshot_as_file(file_path)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://www.soejh.com/login/")
    insert_img(driver, 'login1.jpg')
    driver.quit()
