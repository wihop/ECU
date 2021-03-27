from HTMLTestRunner import HTMLTestRunner
import unittest
from conf.email import find_report,send_mail
from conf.dirpath import *

if __name__ == '__main__':
    # 在测试案例目录加载以test开头的案例集
    discover = unittest.defaultTestLoader.discover(TestCase_dir, pattern='test*.py')
    fp = open(report_name, 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况')
    # 执行已保存的案例集
    runner.run(discover)
    fp.close()
    # 生成和发送邮件
    new_report = find_report(report_path)
    print(new_report)
    send_mail(new_report)
