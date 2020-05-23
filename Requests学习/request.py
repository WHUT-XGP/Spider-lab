# -*- coding = utf-8 -*-
# @Time : 2020/5/10 23:11
# @Author : AX
# @File : whutreq.py
# @Software: PyCharm
import requests
import time

seach = "诡秘之主"
payload = {
    "searchKey": seach
}


# 使用res.text得到html
# res = requests.get("https://www.52bqg.com/modules/article/search.php",params=payload)
# res.encoding="gbk"
# print(res.text)
# print(res.url)

# res = requests.get("https://static.firefoxchina.cn/202005/s8252umVZN8S4X348Hity3fc1AOvCnRoDoFCefRi.jpeg")
# # 使用res.content来保存二进制
# # 如图片则可以使用Image库和BytesIO
# with open("temp.jpeg","wb") as file:
#     file.write(res.content)
def downLoad(url):
    res = requests.get(url)

    with open("麻雀.mp3", "wb") as file:
        file.write(res.content)
    print("%s下载完成！" % url)


def main():
    downLoad("http://m10.music.126.net/20200511001326/ca8a7850fe239be1a4be4b8a45538971/ymusic/555b/0f58/0609/b1e0b087cb826dde13b21cbaa504f963.mp3")


if __name__ == '__main__':
    main()
