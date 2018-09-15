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
source = input()
deal = []
data = []
result = ''
source = source.split(" ")
for i in range(0 , num):
    deal.append(int(source[i]))

for j in deal:
    while(j != 1):
        if(j % 2 == 0):
            j = j / 2
        else:
            j = (3 * j + 1) / 2
        if int(j) not in data:
            data.append(int(j))
        continue
for k in deal:
    if(k not in data):
        result = result + ' ' + str(k)
result = result.strip()
print(result)