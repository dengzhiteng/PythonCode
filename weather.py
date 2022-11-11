# coding:utf -8
# 获取指定城市的天气
import requests

url = "http://t.weather.sojson.com/api/weather/city/"
# addrCodes = ['101250101','101250501','101280101','101280601']
addrCodes = ['101250101','101250501']

dic_foreCast={}

for code in addrCodes:
    res =requests.get(url+code)
    if(res.status==200):
        dic_foreCast[code]=res.text

print(dic_foreCast)