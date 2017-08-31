#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/3 15:32

import os
import time
from api.file_api import get_all_file


class Detect(object):
    # 返回一个目录下的新生成文件的绝对路径
    def __init__(self):
        self.flag = True

    def detector(self, path, sec):
        if not path.endswith('\\' or '/'):
            path = path + '/'
        origin = set(x for x in get_all_file(path))
        time.sleep(sec)
        final = set(x for x in get_all_file(path))
        # origin = set([_f[2] for _f in os.walk(path)][0])
        # time.sleep(sec)
        # final = set([_f[2] for _f in os.walk(path)][0])
        if final.difference(origin):
            self.flag = False
            return list(final.difference(origin))[0]

if __name__ == '__main__':
    d = Detect()
    while d.flag:
        file_name = d.detector('I:\\bishe\\test', 1)
        if file_name:
            print(file_name)
    print('end')
