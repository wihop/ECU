from HTMLTestRunner import HTMLTestRunner
import unittest
from data import ECUdata
import time

now = time.strftime("%Y_%m_%d")
if __name__ == '__main__':
    # 测试报告文件时间戳名称
    fileName = "ECUTest_%s.html" % now
    # 测试报告保存路径+名称
    file_path = r"./report/%s" % fileName
    fp = open(file_path, "wb")
    # 测试案例目录
    test_dir = r'C:\Users\wt\PycharmProjects\小安协议接口\testcase'
    discover = unittest.defaultTestLoader.discover(test_dir, 'test_*.py')
    runner = HTMLTestRunner(stream=fp, title="%s_v%s版本测试报告"%(ECUdata.devName, ECUdata.devVsn), description="接口测试执行情况")
    # 执行已保存的案例
    runner.run(discover)
    fp.close()
