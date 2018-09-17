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
num = []
deal = input().split()
for i in deal:
    num.append(int(i))
result = []
if len(num) == 2 and num[1] == 0:
    result.extend(['0', '0'])
else:
    for i in range(0, len(num) - 1, 2):
        x = num[i] * num[i+1]
        z = num[i+1] - 1
        if z < 0:
            # result.extend(['0', '0'])
            continue
        if x == 0:
            result.extend(['0', '0'])
            continue
        result.append(x)
        result.append(z)
for i in range(len(result)):
    result[i] = str(result[i])
print(" ".join(result))
