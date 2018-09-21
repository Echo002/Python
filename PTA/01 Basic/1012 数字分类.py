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
str = input().split()
deal = []
ver = 1
p_4 = []
p_3 = []
result = [0]*5
for i in str:
    deal.append(int(i))
for j in deal:
    judge = j % 5
    if judge == 0:
        if j % 2 == 0:
            result[0] += j
            continue
        elif judge == 1:
            result[1] = result[1] + ver * j
            ver = -ver
            continue
        elif judge == 2:
            result[2] += 1
            continue
        elif judge == 3:
            p_3.append(j)
            continue
            # 求平均数
        elif judge ==4:
            p_4.append(j)
            continue
result[3] == result[3] / len()


