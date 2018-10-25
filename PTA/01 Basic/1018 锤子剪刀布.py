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

num = int(input())
f1_win, f2_win, tie, f1_win_count, f2_win_count, f1_win_log, f2_win_log, = 0, 0, 0, 0, 0, {'B':0, 'C':0, 'J':0}, {'B':0, 'C':0, 'J':0}
for _ in range(num):
    str = input().split()
    if str[0] == str[1]:
        tie += 1
    if (str[0] == 'J' and str[1] == 'B') or (str[0] == 'B' and str[1] == 'C') or (str[0] == 'C' and str[1] == 'J'):
        f1_win_count += 1
        f1_win_log[str[0]] += 1
    if (str[1] == 'J' and str[0] == 'B') or (str[1] == 'B' and str[0] == 'C') or (str[1] == 'C' and str[0] == 'J'):
        f2_win_count += 1
        f2_win_log[str[1]] += 1
if f1_win_log['B'] >= f1_win_log['C'] and f1_win_log['B'] >= f1_win_log['J']:
    result1 = 'B'
elif f1_win_log['C'] > f1_win_log['B'] and f1_win_log['C'] >= f1_win_log['J']:
    result1 = 'C'
elif f1_win_log['J'] > f1_win_log['B'] and f1_win_log['J'] > f1_win_log['C']:
    result1 = 'J'

if f2_win_log['B'] >= f2_win_log['C'] and f2_win_log['B'] >= f2_win_log['J']:
    result2 = 'B'
elif f2_win_log['C'] > f2_win_log['B'] and f2_win_log['C'] >= f2_win_log['J']:
    result2 = 'C'
elif f2_win_log['J'] > f2_win_log['B'] and f2_win_log['J'] > f2_win_log['C']:
    result2 = 'J'

print('%d %d %d' %(f1_win_count, tie, f2_win_count))
print('%d %d %d' %(f2_win_count, tie, f1_win_count))
print('%s %s' %(result1, result2))