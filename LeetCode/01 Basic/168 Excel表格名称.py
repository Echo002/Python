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
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        assert n > 0
        n = n - 1
        result = []
        result_str = ''
        if n == 0:
            return 'A'
        while n > 0:
            temp = n % 26
            n = (n // 26) - 1
            result.append(temp)
        if n >= 0:
            result.append(n)
        result.reverse()
        for item in result:
            result_str += chr(ord('A') + item)
        return result_str

# 以下是测试代码：
x = 701
s = Solution()
result = s.convertToTitle(x)
print(result)
