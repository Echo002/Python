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

dataSet = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(dataSet[0]) - 1):
    featList = [example[i] for example in dataSet]
    print(featList)

'''
variable = [out_exp_res for out_exp in input_list if out_exp == 2]
  out_exp_res:　　列表生成元素表达式，可以是有返回值的函数。
  for out_exp in input_list：　　迭代input_list将out_exp传入out_exp_res表达式中。
  if out_exp == 2：　　根据条件过滤哪些值可以。
'''