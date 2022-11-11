
import requests
from bs4 import BeautifulSoup
url = 'http://www.anche.cn'
http='http://www.anche.cn'

req = requests.get(url)
req.encoding='utf-8'
html = req.text

bs = BeautifulSoup(html, "html.parser")
# 缩进格式
# print(bs.prettify())

# 获取title标签的所有内容
# print(bs.title)

# 获取title标签的名称
# print(bs.title.name)

# 获取title标签的文本内容
# print(bs.title.string)

# 获取head标签的所有内容
# print(bs.head)

# 获取第一个div标签中的所有内容
# print(bs.div)

# 获取第一个div标签的id的值
# print(bs.div["id"])

# 获取第一个a标签中的所有内容
# print(bs.a)

# 获取所有的a标签中的所有内容
# print(bs.find_all("a"))

# 获取id="u1"
# print(bs.find(id="u1"))

# 获取所有的a标签，并遍历打印a标签中的href的值
# for item in bs.find_all("a"):
#     print(item.get("href"))

# 获取所有的a标签，并遍历打印a标签的文本值
# for item in bs.find_all("a"):
#     print(item.get_text())

def downloadImg(src):
        r = requests.get(src)
        file_name=src.split('/')[-1]
        print('*'*10,'下载图片中.....')
        with open(f"C://Users//dengzhiteng//Desktop//images/{file_name}", "wb")as f:
            f.write(r.content)

count=0
# 获取所有img
for item in bs.find_all("img"):
    src = item.get("src")
    if src.find('https')==-1:
       src = src
    count+=1
    print(src)
    downloadImg(src)

print(f'总共{count}张图片')