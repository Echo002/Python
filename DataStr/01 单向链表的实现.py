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

'''
is_empty()          链表是否为空
length()            链表长度
travel()            遍历链表
add(item)           从头部添加元素
append(item)        从尾部添加元素
insert(pos,item)    在指定位置添加元素
remove(item)        移除元素
search(item)        查找节点是否存在
'''

class Node(object):
    #node
    def __init__(self,elem):
        self.elem = elem
        self.next = None
    pass

class SingleLinkList(object):
    #list
    def __init__(self):
        self._head = None

    def is_empty(self):
        pass

    def length(self):
        pass

    def travel(self):
        pass

    def add(self, item):
        pass

    def append(self, item):
        pass

    def insert(self, pos, item):
        pass

    def remove(self, item):
        pass

    def search(self, item):
        pass



node = Node(100)

single_List = SingleLinkList()