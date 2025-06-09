#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
运行测试用例
@Project ：CommonUseCase
@File ：run_bbs_test.py
@Author ：xie.xiaolan
@Date ：2022/7/8 10:40
"""

from BeautifulReport import BeautifulReport
from email.mime.text import MIMEText
import smtplib
import unittest
import time
import os,datetime
# =========================邮件接收者============================
mailto_list=["xie.xiaolan@qkupower.com"]
#============= 设置服务器，用户名、口令以及邮箱的后缀===============
mail_host="smtp.qq.com"
mail_user="1289458872@qq.com"
mail_pass="qmwvgugghvpgjifd"
#===========================发送邮件============================
def send_mail(to_list,file_new):
    """''
    to_list:发给谁
    sub:主题
    content:内容
    send_mail("aaa@126.com","sub","content")
    """
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    me=mail_user
    msg = MIMEText(mail_body,'html','utf-8')
    msg['Subject'] = u'自动化测试报告'
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host,25)
        s.login(mail_user,mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception as e:
        print(e)
        return False

#==============查找测试报告目录，找到最新生成的测试报告文件==========
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn:os.path.getatime(testreport + "\\" + fn))
    file_new = os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new

if __name__ == '__main__':

    root_dir = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
    now = datetime.datetime.now().strftime('%Y-%m-%d %H_%M_%S')
    filename = '登录自动化报告' + str(now)
    discover = unittest.defaultTestLoader.discover('./test_case',
                                                   pattern='*_sta.py')
    report_dir = root_dir + '/report'
    runner = BeautifulReport(discover).report(description='登录自动化测试报告', filename=filename, report_dir=report_dir,
                                     theme="theme_cyan")

    # now = time.strftime("%Y-%m-%d %H_%M_%S")
    # filename = './bbs/report/' + now +'result.html'
    fp = open(filename,'wb')

    # runner.run(discover)
    fp.close()
    file_path = new_report('./report/')

    if send_mail(mailto_list,file_path):
        print (u"发送成功")
    else:
        print(u"发送失败")

