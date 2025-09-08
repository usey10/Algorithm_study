import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int,input().rstrip().split())

maps = [[0]*m for _ in range(n)]
lengths = [[-1]*m for _ in range(n)]
deq = deque()

for i in range(n):
    tmp = list(map(int, input().rstrip().split()))

    for j in range(m):
        maps[i][j] = tmp[j]

        if maps[i][j] == 2:
            deq.append([i,j])
            lengths[i][j] = 0
        elif maps[i][j] == 0:
            lengths[i][j] = 0


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]



while deq:
    k = deq.popleft()
    for i in range(len(dx)):
        new_x = k[0] + dx[i]
        new_y = k[1] + dy[i]

        if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
            continue
        elif lengths[new_x][new_y] == -1:
            lengths[new_x][new_y] = lengths[k[0]][k[1]] + 1
            deq.append([new_x, new_y])
            
for i in range(n):
    print(" ".join(str(j) for j in lengths[i]))