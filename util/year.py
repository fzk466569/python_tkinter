#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/3 20:45


def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False


def get_days(start_year, end_year):
    days = 0
    for year in range(start_year, end_year):
        days += 365 if not is_leap_year(year) else 366
    return days

if __name__ == '__main__':
    print(get_days(2000, 2003))
