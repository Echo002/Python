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
import math
def prime(num):
    if num % 3 == 0 and num != 3 or num % 2 == 0 and num != 2:
        return False
    for i in range(5, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

lst = input().split()
con = 0
start, stop = int(lst[0]), int(lst[1])
con2 = 1
num = 1
while con < stop:
    num += 1
    if prime(num):
        con += 1
        if con >= start:
            if con2 == 10 or con == stop:
                print(num)
                con2 = 1
            else:
                print(num, end=" ")
                con2 += 1