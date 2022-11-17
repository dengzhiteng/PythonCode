# coding:utf -8
# 以附件的形式爬取长沙 郴州 深圳 广州 四个地方近15天的数据,
# 并以附件的形式发送到邮箱 mrdengzhiteng@163.com
import requests
import json
import time
from dztModule import sendMail

addrCodes = ['101250101','101250501','101280101','101280601','101250401','101010100']
weatherList=[]

print('*'*10,'爬取天气中....')
for code in addrCodes:
    url = f"http://t.weather.sojson.com/api/weather/city/{code}"
    res = requests.get(url)
    data =json.loads(res.text)
    if data['status'] !=200:
        continue
    else:
        info={'cityInfo':data['cityInfo'],'data':data['data']};
        weatherList.append(info)
    time.sleep(1)

# 今日天气
def createThead(fileds):
    thead_html=''
    for filed in fileds:
        thead_html+=f'<th>{filed}</th>'
    return   f'''<thead>{thead_html}</thead>'''

def createTr(info):
     data =info['data']
     cityInfo = info['cityInfo']
     return f'''<tr>
        <td>{cityInfo['city']}</td>
        <td>{data['wendu']}℃</td>
        <td>{data['quality']}</td>
        <td align="left">{data['ganmao']}</td>  
    </tr>'''
thead_html=createThead(['地区','温度','空气质量','提醒'])

tbody_html=''
for weather in weatherList:
    tbody_html += createTr(weather)

tbody_html = f'''<tbody>{tbody_html}</tbody>'''
send_msg = f'''
   <table border='1' cellspacing="0">
       {thead_html}
       {tbody_html}  
   </table>
   '''

# 发送天气到邮箱
now_time = time.strftime('%Y-%m-%d', time.localtime())
subject = f"【今日天气预报】{now_time}"
sender = "mrdengzhiteng@163.com"
recver =["mrdengzhiteng@163.com"]
sendMail.send(sender, recver, subject, send_msg, 'html')
time.sleep(2)