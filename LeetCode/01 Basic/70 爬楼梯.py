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
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(0, n+1):
            j = n - 2*i
            if j < 0:
                break
            num = i + j
            count += int(math.factorial(num) / (math.factorial(j) * math.factorial(num-j)))
        return count

# 以下是测试代码：
x = 3
s = Solution()
result = s.climbStairs(x)
print(result)