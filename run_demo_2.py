import unittest
import BeautifulReport as br
from ECUData import ECUdata
from conf.dirpath import *


if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    all_case = unittest.defaultTestLoader.discover(TestCase_dir, 'test_*.py')
    # 执行已保存的案例
    [test_suite.addTests(case) for case in all_case]
    report = br.BeautifulReport(test_suite)
    report.report(description="%s_v%s版本测试报告" % (ECUdata.devName, ECUdata.devVsn), filename=report_name, log_path = report_path)
