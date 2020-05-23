# -*- coding = utf-8 -*-
# @Time : 2020/5/7 18:11
# @Author : AX
# @File : testUrllib.py
# @Software: PyCharm

import urllib.request
import urllib.error
import urllib.parse

# 获取一个get请求
# 要进行utf-8解码 .read()用来读取
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))


# 获取一个post请求
# import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
# response = urllib.request.urlopen("https://httpbin.org/post", data=data)
# print(response.read().decode("utf-8"))


# 超时处理
# try:
#     response = urllib.request.urlopen("https://httpbin.org/get",timeout=0.1)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print("time out！")

# response = urllib.request.urlopen("http://httpbin.org/get")
# print(response.status)

# response = urllib.request.urlopen("http://baidu.com")
# print(response.getheader("Server"))


# 伪装成浏览器
# url = "https://www.douban.com"
# url ="https://httpbin.org/post"
# url = "https://httpbin.org/post"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
# }
# data = bytes(urllib.parse.urlencode({'name': 'AX'}), encoding="utf-8")
# req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
#
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))

# 1.指定URL
url = "https://www.baidu.com"
# 2.通过请求头设置为浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
}
# 3.封装req对象
req = urllib.request.Request(url=url, headers=headers)
# 4.进行爬取
response = urllib.request.urlopen(req)
# 5.解码阅读
st = str(response.read().decode('utf-8'))
print(st)

# f = open("baidu.html", "w", encoding='utf-8')
# print("begin write")
# f.write(st)
# f.close()
