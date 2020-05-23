# -*- coding = utf-8 -*-
# @Time : 2020/5/7 17:27
# @Author : AX
# @File : Spider.py
# @Software: PyCharm


from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式,进行文字匹配
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作
import requests


def getData():
    print("爬取开始：")
    data = []
    count = 1
    for i in range(10):
        print("当前正在爬取第%d页" % (i + 1))
        html = askURL("https://movie.douban.com/top250?start=" + str(i * 5))
        soup = BeautifulSoup(html, "html.parser")


        for item in soup.select("div .item"):
            # print(item)
            img_href = item.select("img")[0].attrs['src']

            movie_detail_href = item.select("a")[0].attrs['href']

            current_movie = item.select("a .title")

            if len(current_movie) >= 2:
                movie_chinese_name = current_movie[0].string
                movie_foreign_name = current_movie[1].string[2:]
            else:
                movie_chinese_name = current_movie[0].string
                movie_foreign_name = "无外文名"
            # print(movie_chinese_name,movie_foreign_name)
            comment_grade = item.select(".rating_num")[0].string
            comment_num = re.findall(re.compile(r"\d+人评价"), str(item.select(".star span")))
            comment_num = re.findall(re.compile(r"\d+"), comment_num[0])[0]
            # print(comment_num, comment_grade)
            movie_detail = item.select("p .inq")[0].string
            movie_info = str(item.select(".bd p")[0]).replace("<br/>", "")
            movie_info = movie_info.replace(" ", "")
            movie_info = movie_info.replace("<pclass=\"\">", "")
            movie_info = movie_info.replace(r"</p>", "")
            movie_info = movie_info.replace("\n", "")
            data.append(
                {
                    "count": count,
                    "name": movie_chinese_name,
                    "foreign": movie_foreign_name,
                    "imgUrl": img_href,
                    "detailUrl": movie_detail_href,
                    "commentNum": comment_num,
                    "commentGrade": comment_grade,
                    "movieInfo": movie_info,
                    "movieDetail": movie_detail

                }
            )
            count += 1
            # print(movie_detail)
    # print(data)
    print("爬取完成！")
    return data


# 得到指定一个URL的网页内容
def askURL(url):
    # 用户代理，告诉服务器我们是什么内容的机器
    head = {  # 模拟浏览器头部信息
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 81.0.4044.138afari / 537.36"
    }
    try:
        response = requests.get(url=url, headers=head)
        html = response.text
        # print(html)
    except requests.exceptions as e:
        print(e)
    return html


def saveData(data):
    print("保存中...")
    writebook = xlwt.Workbook(encoding='utf-8')
    writesheet = writebook.add_sheet("豆瓣top250")
    name = ["电影排名", "电影名称", "电影外文名", "图片详情", "电影详情链接", "评价人数", "评分", "电影人员/类型", "电影概述"]
    for i in range(len(name)):
        writesheet.write(0, i, name[i])

    for i in range(1, len(data) + 1):
        j = 0
        for item in data[i - 1].values():
            writesheet.write(i, j, item)
            j += 1

    writebook.save("豆瓣top250.xls")
    print("已保存")


def main():
    data = getData()
    saveData(data)


# 指定程序入口
if __name__ == "__main__":  # 当函数执行时
    # 调用函数
    main()
