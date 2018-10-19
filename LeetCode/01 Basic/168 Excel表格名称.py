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
        dic = {1:'A', 2:'B', 3:'C',4:'D',5:'E',6:'E',7:'G',8:'H',
               9: 'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',
               17: 'Q',18:'R',19:'S',20:'T',21:'U',22:'v',23:'w',24:'x',
               25: 'Y',26:'Z',}
        count = 0
        result = []
        while(n >= 0):
            r = n % 26
            result.insert(0,dic[r])
            n -= r * pow(26, count)
        return result

# 以下是测试代码：
x = 45
s = Solution()
result = s.convertToTitle(x)
print(result)
