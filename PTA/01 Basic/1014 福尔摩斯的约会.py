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
dic_D = {'A':'MON' , 'B':'TUE', 'C':'WED' , 'D':'THU' , 'E':'FRI' , 'F':'SAT' , 'G':'SUN'}
dic_H = {'0':'00' , '1':'01' , '2':'02' , '3':'03' , '4':'04' , '5':'05' , '6':'06' , '7':'07' , '8':'08' , '9':'09' ,
         'A': '10' , 'B': '11' , 'C': '12' , 'D': '13' , 'E': '14' , 'F': '15' , 'G': '16' , 'H': '17' ,
         'I': '18' , 'J': '19' , 'K': '20' , 'L': '21' , 'M': '22' , 'N': '23'}
data = []
k = 0
for i in range(4):
    data.append(input())
min_1 = min(len(data[0]) , len(data[1]))
min_2 = min(len(data[2]) , len(data[3]))
for i in range(min_1):
    if data[0][i] == data[1][i] and "A"<=data[0][i]<="G":
        print(dic_D.get(data[0][i]) , end=' ')
        k = i
        break

for j in range(k+1 , min_1):
    if data[0][j] == data[1][j] and ("A"<=data[0][j]<="N" or "0"<=data[0][j]<="9"):
        print(dic_H.get(data[0][j]) , end=':')
        break

for i in range(min_2):
    if data[2][i] == data[3][i] and ("A"<=data[2][i]<="Z" or "a"<=data[2][i]<="z"):
        if i < 10:
            print('0' + str(i) , end='')
            break
        else:
            print(str(i), end='')
            break