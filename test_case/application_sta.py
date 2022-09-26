#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：CommonUseCase 
@File ：application_sta.py
@Author ：xie.xiaolan
@Date ：2022/7/25 14:06 
'''
from test_case.models import myunit, function
from test_case.page_obj.loginPage import login
from service.ApplicationMallService import ApplicationMallService
from test_case.page_obj.applicationMallPage import applicationMallPage
import random,unittest
from time import sleep
from BeautifulReport import BeautifulReport

@unittest.skip("暂不执行")
class application_sta(myunit.launch_browser):

    def string_handling(self,str):
        """ 字符串处理 """
        list_str = list(str)
        list_str.pop(4)
        list_str.pop(4)
        str2 = ''.join(list_str)
        return str2

    # @unittest.skip("暂时跳过")
    def test_mall_num(self):
        """ 用户应用商城权限个数是否正确 """
        lo = login(self.driver)
        lo.user_login()
        ap = applicationMallPage(self.driver)
        user_id = ap.get_userId()
        user_id = user_id.split(":")
        user_id = user_id[1].strip()
        sql_num = ApplicationMallService().user_mall_num(user_id)
        page_num = ap.card_num()
        self.assertEqual(sql_num,page_num,msg="权限个数不匹配")
        function.insert_img(self.driver, "power_number_match.png")


    def test_page_jump(self):
        """ 应用商城测试 """
        lo = login(self.driver)
        lo.user_login()
        po = applicationMallPage(self.driver)
        page_num = po.card_num()
        num = random.randint(0,page_num-1)
        html_name = applicationMallPage(self.driver).get_card_name(num)
        if html_name == "安电U+——管理版" or html_name == "知电U+——管理版":
            html_name = self.string_handling(html_name)
        po.check_card(num)
        sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        html_name_new = po.successfully_entered()
        self.assertIn( html_name_new, html_name, "跳转失败")
        function.insert_img(self.driver, "jump_success.png")


if __name__ == '__main__':
        unittest.main()
