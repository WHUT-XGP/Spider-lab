# -*- coding = utf-8 -*-
# @Time : 2020/5/10 20:36
# @Author : AX
# @File : bs4test.py
# @Software: PyCharm

from bs4 import BeautifulSoup

file = open("index2.html", 'rb')  # 注意此处为二进制
html = file.read()
file.close()
# print(html)
bs = BeautifulSoup(html, 'html.parser')
# print(bs)
# Tag 标签及其内容（默认只能拿到第一个）
# print(bs.title.string)
# print(bs.script)
# print(bs.head)

# print(bs.ul.attrs)
#
# print(type(bs))    # <class 'bs4.BeautifulSoup'>
#
# print(bs.name)      # [document]

# 文档的遍历
# print(bs.head.contents)

import re
# 字符串过滤
# t_list = bs.find_all(re.compile("ul"))

# 正则表达式搜索：使用search()方法匹配
# kwargs  参数
t_list = bs.find_all(id="ps")

# print(t_list)
# t_list = bs.find_all(text=re.compile("\d"))
# for item in t_list:
#     print(item)

# 选择器：
print(bs.select('div #out'))
