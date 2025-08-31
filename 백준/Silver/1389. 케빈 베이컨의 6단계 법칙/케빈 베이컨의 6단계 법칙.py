import sys

n,m  = map(int,sys.stdin.readline().rstrip().split())

all_set = [[int(1e9)]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    all_set[i][i] = 0

for _ in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())

    all_set[x][y] = 1
    all_set[y][x] = 1


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            all_set[i][j] = min(all_set[i][j], all_set[i][k] + all_set[k][j])

bac = {}

for i in range(1,n+1):
    cnt = 0
    for j in range(1, n+1):
        cnt += all_set[i][j]

    bac[i] = cnt

minv = min(bac.values())

for k,v in bac.items():
    if (v == minv):
        result = k
        break

print(result)