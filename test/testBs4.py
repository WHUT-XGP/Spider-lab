# -*- coding = utf-8 -*-
# @Time : 2020/5/7 19:36
# @Author : AX
# @File : testBs4.py
# @Software: PyCharm


'''
BeautifulSoup4 将复杂HTML文档转换成一个复杂的树形结构DOM，每个节点都是python对象，所有对象可以归纳为4种
- Tag
- NavigableString
- BeautifulSoup
- Comment
'''

from bs4 import BeautifulSoup

file = open("baidu.html", 'rb')
html = file.read()
bs = BeautifulSoup(html, "html.parser")

# print(bs.title)
# print(bs.a)
# print(bs.head)
# print(type(bs.head))

# 1.Tag html标签及其内容：拿到它所找到的第一个内容

# 2.NavigableString 标签内的内容

# print(bs.title.string)
# print(type(bs.title.string))

# 标签的属性
# print(bs.a.attrs)

# 3.BeautifulSoup 表示整个文档
# print(type(bs))
# print(bs.name)

# 4. Comment 是一个特殊的NavigableString 输出的内容不包括注释符号（字符串）
# print(bs.a.string)


# ----------------------

# 文档的遍历

# print(bs.head.contents)
# print(bs.head.contents[0])

# 文档的搜索
# 1.find_all()
# 字符串过滤：会查找与字符串完全匹配的内容
# t_list = bs.find_all("a")

import re

# 2.正则表达式搜索：使用search()方法来匹配内容
# t_list = bs.find_all(re.compile("a"))

# 3.传入一个函数来搜索(了解)
# def name_is_exists(tag):
#     return tag.has_attr("name")
# t_list =bs.find_all(name_is_exists)
#
#
# for item in t_list:
#     print(item)

# print(t_list)

# kwargs 参数
# t_list =bs.find_all(href="https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_1")
# for item in t_list:
#   print(item)

# 文本参数
# t_list = bs.find_all(text=re.compile("\d"))
# for item in t_list:
#     print(item)

# limit参数：
# t_list = bs.find_all("a",limit=3)
# print(t_list)

# CSS选择器：bs.select   .get_text()
# print(bs.select('.mnav'))
t_list = bs.select("#u1>#virus-2020")
print(t_list[0].get_text())
# print(bs.select("#u1>#virus-2020"))
