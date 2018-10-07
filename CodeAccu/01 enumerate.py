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
# 01.将数组中的奇数进行排序
# 将一个数组里面的奇数的数进行重新排列,0不是奇数
# 例子:sort_array([5,3,2,8,1,4])==[1,3,2,8,5,4]

arr = [5,3,2,8,1,4]
def sort_arr(arr):
    odd_index = [ind for (ind,val) in enumerate(arr) if val % 2 == 1]
    sorted_odd = sorted([odd for odd in arr if odd % 2 ==1])
    j = 0
    for i in odd_index:
        arr[i] = sorted_odd[j]
        j += 1
    return arr if arr != [] else[]

print(sort_arr(arr))

'''
PS:
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。

普通的for循环：
>>>i = 0
>>> seq = ['one', 'two', 'three']
>>> for element in seq:
...     print i, seq[i]
...     i +=1
... 
0 one
1 two
2 three

for循环使用enumerate：
>>>seq = ['one', 'two', 'three']
>>> for i, element in enumerate(seq):
...     print i, element
... 
0 one
1 two
2 three

在创建列表中 先写for再写if（参考32、33行）
'''