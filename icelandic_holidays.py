#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2013 Sölvi Páll Ásgeirsson
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""
Functions for determining if a datetime object represents an Icelandic
holiday.

Public API:
is_holiday(dt)     -> True or False
is_businessday(dt) -> True or False
is_bankday(dt)     -> True or False

---------------------------------------------------------------------
As of 2013, these are the public holidays:

- January 1st, new years day (Nýársdagur)
- Holy Thursday, the last thursday before easter (Skírdagur)
- Good friday, the friday preceding easter (föstudagurinn langi)
- Easter sunday (páskadagur)
- Easter monday (annar í páskum)
- First day of summer, the first thursday after 18th of April (Sumardagurinn fyrsti)
- May 1st, labour day (verkalýðsdagurinn)
- Ascension of Jesus, 40 days after Easter (Uppstigningardagur)
- Pentecost, 49 days after Easter (hvítasunnudagur)
- Whit monday, monday after Pentecost (annar í hvítasunnu)
- June 17th., National holiday
- Merchant holiday / First monday of august (frídagur verslunarmanna)
- December 24th from 13:00 / Christmas eve (aðfangadagur)
- December 25th / Christmas day (jóladagur)
- December 26th / Second day of Christmas (annar í jólum)
- December 31st from 13:00 / New years eve (gamlársdagur)

references:
- http://visindavefur.hi.is/svar.asp?id=1692
- http://www.lanamal.is/fagfjarfestar/fridagar
- http://www.smart.net/~mmontes/nature1876.html

"""

from datetime import datetime, timedelta

__holiday_funs = []

def __holiday_fun(f):
    if f not in __holiday_funs:
        __holiday_funs.append(f)
    return f

def get_easter_sunday(year):
    """ Get easter sunday for year.  Works for years after 1583.
    See http://www.smart.net/~mmontes/nature1876.html """
    if year < 1583:
        raise ValueError("year must be larger than 1583")
    
    a = year % 19
    b = int(year / 100)
    c = int(year % 100)
    d = int(b / 4)
    e = b % 4
    f = int((b + 8) / 25)
    g = int((b - f + 1) / 3)
    h = (19 * a + b - d - g + 15) % 30
    i = int(c / 4)
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = int((a + 11 * h + 22 * l) / 451)
    month = int((h + l - 7 * m + 114) / 31)
    day = ((h + l - 7 * m + 114) % 31) + 1

    return datetime(year, month, day)

@__holiday_fun
def __january_1st(dt):
    return dt.month == 1 and dt.day == 1

@__holiday_fun
def __holy_thursday(dt):
    return dt.date() == (get_easter_sunday(dt.year) - timedelta(days=3)).date()

@__holiday_fun
def __good_friday(dt):
    return dt.date() == (get_easter_sunday(dt.year) - timedelta(days=2)).date()

@__holiday_fun
def __easter_sunday(dt):
    return get_easter_sunday(dt.year).date() == dt.date()

@__holiday_fun
def __easter_monday(dt):
    return get_easter_sunday(dt.year).date() + timedelta(days=1) == dt.date()

@__holiday_fun
def __first_day_of_summer(dt):
    if dt.month != 4:
        return False
    
    d = datetime(dt.year, 4, 19)
    while True:
        if d.isoweekday() == 4:
            break
        d = d + timedelta(days=1)
    return dt.date() == d.date()

@__holiday_fun
def __may_1st(dt):
    return dt.month == 5 and dt.day == 1

@__holiday_fun
def __ascension_of_jesus(dt):
    return dt.date() == (get_easter_sunday(dt.year) + timedelta(39)).date()

@__holiday_fun
def __pentecost(dt):
    return dt.date() == (get_easter_sunday(dt.year) + timedelta(49)).date()

@__holiday_fun
def __whit_monday(dt):
    return dt.date() == (get_easter_sunday(dt.year) + timedelta(50)).date()

@__holiday_fun
def __june_17th(dt):
    return dt.month == 6 and dt.day == 17

@__holiday_fun
def __merchant_holiday(dt):
    if dt.month != 8:
        return False

    d = datetime(dt.year, 8, 1)
    while True:
        if d.isoweekday() == 1:
            break
        d = d + timedelta(days=1)
    return dt.date() == d.date()

@__holiday_fun
def __christmas_eve(dt):
    return dt.month == 12 and dt.day == 24

@__holiday_fun
def __christmast_day(dt):
    return dt.month == 12 and dt.day == 25

@__holiday_fun
def __second_day_of_christmas(dt):
    return dt.month == 12 and dt.day == 26

@__holiday_fun
def __new_years_eve(dt):
    return dt.month == 12 and dt.day == 31

def is_weekday(dt):
    weekday = datetime.isoweekday(dt)
    return 1 <= weekday <= 5

def is_holiday(dt):
    """ Accepts a datetime object, returns True if it is a holiday, False otherwise. """
    for fun in __holiday_funs:
        if fun(dt):
            return True
    return False

def is_businessday(dt):
    """ Accepts a datetime object, returns True if it is a business day, False otherwise. """
    return is_weekday(dt) and not is_holiday(dt)

def is_bankday(dt):
    """ Accepts a datetime object, returns True if it represents a bank day. """
    return is_businessday(dt) or (__new_years_eve(dt) and is_weekday(dt))
