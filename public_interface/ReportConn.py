'''
    导出报告优化处理接口
'''
import os


class ReportConn():

    '''失败截图'''
    def save_img(self,driver, test_method):  # 失败截图方法（必须要定义在class中）
        # root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/')
        # img_path = root_dir + '/img'
        base_dir = os.path.dirname(os.path.dirname(__file__))
        base_dir = str(base_dir)
        base_dir = base_dir.replace('\\', '/')
        base = base_dir.split('public_interface')[0]
        img_path = base + "/report/image/"
        driver.get_screenshot_as_file(u'{}/{}.png'.format(img_path, test_method))