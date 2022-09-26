#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
打开浏览器
@Project ：CommonUseCase 
@File ：driver.py
@Author ：xie.xiaolan
@Date ：2022/7/7 15:58 
'''

# -*-coding:utf-8-*-
# _author_ = "janehost"

from selenium import webdriver
import importlib,sys

# 启动浏览器
importlib.reload(sys)


def browser():
    # 打开谷歌浏览器
    driver = webdriver.Chrome()
    # 火狐浏览器
    # driver = webdriver.Firefox()
    return driver


if __name__ == '__main__':
    dr = browser()
    # 测试环境
    dr.get("https://www.soejh.com/login/")
    # dr.quit()

