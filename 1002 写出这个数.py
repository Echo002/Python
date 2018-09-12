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
dic = ['ling','yi','er','san','si','wu','liu','qi','ba','jiu']
n = int(input())
sum = 0
list = []
while(n != 0):
    r = n % 10
    sum = sum + r
    n = int(n // 10)
while(sum != 0):
    r = dic[sum % 10]
    list.append(r)
    sum = int(sum // 10)
list.reverse()
str = ''
for i in list:
    str = str + ' '+ i
result = str.strip()
print(result)