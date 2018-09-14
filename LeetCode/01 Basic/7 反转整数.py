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
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sum = 0
        if(x >= 0):
            while(x != 0):
                r = x % 10
                sum = sum * 10 + r
                x = x // 10
                if(sum > 2**31-1):
                    return 0
            return sum
        else:
            x = -x
            while (x != 0):
                r = x % 10
                sum = sum * 10 + r
                x = x // 10
                if (sum > 2 ** 31):
                    return 0
            return -sum
# 以下是测试代码
x = 1534236469

s1 = Solution()
s = s1.reverse(x)
print(s)