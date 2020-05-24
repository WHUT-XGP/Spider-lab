# -*- coding = utf-8 -*-
# @Time : 2020/5/23 16:45
# @Author : AX
# @File : testSelenium.py
# @Software: PyCharm

from selenium import webdriver

if __name__ == '__main__':
    path = r"D:\selenium-browserDriver-path\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get("https://www.icourse163.org/")

