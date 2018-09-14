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

import re
count = int(input())
part = []
result = []
for i in range(count):
    stock = input()
    if(re.match(r"A*PA+TA*" , stock)):
        part = re.split(r'[P|T]' , stock)
        part_a = part[0]
        part_b = part[1]
        part_c = part[2]
        if(len(part_c) == len(part_a) * len(part_b)):
            result.append('YES')
        else:
            result.append('NO')
    else:
        result.append('NO')
for i in range(0,len(result)):
    print(result[i])
