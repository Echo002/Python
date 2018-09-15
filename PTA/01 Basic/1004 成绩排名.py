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

num = int(input())
list = []
No = []
Name = []
Grade = []
max = 0
min = 0
for i in range(0 , num):
    r = input()
    list.append(r)
for i in range(0 , num):
    r = list[i].split(" ")
    Name.append(r[0])
    No.append(r[1])
    Grade.append(int(r[2]))
for i in range(0 , num):
    if(Grade[max] < Grade[i]):
        max = i
    if(Grade[min] > Grade[i]):
        min = i
print(Name[max] + " " + No[max])
print(Name[min] + " " + No[min])