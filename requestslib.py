import requests
import json

#带参数的get
# headers={
#     'Accept': 'application/json, text/plain, */*',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
# }
# res =requests.get('https://api.iviewui.com/v1/asd/list?name=2',headers=headers,)
# data = json.loads(res.text)
# print('res',data['data'])

# 带参数的post
headers={
    'Accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
data = {'key1':'value1','key2':'value2'}
url ='https://stats.g.doubleclick.net/j/collect'
res =requests.post(url=url,headers=headers,data=data)
print('res',res.text)
