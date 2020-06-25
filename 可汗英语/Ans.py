# -*- coding:utf-8 -*-
# @Time : 2020/6/20 13:03
# @Author : AX
# @File : Ans.py
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup
import re

"""
testID:参数 url的最后一位
"""
def requestTest(testId):
    # 指定url
    url = "http://jxpt.whut.edu.cn:81/meol/common/question/test/student/stu_qtest_result.jsp"
    # 一般header 无明显防爬手段的话，只需要加入User-Agent,如果还是进不去那就加个Host 再进不去就认真找找有没有反token
    headers = {
        "User-Agent": r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebK"
                      r"it/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
    }
    # cookies 一般在控制台可以拿到数据，多个cookie的话就写成这个形式，也可以写进headers里面（一般不推荐）
    # cookies 一般是和账号绑定的，所以一般有相应前端加密手段，
    # 这里似乎还是用的武理祖传md5和hash，一般这个是爬虫难点，需要检查js源码或者模拟运行

    cook = {

    }
    # params 这个命令不好，应该叫query 也就是url的query参数,在这里指定为我们testId
    params = {
        "testId": testId
    }
    # 开始爬取
    html = requests.get(url=url, headers=headers, cookies=cook, params=params)
    # 打印结果
    print(html)
    # 保存最后结果的数组
    txt_content = []
    # 开始解析题目
    # 初始化bs
    bs = BeautifulSoup(html.text, "html.parser")
    # 根据网页特点选择所有的Input
    test = bs.select("input")
    # 遍历寻找
    for item in test:
        # 寻找有value的 input
        # 利用正则来搜索 这里双重否定表肯定（脑残操作）可以改写为if re.search(re.compile("value"),str(item))
        if not re.search(re.compile("value"), str(item)) is None:
            # 保存题目
            title = ''
            # 进一步提取文字,在这里将value里的值又作为html再次解析（傻逼武理）
            sBr = BeautifulSoup(str(item.attrs['value']), "html.parser")
            # 选择span
            current_str = sBr.select("span")
            # 避免出现那个轮回那样的嵌套情况
            for text in current_str:
                title = title + str(text.string)
            # 将题目加入数组s
            txt_content.append({
                '题目': title
            })

    # 解析答案：
    ans = bs.select(".Fimg")
    # 用于标记下标
    count = 0
    # 对比一下长度差 会发现len(ans)要多...因为有个傻逼试卷解析也是.Fimg 在这里用正则匹配
    print(len(ans))
    print(len(txt_content))
    for item in ans:
        # 正则判断是否为答案
        if not re.search(re.compile("参考答案"), str(item)) is None:
            print(item.string)
            # 加入到对应位置
            txt_content[count]['参考答案'] = item.string
            count =count + 1
    # 打印结果
    # print(txt_content)
    for item in txt_content:
        print(item)
    # 写入
    with open('ans.txt', 'a+', encoding='utf8') as file:
        for item in txt_content:
            file.write('题目：' + str(item['题目'] + '\n参考答案：' + str(item['参考答案'] + '\n')))


if __name__ == '__main__':
    # 31318160
    # 32811098
    # 34676591
    # 31060238
    # 37530819
    requestTest(31318160)
    requestTest(32811098)
    requestTest(34676591)
    requestTest(31060238)
    requestTest(37530819)
