
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：CommonUseCase
@File ：ApplicationMallService.py
@Author ：xie.xiaolan
@Date ：2022/7/6 10:58
'''
from public_interface.DBHelper import DBHelper
from public_interface.LogUtil import LogUtil
from public_interface.PrpCrypt import PrpCrypt
import logging
class LoginService:
    # 初始化数据库连接类
    dbhelper = DBHelper()
    LogUtil.init('run.log', console=True)
    logger = LogUtil()

    def account_password_login(self,username,password):
        """
        账号密码登录
        :param username: 账号
        :param password: 密码
        :return num: 0（未注册） 1（账号正常）
        """
        num = 0
        try:
            sql = "SELECT * FROM `power_iot`.`user` WHERE `is_delete` = '0' AND `phone_number` = '{}'".format(username)
            results = self.dbhelper.fetchone(sql)
            if results:
                sql_password = results[1]
                # 加密密码
                eny = PrpCrypt().encrypt(password)
                password_s = str(eny,encoding='utf-8')
                self.logger.info("字符串处理",password_s)
                assert password_s == sql_password
                num = 1
                return num
            else:
                print("此账号未注册，请先注册")
        except AssertionError:
            self.logger.error("密码校对","密码输入错误",password)
        except:
            self.logger.error("账号密码登录","账号输入异常",username)
        finally:
            return num


if __name__ == '__main__':
    login = LoginService()
    username = "15816870496"
    password = "a123456789"
    na = login.account_password_login(username,password)
    print(na)