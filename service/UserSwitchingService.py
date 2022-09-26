#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
需量管理节约费用查询
@Project ：CommonUseCase 
@File ：UserSwitchingService.py
@Author ：xie.xiaolan
@Date ：2022/7/27 17:53 
'''

from public_interface.DBHelper import DBHelper
from public_interface.LogUtil import LogUtil
import random

class UserSwitchingService():
    # 初始化数据库连接类
    dbhelper = DBHelper()
    LogUtil.init('run.log', console=True)
    logger = LogUtil()

    def acquisition_costs(self,username="新笙电器",month = "2022-06"):
        """
        获取用户需量管理节约的费用
        :param username: 用户工厂名称（简写）
        :param month: 上月日期（yyyy-mm）
        :return: 费用
        """
        money = 0
        try:
            sql = ("SELECT SUM(save_charge) FROM algorithm_md_space_analysis_result "
                    "WHERE MONTH = '{0}' AND space_analysis_id IN ("
                    "SELECT id FROM algorithm_md_space_analysis_unit WHERE related_inlids IN ("
                    "SELECT inlid FROM inline WHERE cid_belongedto = ( SELECT cid FROM company WHERE shortname = '{1}' ) ) )".format(month,username))
            money = self.dbhelper.fetchone(sql)
            a = money[0]
            if a != None:
                money = int(a)
            else:
                money = 0
        except:
            self.logger.error("拥有产品权限个数","账号有误",username)
        finally:
            return money

    def get_chinese(self,product = "知电U+"):
        """
        随机抽取已有用户的汉字
        :param product: 产品代理权限
        :return: 汉字列表
        """
        if product == "知电U+":
            product = "1"
        elif product == "知电U+管理版":
            product = "5"
        elif product == "安电U+":
            product = "2"
        elif product == "安电U+管理版":
            product = "3"
        elif product == "识电U+":
            product = "4"
        elif product == "安识U+":
            product = "12"

        chinese = []
        try:
            sql = 'SELECT shortname FROM company WHERE is_show = "1" and product = "{}"'.format(product)
            money = self.dbhelper.fetchall(sql)
            a = money[0]
            if a != None:
                for row in money:
                    chinese.append(" | ".join(row))
                chinese = self.GBK2313(chinese)
            else:
                chinese = 0
        except:
            self.logger.error("拥有产品权限个数","账号有误",product)
        finally:
            return chinese


    def GBK2313(self,fruit_name_list):
        """ 随机生成汉字 """
        num_items = len(fruit_name_list)
        random_index = random.randrange(num_items)
        str = fruit_name_list[random_index]
        single_chinese = len(str)
        random_index_s = random.randrange(single_chinese)
        str = str[random_index_s]
        return str

    def acquisition_costs_manage(self,proxy_name="华能广东能源销售",month = "2022-06"):
        """
        获取用户需量管理节约的费用(管理版)
        :param username: 用户工厂名称（简写）
        :param month: 上月日期（yyyy-mm）
        :return: 费用
        """
        money = 0
        try:
            sql = ("SELECT SUM(save_charge) FROM algorithm_md_space_analysis_result "
                    "WHERE MONTH = '{0}' AND space_analysis_id IN ("
                    "SELECT id FROM algorithm_md_space_analysis_unit WHERE related_inlids IN ("
                    "SELECT inlid FROM inline WHERE cid_belongedto IN ( "
                    "SELECT cid FROM company WHERE proxy = (SELECT proxy_id FROM proxy WHERE `shortname` = '{1}') AND is_show = '1') ) )".format(month,proxy_name))
            money = self.dbhelper.fetchone(sql)
            a = money[0]
            if a != None:
                money = int(a)
            else:
                money = 0
        except:
            self.logger.error("拥有产品权限个数","账号有误",proxy_name)
        finally:
            return money

    def get_all_platform_point(self,entry_name = "知电U+",username = "富晶特玻新材料"):
        """ 获取所有平台监测点 """
        # 情况一
        point = ["知电U+","安电U+","智电U+"]
        # 情况二
        manage = ["知电U+管理版","安电U+管理版"]
        # 情况三
        know = "识电U+"
        # 情况四
        ease = "安识U+"
        sql = ""
        if entry_name in point:
            sql = "SELECT `name` FROM point INNER JOIN company on cid = cid_belongedto WHERE shortname = '{}'".format(username)
        elif entry_name in manage:
            sql = ("SELECT c.fullname FROM company c INNER JOIN proxy p on c.proxy = p.proxy_id "
                   "WHERE p.shortname = '{}' AND c.is_show = '1'".format(username))
        elif entry_name == know:
            sql = ("SELECT storey_id, storey_name from storey_room_map s,company c where c.cid = s.cid "
                   "AND c.shortname='{}' group by storey_id, storey_name order by storey_id".format(username))
        elif entry_name == ease:
            sql = ("SELECT `name` FROM point WHERE mtid in(SELECT mtid FROM "
                   "monitor_reuse m,company c WHERE m.cid = c.cid AND c.shortname = '{}' AND c.product = '12')".format(username))
        point_list = []
        try:
            money = self.dbhelper.fetchall(sql)
            a = money[0]
            if a != None:
                for row in money:
                    point_list.append(" | ".join(row))
        except:
            self.logger.error("拥有监测点权限个数", "账号有误", entry_name)
        finally:
            return point_list



if __name__ == '__main__':
    de = UserSwitchingService()
    # n = "元/月"
    # str = n.split("/")
    # n = str[0]
    # n = de.acquisition_costs()
    # n = round(n/10000,2)
    a = de.get_all_platform_point()
    print(a)