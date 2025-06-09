#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
时间选择
@Project ：CommonUseCase 
@File ：timeSelectionPage.py
@Author ：xie.xiaolan
@Date ：2022/8/30 10:32 
'''
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from test_case.page_obj.base import page
from time import sleep



class timeSelectionPage(page):

    url = "/"
    # 时间筛选按钮,知电U、安电U、安识U
    data_point_loc = (By.XPATH, "//div[@class='filter-btn__group']/button")
    # 时间筛选按钮,管理版、识电u、智电U
    data_points_loc = (By.XPATH, "//div[@class='datetime']/span/button")
    # 日期选择框
    data_check_loc = (By.CLASS_NAME, 'ant-picker-input')
    # 时间插件向前一个月
    last_data_loc = (By.CLASS_NAME, 'ant-picker-header-prev-btn')
    # 选择日期
    check_datetime_loc = (By.XPATH, '//*[@class="ant-picker-body"]/table/tbody/tr[1]/td[6]')
    # 选择结束日期
    check_day_end_loc = (By.XPATH, '//*[@class="ant-picker-body"]/table/tbody/tr[4]/td[6]')
    # 选择结束日期
    check_datetime_end_loc = (By.XPATH, '//*[@class="ant-picker-body"]/table/tbody/tr[2]/td[1]')
    # 选择月份
    check_month_loc = (By.XPATH, '//*[@class="ant-picker-body"]/table/tbody/tr[1]/td[1]')
    # 选择年份
    check_year_loc = (By.XPATH, '//*[@class="ant-picker-body"]/table/tbody/tr[1]/td[2]')
    # 自定义【时】时间选择确定按钮
    check_customize_hour_confirm = (By.CLASS_NAME , "ant-picker-ok")
    # 获取中间时间端电量区间
    judgment_customize_hour_loc = (By.XPATH,"//*[@class='power-fee__card-wraper']/div[2]/div[2]/p[2]")
    # 点击自定义【日】选择
    check_customize_day_loc = (By.CLASS_NAME,"filter-btn__day")
    # 点击自定义【日】时间弹窗选择
    check_customize_day_input = (By.CSS_SELECTOR,".ant-picker-input.ant-picker-input-active")


    # 判断是否成功
    # 电量电费、用电管理
    judgment_days_loc = (By.XPATH , "//section[@class='power-fee__card-wraper']/div[5]/div[2]/p[2]")
    # 曲线图（用电统计）
    echar_count = (By.XPATH , "//section[@class='power-fee__statistic']/div[2]")
    echar_mouse = (By.XPATH , "//section[@class='power-fee__statistic']/div[2]/div[2]/p")  # 鼠标悬浮
    # 用电监测、电能质量
    echar_div_loc = (By.XPATH , "//div[@class='page-left-content__in']/div[2]/div/div/div[2]/div[1]/div[2]")
    floating_frame_loc = (By.XPATH , "//div[@class='page-left-content__in']/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[1]")
    # 指标统计
    min_num_count_loc = (By.XPATH , "//div[@class='conventional-parameters table-style']/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[2]/div/span[1]")
    # 负荷分析





    def check_data(self,software_name,num_s):
        """
        点击时间类型，并获取点击时间类型的文本
        :param software_name: 平台名称
        :param num_s: 第几个时间类型
        :return: 点击的时间的文本
        """
        text = ""
        if software_name == "知电U+" or software_name == "安电U+" or software_name == "安识U+":
            text = self.find_elements(*self.data_point_loc)[num_s].text
            self.find_elements(*self.data_point_loc)[num_s].click()
        else:
            text = self.find_elements(*self.data_points_loc)[num_s].text
            self.find_elements(*self.data_points_loc)[num_s].click()
        return text

    def check_time_frame(self):
        """ 点击时间选择框 """
        self.find_element(*self.data_check_loc).click()

    def check_data_time(self):
        """ 日选择 """
        self.find_element(*self.last_data_loc).click()
        sleep(2)
        data_text = self.find_element(*self.check_datetime_loc).text
        self.find_element(*self.check_datetime_loc).click()
        return data_text

    def check_data_month(self):
        """ 月选择 """
        month_text = self.find_element(*self.check_month_loc).text
        self.find_element(*self.check_month_loc).click()
        return month_text

    def check_data_year(self):
        """ 年选择 """
        year_text = self.find_element(*self.check_year_loc).text
        self.find_element(*self.check_year_loc).click()
        return year_text

    def judge_success_money(self):
        """ 电量电费模块判断点击是否成功 """
        day_text = self.find_element(*self.judgment_days_loc).text
        return day_text

    def judge_chart_success(self):
        """ 判断曲线图时间更改是否成功 """
        ele = self.find_element(*self.echar_div_loc)
        ActionChains(self.driver).move_to_element(ele).perform()
        move_text = self.find_element(*self.floating_frame_loc).text
        return move_text

    def check_hour_customize(self):
        """ 自定义【时】起始时间选择 """
        self.find_element(*self.last_data_loc).click()
        sleep(2)
        #data_text = self.find_element(*self.check_datetime_loc).text
        self.find_element(*self.check_datetime_loc).click()
        self.find_element(*self.check_customize_hour_confirm).click()
        sleep(2)
        self.find_element(*self.check_datetime_end_loc).click()
        self.find_element(*self.check_customize_hour_confirm).click()

    def judge_hour_customize(self):
        """ 判断自定义【时】选择是否正确 """
        hour_text = self.find_element(*self.judgment_customize_hour_loc).text
        list = hour_text.split(" - ")
        return list

    def check_day_customize(self):
        """ 点击自定义【日】 """
        self.find_element(*self.check_customize_day_loc).click()

    def check_day_customize_input(self):
        """ 点击自定义【日】文本框 """
        self.find_element(*self.check_customize_day_input).click()
        sleep(2)
        self.find_element(*self.last_data_loc).click()
        sleep(2)
        self.find_element(*self.check_datetime_loc).click()
        self.find_element(*self.last_data_loc).click()
        self.find_element(*self.check_day_end_loc).click()

    def judge_day_customize(self):
        """ 判断自定义【日】查询是否成功 """
        hour_text = self.find_element(*self.judgment_customize_hour_loc).text
        return hour_text




    if __name__ == '__main__':
        string = "11-02 03:00 - 11-02 04:00"
        list = string.split(" - ")
        print(list[0])

