from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import smtplib
import os


# 定义发送邮件
def send_mail(file):
    f = open(file, 'rb',).read()
    # f.close()
    att = MIMEText(f, 'base64', 'utf-8')
    att['content-type'] = 'application/octet-stream'
    att['content-disposition'] = "attachment; filename ='testing_result.html'"
    msg = MIMEText('各位好，附件是本次的测试报告，请查阅!谢谢', 'plain', 'utf-8')

    msg_all = MIMEMultipart('related')
    msg_all['Subject'] = Header('自动化测试报告', "utf-8")

    print('添加附件')
    msg_all.attach(att)
    print('添加成功')
    msg_all.attach(msg)

    smtp = smtplib.SMTP()    # 简单邮件传输协议
    smtp.connect('smtp.qq.com', 25)     # 邮箱服务器
    smtp.login('1106334809@qq.com', 'hjoyprrynbiegbch')        # 登录邮箱
    smtp.sendmail('1106334809@qq.com', '1106334809@qq.com', msg_all.as_string())     # 发送者和接收者
    smtp.quit()
    print("邮件已发出！注意查收。")


# 查找测试报告
def find_report(address):
    lists = os.listdir(address)
    # lists.sort(key=lambda fn: os.path.getmtime(address + '\\' + fn))
    file_new = os.path.join(address, lists[-1])
    print(file_new)
    return file_new
