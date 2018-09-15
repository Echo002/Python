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
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        data = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        deal = list(s)
        sum = 0
        for i in range(0 , len(s)):
            if (s[i] == 'I'):
                if(s[i+1] == 'V'):
                    sum += 4
                    i+=2
                    continue
                elif(s[i+1] == 'X'):
                    sum += 9
                    i+=2
                    continue
            if (s[i] == 'X'):
                if(s[i+1] == 'L'):
                    sum += 40
                    i+=2
                    continue
                elif(s[i+1] == 'C'):
                    sum += 90
                    i+=2
                    continue
            if (s[i] == 'C'):
                if(s[i+1] == 'D'):
                    sum += 400
                    i+=2
                    continue
                elif(s[i+1] == 'M'):
                    sum += 900
                    i+=2
                    continue
            sum = sum + data[s[i]]
        return sum


# 以下是测试代码：
s = "LVIII"
s1 = Solution()
s = s1.romanToInt(s)
print(s)