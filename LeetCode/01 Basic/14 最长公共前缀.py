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
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        count = 0
        min = 0
        for i in strs:
            if i == '' :
                return ''
        if strs == []:
            return ''
        for i in range(0,len(strs)):
            if len(strs[min])>len(strs[i]):
                min = i
        for i in range(0, len(strs[min])):                  # 最多只能比较最短单词的长度次数
            for j in range(0 , len(strs)):                  # 每一轮和其他的单词比较
                if strs[0][i] != strs[j][i]:
                    if count == 0:
                        return ''
                    else:
                        return strs[min][:count]
            count += 1
        return strs[min][:count]

# 以下是测试代码：
s = []
s1 = Solution()
s = s1.longestCommonPrefix(s)
print(s)