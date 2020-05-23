# -*- coding = utf-8 -*-
# @Time : 2020/5/7 15:38
# @Author : AX
# @File : 文件基本操作.py
# @Software: PyCharm

# 打开文件 w(写模式） 文件不存在就创建 r只读（默认） a追加写入
# rb以二进制打开用于只读 wb二进制打开用于写入
# ab用于打开二进制追加写入 r+打开一个文件用于读写，指针位于开头 w+不存在则创建新文件
# f = open('test.txt', "w")

# f.write("Hello World")  # 将字符串写入文件中
'''
content = f.read(5)
print(content)  # Hello
content = f.read(5)
print(content)  # Worl
f.close()  # 关闭文件
'''

f = open("test.txt", "r")
content = f.readlines()
print(content)  # ['Hello World\n', 'Hello World\n', 'Hello World\n', 'Hello World\n', 'Hello World']
f.close()

f = open("test.txt", "r")
content = f.readline()
print(content)  # Hello World
f.close()

