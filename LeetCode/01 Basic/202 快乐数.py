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

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        deal = n
        sum = 0
        sets = []
        setb = []
        while True:
            while deal != 0:
                num = deal % 10
                sets.append(num)
                sum += num * num
                deal /= 10
                deal = int(deal)
            if sum == 1:
                return True
            else:
                if sets in setb:
                    return False
                deal = sum
                sum = 0
                sorted(sets)
                setb.append(sets)
                sets = []

# 以下是测试代码：
x = 2
s = Solution()
result = s.isHappy(x)
print(result)