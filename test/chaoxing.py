# -*- coding = utf-8 -*-
# @Time : 2020/5/11 21:56
# @Author : AX
# @File : chaoxing.py
# @Software: PyCharm
import requests
import math


def request(url, header, params, methods, cookies):
    res = requests.request(method=methods, url=url, headers=header, params=params, cookies=cookies)
    return res.text


url = "https://mooc1-1.chaoxing.com/mycourse/studentcourse"
params = {
    "courseId": "208811846",
    "clazzid": "18032834",
    "vc": "1",
    "cpi": "124973121",
    "enc": "9ca62abcb7a0d024cbdeee442f083819"
}
cookies = open("cookie.txt", "r")
cookies = cookies.read().rstrip()
print(cookies)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}
print(request(url=url, header=headers, params=params, methods="GET", cookies=cookies))
