#!/usr/bin/python3
# encoding='utf-8'

# 定义变量
# counter = 1001          # 整型变量
# miles = 1000.0       # 浮点型变量
# name = "runoob"     # 字符串

#a = b = c = 1
# a, b, c = 1, 2, "john"
# print(a,b,c)

# if
# if 1==1:
#  print ("成立")
# elif 2==1:
#  print('不成立')
# else:
 # print('不成立')

# 多行语句
# moreRow = 'item_one + \
#         item_two + \
#         item_three'
# print(moreRow)

# userName='张三'
# age=18

#换行输出
# print(userName)
# print(age)
#不换行输出
# print(userName,age)

# s = 'abcdef'
# print(s[1:5])
# print(s[1:5])

#while
# index=1
# while(index<=10):
#  if(index%2==0):
#   print(index,'is even')
#  else:
#   print(index,'is odd')
#  index+=1

# import time
# # 时间戳 单位为 s
# temp = time.time()
# print(temp)
#
# def test1():
#  print('test1')
#  return
#
# def test2():
#  print('test2');
#  return
#
# if False:
#  test1()
# else:
#  test2()


# for index in range(10,20):
#  print(index)

"""
fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
 print('当前水果 : ' + fruits[index])
print("Good bye!")
"""

# x=int(input("请输入年龄: "))
# if(x>=18):
#     print('成年人')
# else:
#     print('未成年人')


# if 1 :
#     pass
# else:
#     pass

# for item in range(1,10,2):
#     print(item)
#
# print('*'*20)
#
#
# for item in range(1,10):
#     print(item)

# import  keyword
# print(keyword.kwlist)

# case1

# arr = ['Mary', 'had', 'a', 'little', 'lamb']
# for index in range(len(arr)):
#     print(arr[index])

#case2 for
# for index in range(10):
#     if index%2==0:
#         print('偶数',index)
#     else:
#         print('奇数',index)

#case2 while
# i=0
# while i<100:
    # if(i>=10):break;
    # i+=1
    # print(i)

# list
# list =[1,2,3]
# list.append(1)
# print(list,id(list))
# list_copy = list.copy()
# print(list_copy,id(list_copy))

# print(list[0])
# del list[1:2]
# print(list[0])

# 定义函数
# def fntest():
#     pass
#     return 1,2,2,1,3,4,5
# print(fntest())


# 构造一个 1,3,5,7,9,....99 数列
# arr=[]
# for i in range(1,100,2):
#     arr.append(i)
# print(arr)

# 切片
# arr = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# print(arr[0:1])

# arr1=list(range(1,101))
# print(arr1[:10])
# print(arr1[-10:])
# print(arr1[:])

# print(range(100))

# obj = {'a': 1, 'b': 2, 'c': 3}
# for key in obj:
#     print(key,obj[key])

# for s in 'Python':
    # print(s)

# arr =[x * x for x in range(1, 11)]
# print(arr) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# arr =[x * x for x in range(1, 11) if x % 2 == 0]
# print(arr)  #[4, 16, 36, 64, 100]

#open
# with open('./static/mail.txt',encoding='utf-8') as fo:
#     ss =fo.read()
#     print(ss)

#zipfile
import zipfile
# zf = zipfile.ZipFile("2.zip",'w')
# zf.write('./static/mail.txt')
# zf.close()

# 解压 (一直失败)
# zf=zipfile.ZipFile("2.zip")
# zf.extractall()

#字符串
# s1 = '我叫{0},今年{1}岁'.format('小明1',1)
# print(s1)
#
# s2 = '我叫{name},今年{age}岁'.format(name='小明2',age=2)
# print(s2)

# print('我是%s,今年%d岁'%('小明',1))






