#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/4 07:11

from api.file_api import target_match_path, cm_test, detect

if __name__ == '__main__':
    # 监听某目录下是否有新文件产生
    # path = '/Users/ambition/test_pro'
    path = 'I:\\bishexiangguan\\test'
    second = 1

    # 监听某目录是否有新文件产生
    # for file_name in detect(path, second):
    #     print(file_name)

    # 特征码匹配文件是否为webshell
    target_match_path(path)

    # 文件创建与修改时间来判断是否为webshell
    # for k, v in cm_test(path).items():
    #     print(k, v)
