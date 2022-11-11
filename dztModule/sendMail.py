# coding:utf -8
import smtplib  # smtp服务器
from email.mime.text import MIMEText  # 邮件文本

# 发送邮件 format默认发送文本
def send(sender,recver,subject,content,format='plain'):
    password = "UIKYSAZTNQGWNYFR" # 邮箱授权码,不要外泄,后果很严重
    # content 发送内容   "plain"文本格式   utf-8 编码格式
    message = MIMEText(content, format, "utf-8")
    message['Subject'] = subject  # 邮件标题
    message['To'] = recver  # 收件人
    message['From'] = sender  # 发件人
    smtp = smtplib.SMTP_SSL("smtp.163.com", 994)  # 实例化smtp服务器
    smtp.login(sender, password)  # 发件人登录
    smtp.sendmail(sender, [recver], message.as_string())  # as_string 对 message 的消息进行了封装
    smtp.close()
    return