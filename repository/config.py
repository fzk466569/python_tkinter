#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/2 10:12

MYSQL_HOST = '127.0.0.1'
MYSQL_USER = 'root'
MYSQL_PASS = 'root'
MYSQL_CONN = 'mysql://{0}:{1}@{2}/test?charset=utf8'.format(MYSQL_USER, MYSQL_PASS, MYSQL_HOST)
