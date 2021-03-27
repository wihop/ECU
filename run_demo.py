from HTMLTestRunner import HTMLTestRunner
import unittest
from ECUData import ECUdata
from conf.dirpath import *


if __name__ == '__main__':
    fp = open(ReportPath_name, "wb")
    discover = unittest.defaultTestLoader.discover(TestCase_dir, 'test_*.py')
    runner = HTMLTestRunner(stream=fp, title="%s_v%s版本测试报告"%(ECUdata.devName, ECUdata.devVsn), description="接口测试执行情况")
    # 执行已保存的案例
    runner.run(discover)
    fp.close()
