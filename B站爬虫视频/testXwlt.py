# -*- coding = utf-8 -*-
# @Time : 2020/5/13 13:26
# @Author : AX
# @File : testXwlt.py
# @Software: PyCharm

import xlwt

workbook = xlwt.Workbook(encoding="utf-8")  # 创建workbook对象，参数为编码
worksheet = workbook.add_sheet("sheet1")  # 创建单元表,参数为表名
worksheet.write(0, 0, "hello")  # 写入数据，第一个参数为行，第二个参数为列，第三个参数为写入内容
workbook.save("hello.xls")  # 进行保存 参数为文件名
