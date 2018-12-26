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
def set_map(m, n, fill=None):
    mat = []
    for i in range(m):
        mat.append([fill] * n)
    return mat

INF = 9999

def show(dis, path):
    m = len(path)
    for i in range(m):
        for j in range(i + 1, m):
            print("%d->%d: " % (i, j), end="")
            k = path[i][j]
            print(i, end=" ")
            while k != j:
                print(k, end=" ")
                k = path[k][j]

            print(j)
            print(dis[i][j])

def floyd(graph):
    m = len(graph)

    dis = set_map(m, m, fill=0)
    path = set_map(m, m, fill=0)
    for i in range(m):
        for j in range(m):
            dis[i][j] = graph[i][j]
            path[i][j] = j

    for k in range(m):
        for i in range(m):
            for j in range(m):
                if dis[i][k] + dis[k][j] < dis[i][j]:
                    dis[i][j] = dis[i][k] + dis[k][j]
                    path[i][j] = path[i][k]

    return dis, path

if __name__ == '__main__':
    graph = set_map(6, 6, fill=INF)
    graph[0][1] = 1
    graph[0][2] = 2
    graph[1][2] = 1
    graph[1][5] = 7
    graph[2][3] = 1
    graph[2][4] = 2
    graph[3][5] = 3
    graph[4][5] = 6

    dis, path = floyd(graph)
    show(dis, path)