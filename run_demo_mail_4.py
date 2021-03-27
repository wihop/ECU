import BeautifulReport as br
import unittest
from ECUData import ECUdata
from conf.email import find_report ,send_mail
from conf.dirpath import *

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    # 在测试案例目录加载以test开头的案例集
    all_case = unittest.defaultTestLoader.discover(TestCase_dir, 'test_*.py')
    # 执行已保存的案例
    [test_suite.addTests(case) for case in all_case]
    report = br.BeautifulReport(test_suite)
    report.report(description="%s_v%s版本测试报告" % (ECUdata.devName, ECUdata.devVsn), filename=report_name, log_path=report_path)
    # 生成邮件和发送邮件
    new_report = find_report(report_path)
    print(new_report)
    send_mail(new_report)
