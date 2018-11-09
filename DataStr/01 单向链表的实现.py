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
        self.__head = None

    def is_empty(self):
        return self.__head == None

    def length(self):
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next

    def add(self, item):
        # 头插法
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        # 尾插法
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        #指定位置添加元素 pos从0开始索引 pos是添加完成后的位置
        node = Node(item)
        pre = self.__head
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            for i in range(pos - 1):
                pre = pre.next
            # 循环结束后，pre指向pos-1的位置
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        pass

    def search(self, item):
        pass

if __name__ == "__main__":
    single_List = SingleLinkList()
    print(single_List.is_empty())
    print(single_List.length())

    single_List.append(1)
    print(single_List.is_empty())
    print(single_List.length())

    single_List.append(2)
    single_List.append(3)
    single_List.append(4)
    single_List.append(5)
    single_List.append(6)
    single_List.travel()
    print('\n')

    single_List.insert(-1, 9) #98123456
    single_List.insert(2, 100)#981 100 123456
    single_List.insert(10, 200)# 981 100 23456 200

    single_List.travel()