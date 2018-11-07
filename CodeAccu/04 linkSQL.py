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

# 使用 cursor() 方法创建一个游标对象 cursor

# with open('users.csv','a+') as fw:
#     for i in range(len(data)):
#         fw.write("".join(tuple(data[i])))

def red_mysql_to_csv(filename):
    with codecs.open(filename=filename,mode='w',encoding='utf-8')as f:
        write = csv.writer(f,dialect='excel')
        write.writerow(['车辆标识','触发事件','运营状态','GPS时间','GPS经度','GPS纬度','GPS速度','GPS方位','GPS状态'])
        db = pymysql.connect("localhost", "root", "root", "Demo")
        cursor = db.cursor()
        sql =r"select * from gps1 where 触发事件 =1 and GPS状态=1 and GPS方位>300 and GPS速度 > 40;"
        cursor = db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        for res in results:
            print(res)
            write.writerow(res)

red_mysql_to_csv('result.csv')
