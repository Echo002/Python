#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Author:xugao
#         ┌─┐       ┌─┐
#      ┌──┘ ┴───────┘ ┴──┐
#      │                 │
#      │                 │
#      │    ＞  　　＜    │
#      │                 │
#      │  ....　⌒　....　│
#      │                 │
#      └───┐         ┌───┘
#          │         │
#          │         │
#          │         │
#          │         └──────────────┐
#          │                        │
#          │                        ├─┐
#          │                        ┌─┘
#          │                        │
#          └─┐  ┐  ┌───────┬──┐  ┌──┘
#            │ ─┤ ─┤       │ ─┤ ─┤
#            └──┴──┘       └──┴──┘
#                神兽保佑
#                BUG是不可能有BUG的!
import pymysql
import codecs
import csv

def red_mysql_to_csv(filename):
    with codecs.open(filename = filename, mode = 'a+',encoding = 'utf-8')as f:
        write = csv.writer(f,dialect = 'excel')
        write.writerow(['车辆标识','触发事件','运营状态','GPS时间','GPS经度','GPS纬度','GPS速度','GPS方位','GPS状态'])
        db = pymysql.connect("localhost", "root", "root", "Demo")
        sql =r"select GPS经度,GPS纬度 from gps1 where 触发事件 = 2 and 运营状态 = 2 and GPS速度 > 0 and GPS方位 > 300 and 车辆标识=162411;"
        cursor = db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        for res in results:
            print(res)
            write.writerow(res)
red_mysql_to_csv('result.csv')
