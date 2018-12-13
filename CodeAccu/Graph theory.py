INF=9999

G={ 1: {1:INF,2:1,3:2,4:INF,5:INF,6:INF},
    2: {1:INF,2:INF,3:1,4:INF,5:INF,6:7},
    3: {1:INF,2:INF,3:INF,4:1,5:2,6:INF},
    4: {1:INF,2:INF,3:INF,4:INF,5:INF,6:3},
    5: {1:INF, 2:INF,3:INF,4:INF,5:INF,6:6},
    6: {1:INF,2:INF,3:INF,4:INF,5:INF,6:INF},
}

for k in G.keys():
    for i in G.keys():
        for j in G[i].keys():
            if G[i][j] > G[i][k] + G[k][j]:
                G[i][j] = G[i][k] + G[k][j]
for i in G.keys():
    print(G[i].values())