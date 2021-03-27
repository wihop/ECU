import time

now = time.strftime("%Y_%m_%d")

# 测试案例目录
TestCase_dir = r"C:\Users\wt\PycharmProjects\小安协议接口\testcase"

# 测试报告文件路径时间戳名称
report_path = r"C:\Users\wt\PycharmProjects\小安协议接口\report"
report_name = "ECUTest_%s.html" % now
ReportPath_name = report_path + "/" + report_name
