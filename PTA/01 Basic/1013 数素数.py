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
count = 0
start, stop = int(lst[0]), int(lst[1])
line_count = 1
num = 1
while count < stop:
    num += 1
    if prime(num):
        count += 1
        if count >= start:
            if line_count == 10 or count == stop:
                print(num)
                line_count = 1
            else:
                print(num, end=" ")
                line_count += 1