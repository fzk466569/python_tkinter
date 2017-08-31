#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/3 15:31
import hashlib


def md5(str):
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()

if __name__ == '__main__':
    print(md5('111'.encode('utf-8')))