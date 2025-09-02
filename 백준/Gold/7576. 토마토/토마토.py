import sys
from collections import deque

input = sys.stdin.readline
M, N = map(int, input().rstrip().split())

tomato = [[] for _ in range(N)]
q = deque()

for i in range(N):
    t = list(map(int, input().rstrip().split()))
    tomato[i] = t

    for j in range(M):
        if t[j] == 1:
            q.append([i,j,0])
        

max_day = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    k = q.popleft()
    max_day = max(max_day, k[2])
    for i in range(len(dx)):
        new_x = k[0] + dx[i]
        new_y = k[1] + dy[i]
        # print(new_x, new_y)
        if new_x < 0 or new_x >= N or new_y < 0 or new_y >= M:
            continue
        else:
            if tomato[new_x][new_y] == 0:
                q.append([new_x, new_y, k[2]+1])
                tomato[new_x][new_y] = 1


for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            max_day = -1
            break
    if max_day == -1:
        break

print(max_day)