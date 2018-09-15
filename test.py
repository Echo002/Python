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
def text1(a):
    if (a % 2 == 0):
        a = a / 2
    elif (a % 2 != 0):
        a = (3 * a + 1) / 2
    return a


n = input()
m = input().split()
for i in range(len(m)):
    m[i] = int(m[i])
result = m[0:len(m)]
for i in m:
    a = i
    while a > 1:
        a = text1(a)
        if (a in result):
            result.remove(a)
result.sort(reverse=True)
if (len(result) == 1):
    print(result[0], end='')
else:
    for i in range(len(result) - 1):
        print(result[i], end=' ')
    print(result[i + 1], end='')