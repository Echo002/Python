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
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, mid, right = 0, x//2, x
        if x == 0 or x == 1:
            return x
        while True:
            if mid * mid == x:
                return mid
            if mid * mid > x:
                left = 0
                right = mid
            else:
                left = mid
            mid = (left+right)//2
            if mid*mid <= x and (mid+1)*(mid+1) > x:
                return mid

# 主要是二分法的应用！

# 以下是测试代码：
x = 4
s = Solution()
result = s.mySqrt(x)
print(result)