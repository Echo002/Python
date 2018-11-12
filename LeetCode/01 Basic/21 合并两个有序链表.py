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

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def travel(self):
        cur = self
        while cur != None:
            print(cur.val, end=" ")
            cur = cur.next
        print("\n", end='')

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        first = res
        cur1 = l1
        cur2 = l2
        while cur1 != None or cur2 != None:
            if cur1 == None:
                res.next = cur2
                return first.next
            if cur2 == None:
                res.next = cur1
                return first.next
            if cur1.val > cur2.val:
                res.next = cur2
                cur2 = cur2.next
            else:
                res.next = cur1
                cur1 = cur1.next
            res = res.next

# 以下是测试代码：


l1 = ListNode(2)
n1 = ListNode(3)
n2 = ListNode(4)
n3 = ListNode(9)
l1.next = n1
n1.next = n2
n2.next = n3

l2 = ListNode(3)
m1 = ListNode(5)
m2 = ListNode(7)
m3 = ListNode(8)
l2.next = m1
m1.next = m2
m2.next = m3

s1 = Solution()
s = s1.mergeTwoLists(l1, l2)
print(l1,l2)
print(s.travel())
