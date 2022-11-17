from dingtalkchatbot.chatbot import DingtalkChatbot
from datetime import  datetime

def send_markdown(bot):
    red_msg = '<font color="#dd0000">级别:危险</font>'
    orange_msg = '<font color="#FFA500">级别:警告</font>'
    now_time = datetime.now().strftime('%Y.%m.%d %H:%M:%S')
    url = 'https://blog.csdn.net/qq_46158060?type=blog'
    bot.send_markdown(
        title=f'来自梦无矶小仔的提醒',
        text=f'### **我是主内容的第一行**\n'
             f'**{red_msg}**\n\n'
             f'**{orange_msg}**\n\n'
             f'**发送时间:**  {now_time}\n\n'
             f'**相关网址:**[点击跳转]({url}) \n',
        is_at_all=True)

def send_text(bot):
    bot.send_text(msg='我就是我, 是不一样的烟火', is_at_all=False)

def send_image(bot):
    bot.send_image(pic_url='https://img-blog.csdnimg.cn/255fb93f92ec463ca08e959181cf2c90.png')

def send_link(bot):
    bot.send_link(title='万万没想到，李小璐竟然...', text='故事是这样子的...', message_url='http://www.kwongwah.com.my/?p=454748", pic_url="https://pbs.twimg.com/media/CEwj7EDWgAE5eIF.jpg')

def dingtalk_robot(webhook,secret):
    dogBOSS = DingtalkChatbot(webhook, secret)
    # send_markdown(dogBOSS)
    send_text(dogBOSS)
    # send_image(dogBOSS)
    # send_link(dogBOSS)

if __name__ == '__main__':
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=d8df16b2c85f6a60636238b2c125ffe915e7e94f8dd86b6fbe780256f24e1b91'
    secrets = 'SEC62b015f48045c57945515b56d802d4d18028200e462360a33f40d961626598a2'
    dingtalk_robot(webhook=webhook,
                   secret=secrets)