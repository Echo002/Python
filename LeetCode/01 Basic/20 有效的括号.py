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
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {'(':')' , '[':']' , '{':'}'}
        stack = []                          # 使用栈
        for i in s:
            if i in dic.keys():
                stack.append(i)
            elif i in dic.values():
                if len(stack) == 0 or dic.get(stack[-1]) != i:
                    return False
                else:
                    stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False

# 以下是测试代码：
s = "()"
s1 = Solution()
s = s1.isValid(s)
print(s)