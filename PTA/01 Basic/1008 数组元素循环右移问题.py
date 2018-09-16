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
str1 = input()
str2 = input()
deal_1 = str1.split()
deal_e = str2.split()
deal_2 = []
str = ''
num = int(deal_1[0])
step = int(deal_1[1])
for i in deal_e:
    deal_2.append(int(i))
for i in range(step):
    temp = deal_2[-1]
    for j in range(0,num-1):
        deal_2[num - 1 - j] = deal_2[num -2 -j]
    deal_2[0] = temp
#print(deal_2)
result = [str(x) for x in deal_2]
print(result)
