#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
优加云应用商场权限个数查验
@Project ：CommonUseCase 
@File ：ApplicationMallService.py
@Author ：xie.xiaolan
@Date ：2022/7/6 10:58 
'''

from public_interface.DBHelper import DBHelper
from public_interface.LogUtil import LogUtil
import random

class ApplicationMallService():
    # 初始化数据库连接类
    dbhelper = DBHelper()
    LogUtil.init('run.log', console=True)
    logger = LogUtil()

    def user_mall_num(self,user_id):
        """
        根据用户id查询用户拥有的平台权限个数
        :param user_id: 用户id
        :return: 权限个数
        """
        num = 0
        try:
            sql = "SELECT COUNT(*) FROM user_product_auth WHERE user_id = '{}'".format(user_id)
            num = self.dbhelper.fetchone(sql)
        except:
            self.logger.error("拥有产品权限个数","账号有误",user_id)
        finally:
            return int(num[0])

if __name__ == '__main__':
    mall_num = ApplicationMallService()
    # num = mall_num.user_mall_num("52")
    # print(type(num))
    # print(num)
    # s = 'ID: 52'
    # s = s.split(":")
    # s = s[1].strip()
    # print(s)
    sql_num = mall_num.user_mall_num("119")
    num = random.randint(0, sql_num - 1)
    print(num)
