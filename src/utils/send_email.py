# -*- coding: UTF-8 -*-
# /usr/bin/env python

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart


def Emails(sender, receivers, file, token):
    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header(sender, 'utf-8')  # 发送者
    message['To'] = Header("hero", 'utf-8')  # 接收者

    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    # 带有附件的邮件正文内容
    message.attach(MIMEText('想要的自己拿来', 'plain', 'utf-8'))

    # 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open(file, 'r').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="' + file + '"'
    message.attach(att1)

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect("smtp.163.com", 25)  # 25 为 SMTP 端口号
        smtpObj.login("15991607065@163.com", token)
        smtpObj.sendmail(sender, receivers, message.as_string())
        return "邮件发送成功"
    except smtplib.SMTPException:
        return "Error: 无法发送邮件"


sender = '15991607065@163.com'
receivers = ['yli@fintechautomation.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
file = 'demo.txt'
token = 'JMCKDTQVFRNWLLFW'
Emails(sender, receivers, file, token)
