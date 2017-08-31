#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/3 10:48

import re

from file_pro.file_content import get_file_content
from file_pro.common import get_all_file, get_time_between, get_mtime
from repository.common import DbCommon
from util.listen import Detect


def target_match_path(path, trust_path=[], trust_file_type=[], scripts=[]):
    print('target_match_path', path, trust_path, trust_file_type, scripts)
    file_id = 0
    for file_name in get_all_file(path, trust_path, trust_file_type):
        file_id += 1
        file_name = format_filename(file_name)
        print('正在检测文件【特征码】： ', file_name)
        file_content = get_file_content(file_name)
        dbc = DbCommon()
        re_t = ''
        for script in scripts:
            t = '|'.join(dbc.get_all_data_column(script, 'value'))
            re_t += t + '|'
        # 去掉正则的最后一个 |
        re_t = re_t[:-1]
        print(re_t)
        re_tag = re.compile('(' + re_t + ')')
        # retag = 'fzkf|3|<? php eval\($_POST[|<?php eval\($_POST[|<?php system\($_REQUEST[|<?php eval\($_POST[|<?php @eval\($_POST['
        # re_tag = re.compile(retag)
        # print('re.compile(retag): ', re.compile(retag))
        print('type(file_content): ', type(file_content))
        try:
            file_content = file_content.decode('utf-8')
        except:
            pass
        print(file_name)
        print('type(file_content): ', type(file_content))
        if re_tag.search(file_content):
        #     print('flag: ', flag)
        #     flag = True if  else False
        #
        # except TypeError:
        #     flag = False
        #     # flag = True if re_tag.search(file_content.decode('utf-8')) else False
        # if flag:
            status = 'unsafe'
            try:
                expand = re_tag.search(file_content).group(0)
            except TypeError:
                pass
                # expand = re_tag.search(file_content.decode('utf-8')).group(0)
            yield file_id, file_name, get_mtime(file_name), status, expand
            # yield 'unsafe'
        else:
            status = 'safe'
            # yield 'safe'
            yield file_id, file_name, get_mtime(file_name), status, ''


def target_match_file(file_name, scripts=[]):
    file_name = format_filename(file_name)
    file_content = get_file_content(file_name)
    dbc = DbCommon()
    re_t = ''
    for script in scripts:
        t = '|'.join(dbc.get_all_data_column(script, 'value'))
        re_t += t + '|'
    re_t = re_t[:-1]
    re_tag = re.compile(re_t)
    print(re_t, re_tag)
    status = '安全'
    if re_tag.search(file_content):
        status = '危险'
        # print(re_tag.search(file_content).group(0))
        return [status, re_tag.search(file_content).group(0)]
    else:
        # print('safe')
        return [status, '']


def format_filename(file_name=''):
    # print('format_filename', file_name)
    if '\\' in file_name:
        file_name = file_name.replace('\\', '/')
    return file_name


def cm_match(path):
    for file_name in get_all_file(path):
        print('正在检测文件【时间差】： ', file_name)
        days_diff = get_time_between(file_name)
        yield file_name, days_diff


def cm_test(path):
    day_dict = {}
    # target_match('/Users/ambition/test_pro')
    for file_name, day in cm_match(path):
        day_dict[file_name] = day

    return day_dict


# 监测某目录下的文件变化
def detect(path, sec):
    dt = Detect()
    while dt.flag:
        file_name = dt.detector(path, sec)
        if file_name:
            yield file_name
            dt.flag = True


if __name__ == '__main__':
    # for x in detect('C:/Users/12054/Documents/Adobe/dynamiclinkmediaserver/6.0'):
    #     print(x)
    # detect_test('/Users/ambition/test_pro', 1)
    for x in get_all_file('I:/tomcat/apache-tomcat-7.0.68/webapps/neusoftwebshop', ['I:/bishexiangguan/test/safe'], ['mp3', 'mp4', 'avi']):
    # for x in get_all_file('I:\\bishexiangguan\\test', ['I:\\bishexiangguan\\test\\safe'], ['mp3']):
    #     get_time_between(x)
        print(x)
    # filename = 'I:/bishexiangguan/test/safe/unsafe\\1111.txt'
    # filename = format_filename(filename)
    # print(filename)
    # print(target_match_file(filename, scripts=['asp', 'php']))
