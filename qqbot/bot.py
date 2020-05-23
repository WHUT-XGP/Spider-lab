# -*- coding = utf-8 -*-
# @Time : 2020/5/11 9:28
# @Author : AX
# @File : bot.py
# @Software: PyCharm

import nonebot

import qqbot.config

if __name__  == '__main__':
    nonebot.init(config_object=qqbot.config)
    nonebot.load_builtin_plugins()
    nonebot.run(host='127.0.0.1', port=8080)