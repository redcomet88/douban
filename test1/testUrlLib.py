# -*- codeing = utf-8 -*-
# Author: Redcomet
# QQ: 626206333
# @Time :2022/1/19 10:10
# @Author: Administrator
# @File :testUrlLib.py

import urllib.request

# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))

data = bytes(urllib.parse.urlencode({"hello":"world"}), encoding="utf-8")
response = urllib.request.urlopen("http://httpbin.org/post", data= data)
print(response.read().decode("utf-8"))