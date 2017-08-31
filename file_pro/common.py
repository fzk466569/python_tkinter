#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/2 09:57

import os
import time
from datetime import datetime, date
from util.year import get_days as get_days_years


def get_all_file(path, trust_path=[], trust_file_type=[]):
    path = path.replace('/', '\\')
    # print('get_all_file-trust_file_type', trust_file_type, trust_path)
    # 递归返回一个目录下的所有文件
    # linux 需要取消注释下面这两行
    # if not path.endswith('/'):
    #     path = path + os.sep
    num = 0
    for root, dirs, files in os.walk(path):
        if root in trust_path:
            continue
            # print('root: ', root)
            # print('dirs: ', dirs)
            # print('files: ', files)
        for name in files:
            # print('get_all_file', name.split('.')[-1], trust_file_type)
            if not root.endswith(os.sep):
                root = root + os.sep
            if name.split('.')[-1] not in trust_file_type:
                num += 1
                yield (root + os.sep + name)
                # print('11111111111111111111', root + name)
            else:
                continue
                # print(time.ctime(os.path.getctime(os.path.join(root, name))))
                # print(time.ctime(os.path.getmtime(os.path.join(root, name))))
    print(num)


def get_cur_file(path):
    # 返回一个目录下的所有文件和文件夹
    if not path.endswith('/'):
        path = path + os.sep
    return os.listdir(path)


def get_file_ctime(name):
    # 返回一个文件的创建时间
    return time.ctime(os.path.getctime(name))


def get_file_mtime(name):
    # 返回一个文件的最后修改时间
    return time.ctime(os.path.getmtime(name))


def get_ctime_list(path):
    # 返回一个目录下所有文件和文件夹的创建时间
    if not path.endswith('/'):
        path = path + os.sep
    ctime_list = []
    for f in get_cur_file(path):
        ctime_list.append(os.path.getctime(path + f))
    return ctime_list


def get_cmtime(name):
    return int(os.path.getctime(name) - os.path.getmtime(name))


def get_mtime(name):
    time_stamp = os.path.getmtime(name)
    date_array = datetime.utcfromtimestamp(time_stamp)
    return date_array.strftime("%Y-%m-%d %H:%M:%S")


def get_time_between(name):
    # 返回一个文件cm天数时间差
    a = (time.localtime(get_cmtime(name)))
    return get_days_years(1970, a.tm_year) + a.tm_yday - 1


def convertstringtodate(stringtime):
    if stringtime[0:2] == "20":
        year = stringtime[0:4]
        month = stringtime[4:6]
        day = stringtime[6:8]
        begintime = date(int(year), int(month), int(day))
        return begintime
    else:
        year = "20" + stringtime[0:2]
        month = stringtime[2:4]
        day = stringtime[4:6]
        begintime = date(int(year), int(month), int(day))
        return begintime


def get_days(nowtime, stringtime):
    if isinstance(nowtime, date):
        pass
    else:
        nowtime = convertstringtodate(nowtime)
    if isinstance(stringtime, date):
        pass
    else:
        stringtime = convertstringtodate(stringtime)

    result = nowtime - stringtime
    return result.days


def get_special_value(value_list):
    # 返回一个list中的特殊值
    for value in value_list:
        return time.ctime(value)


if __name__ == '__main__':
    # path = '/Users/ambition/Downloads'
    # for x in get_all_file('I:/bishexiangguan/test', ['I:/bishexiangguan/test/safe'], ['mp3', 'mp4', 'avi']):
    # for x in get_all_file('I:\\bishexiangguan\\test', ['I:\\bishexiangguan\\test\\safe'], ['mp3']):
        # get_time_between(x)
        # print(x)
    timeStamp = get_mtime('I:\\JDK8\\release')
    dateArray = datetime.utcfromtimestamp(timeStamp)
    otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
    print(otherStyleTime)