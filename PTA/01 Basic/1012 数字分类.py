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
from decimal import Decimal as D
n=input().split()
m=int(n[0])
a=list(map(int,n[1:]))
A1,A2,A3,A4,A5=0,0,0,0,0
k,j,flag=0,0,0
for i in range(m):
    if a[i]%10==0:
        A1+=a[i]
    elif a[i]%5==1:
        flag=1
        A2+=a[i]*(-1)**k
        k+=1
    elif a[i]%5==2:
        A3+=1
    elif a[i]%5==3:
        A4+=a[i]
        j+=1
    elif a[i]%5==4:
        if a[i]>A5:
            A5=a[i]
if A1==0:
    A1="N"
if flag==0:
    A2="N"
if A3==0:
    A3="N"
if A4==0:
    A4="N"
else:
    A4="{:.1f}".format(D(str(A4/j)))
if A5==0:
    A5="N"
print(A1,A2,A3,A4,A5)
