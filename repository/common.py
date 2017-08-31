#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/2 10:38

import dataset

from repository.config import MYSQL_CONN


class DbCommon(object):
    def __init__(self):
        self.conn = MYSQL_CONN
        self.db = dataset.connect(self.conn)

    def get_tables(self):
        return self.db.tables

    def get_table_structure(self, table):
        # 返回数据库字段名
        return self.db[table].columns

    def get_all_data_column(self, table, column):
        # 返回一个表某个字段所有的值
        values = []
        for value in self.db[table].all():
            # print('value.get(): ', [x for x in value.values()])
            values.append(value.get(column).replace('(', '\(').replace('[', '\[').replace('?', '\?').replace('$', '\$'))
            # yield x
        return values

    def get_all_data(self, table):
        for value in self.db[table].all():
            yield [x for x in value.values()]

    def set_data(self, table, data):
        return self.db[table].insert(data)

    def update_data(self, table, data, origin):
        return self.db[table].update(data, [origin])


if __name__ == '__main__':
    dbc = DbCommon()
    table = 'test'
    # table = 'settings'
    # dbc.set_data(table, {'value': 'fff'})
    for x in dbc.get_all_data(table):
        print(x)
        # print(len(x))
    # print(dbc.update_data(table=table, data=dict(user='fzk', phone='123', email='111'), origin='user'))
    # dbc.get_all_data(table, 'phone')
