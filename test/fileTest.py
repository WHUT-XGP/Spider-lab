# -*- coding:utf-8 -*-
# @Time : 2020/5/25 10:11
# @Author : AX
# @File : fileTest.py
# @Software: PyCharm
import requests

if __name__ == '__main__':
    file = requests.get(
        "http://tmp/wxb3a8c258fd1798f6.o6zAJs4bo7XRNpKBe4FVpaxH__R4.l0YCmgCaDg28a7acf4219a80d27f51d0e5ea670f2c50.jpg")
    with open("test.jpg", "wb") as f:
        f.write(file.content)
