# -*- coding = utf-8 -*-
# @Time : 2020/5/7 21:32
# @Author : AX
# @File : whut.py
# @Software: PyCharm
import urllib.request
import urllib.error
import urllib.parse
import hashlib

# MsgID=&KeyID=&UserName=&Password=&rnd=64183&return_EncData=&code=9219201675&userName1=9c518de98e8b84c94fd2932ceda771d6&password1=20b37818d645b6307eb3f9fb2d9b38c4269aa9d2&webfinger=8e9444ad687caac8ab5be6731715c549&type=xs&userName=0121810870217&password=AX.xgp000908
# 1.指定URL
url = "http://sso.jwc.whut.edu.cn/Certification/login.do"
# 2.通过请求头设置为浏览器
# data = {
#     "MsgID": "",
#     "KeyID": "",
#     "UserName": "",
#     "Password": "",
#     "rnd": 64183,
#     "return_EncData": "",
#     "code": 9219201675,
#     "userName1": "9c518de98e8b84c94fd2932ceda771d6",
#     "password1": "20b37818d645b6307eb3f9fb2d9b38c4269aa9d2",
#     "webfinger": "8e9444ad687caac8ab5be6731715c549",
#     "type": "xs",
#     "userName": "0121810870217",
#     "password": "AX.xgp000908",
# }


username = "0121810880322"
username1 = hashlib.md5(bytes(username.encode("utf-8")))
username1 = username1.hexdigest()
password = "ykh20001229"
temp = username + password
password1 = hashlib.sha1(bytes(temp.encode("utf-8")))
password1 = password1.hexdigest()
print(username1, password1)
data = "MsgID=&KeyID=&UserName=&Password=&rnd=64183&return_EncData=&code=9219201675&userName1=" + username1 + "&password1=" + password1 + "&webfinger=b9a7a7901c83c4c0dad90bd2bbf19498&type=xs&userName=" + username + "&password=" + password
data = bytes(data.encode('utf-8'))
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    # "Cookie": "JSESSIONID=975C46D733324E0799A4ACAAC7DB1FC6"
}
# 975C46D733324E0799A4ACAAC7DB1FC6  BC196C4FF21BD35F209DE693F08517B4
# 3.封装req对象
try:
    req = urllib.request.Request(url=url, headers=headers, method="POST", data=data)
except urllib.error.URLError as e:
    if hasattr(e, "code"):
        print(e['code'])
# 4.进行爬取
response = urllib.request.urlopen(req)
# 5.解码阅读
st = str(response.read().decode('utf-8'))
with open('baidu.html','w') as file:
    file.write(st)

print(st)
