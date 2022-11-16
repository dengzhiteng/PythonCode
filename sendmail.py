# coding:utf -8
from dztModule import sendMail
import requests
# from bs4 import BeautifulSoup
# url = 'http://www.anche.cn'
# req = requests.get(url)
# req.encoding='utf-8'
# data = req.text

file = open('./static/mail.html', 'r', encoding='utf-8')     # 打开文件
data = file.read() # 读取文件内容

sender = "mrdengzhiteng@163.com"
subject = "【python机器人发送的邮件】"
recverList = ['mrdengzhiteng@163.com']

print("*" * 10, '发送中.....')
for recver in recverList:
    sendMail.send(sender,recver,subject,data,'html')
print("*" * 10, f'发送完毕,共发送{len(recverList)}封邮件')


