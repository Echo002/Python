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
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num1, num2 = int(a,2), int(b,2)
        result = bin(num1 + num2)
        result = result.lstrip('0b')
        if result == '':
            return "0"
        return result

# 以下是测试代码：
a = "11"
b = "1"
s = Solution()
result = s.addBinary(a,b)
print(result)