# -*- coding = utf-8 -*-
# @Time : 2020/5/10 23:59
# @Author : AX
# @File : res.py
# @Software: PyCharm

import requests

# 设置header
headers = {
    "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 81.0.4044.138afari / 537.36"
}
# allow_redirects=False 拒绝重定向 cookies设置cookie header设置request header params给定设置参数 timeout设置超时时间
res = requests.get("http://movie.douban.com/top250", headers=headers)
print(res.text)
print(res.history)
