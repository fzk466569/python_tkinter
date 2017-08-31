#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/3 09:55

import re
from repository.common import DbCommon


def get_file_content(file_name):
    file_name = file_name.replace('//', '/')
    with open(file_name, 'r') as f:
        try:
            return f.read()
        except:
            return ''

if __name__ == '__main__':
    # re_string = 'my favorite team is edg'
    # file_name = '/Users/ambition/test_pro/1.txt'
    # print(get_file_content(file_name))
    # print(len(get_file_content(file_name)))
    # # re_tag = re.compile(r'name')
    # # print(re_tag.match(get_file_content(file_name)).group(0), '1111111')
    #
    # dbc = DbCommon()
    # re_t = '|'.join(dbc.get_all_data('test1', 'value'))
    # re_tag = re.compile(r'(' + re_t + ')')
    # print(re_tag)
    # print(re_tag.search(re_string))
    print(get_file_content('I:/bishe/web/I:/bishe/web/plugin/web.txt'))
