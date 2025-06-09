#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
数据库连接
@Project ：CommonUseCase
@File ：DBHelper.py
@Author ：xie.xiaolan
@Date ：2022/7/6 10:18
'''
import sys
import pymysql
import logging


# 加入日志
#获取logger实例
logger = logging.getLogger("baseSpider")
# 指定输出格式
formatter = logging.Formatter('%(asctime)s\
              %(levelname)-8s:%(message)s')
# 文件日志
file_handler = logging.FileHandler("baseSpider.log")
file_handler.setFormatter(formatter)
# 控制台日志
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

# 为logge添加具体的日志处理器
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.setLevel(logging.INFO)

class DBHelper:
    # 构造函数
    # --- 测试数据库
    def __init__(self, host='172.18.1.248',port='4000', user='poweriot',
                 pwd='power_iot123', db='power_iot'):
    # --- 生产数据库
    # def __init__(self, host='172.16.0.253', port='4000', user='poweriot',
    #                  pwd='power_iot456', db='power_iot'):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.db = db
        self.conn = None
        self.cur = None

    # 连接数据库
    def connectDatabase(self):
        try:
            self.conn = pymysql.connect(self.host, self.port, self.user,
                                        self.pwd, self.db, charset='utf8mb4',cursorclass = pymysql.cursors.DictCursor)
        except:
            logger.error("connectDatabase failed")
            return False
        self.cur = self.conn.cursor()
        return True


    # 关闭数据库
    def close(self):
        # 如果数据打开，则关闭；否则没有操作
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()
        return True


    # 执行数据库的sq语句,主要用来做插入操作
    def execute(self, sql, params=None):
        # 连接数据库
        self.connectDatabase()
        try:
            if self.conn and self.cur:
                # 正常逻辑，执行sql，提交操作
                self.cur.execute(sql, params)
                self.conn.commit()
        except:
            logger.error("execute failed: " + sql)
            logger.error("params: " + params)
            self.close()
            return False
        return True

    def fetchall(self, sql, params=None):
        """
        用来查询表数据,多条数据
        :param sql: sql语句
        :param params: 参数，可以为None
        :return:
        """
        self.execute(sql, params)
        return self.cur.f


    def fetchone(self, sql, params=None):
        """
        用来查询表数据,单条数据
        :param sql: sql语句
        :param params: 参数，可以为None
        :return:
        """
        self.execute(sql, params)
        return self.cur.fetchone()




if __name__ == '__main__':
    dbhelper = DBHelper()
    # 创建数据库的表
    # sql = "create table maoyan('id'varchar(8),\
    #             'title'varchar(50),\
    #             'star'varchar(200), \
    #             'time'varchar(100),primary key('id'));"
    # result = dbhelper.execute(sql, None)
    #查询数据
    # sql = "SELECT count(*) as nu FROM `power_iot`.`user_product_auth` WHERE `user_id` = '52'"
    sql = "SELECT * FROM `power_iot`.`user_product_auth`"
    result = dbhelper.fetchall(sql, None)
    print(result)
    if result:
        logger.info("查询成功")
    else:
        logger.error("查询失败")
