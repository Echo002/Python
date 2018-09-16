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
import re
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        data = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        #deal = list(s)
        sum = 0
        deal = re.findall('IV|IX|XL|XC|CD|CM',s)
        for i in deal:
            sum += data[i]
        deal = re.split('IV|IX|XL|XC|CD|CM',s)
        for i in deal:
            e_out = list(i)
            for e_in in e_out:
                sum += data[e_in]
        return sum


# 以下是测试代码：
s = "MCMXCIV"
s1 = Solution()
s = s1.romanToInt(s)
print(s)