import unittest
import BeautifulReport as br
from data import ECUdata
import time

now = time.strftime("%Y_%m_%d")
if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    # 测试案例目录
    test_dir = r'C:\Users\wt\PycharmProjects\小安协议接口\testcase'
    # 测试报告文件时间戳名称
    fileName = "ECUTest_%s.html" % now
    # 测试报告保存路径
    file_path = r"./report/"
    all_case = unittest.defaultTestLoader.discover(test_dir, 'test_*.py')
    # 执行已保存的案例
    [test_suite.addTests(case) for case in all_case]
    report = br.BeautifulReport(test_suite)
    report.report(description="%s_v%s版本测试报告" % (ECUdata.devName, ECUdata.devVsn), filename=fileName, log_path=file_path)
