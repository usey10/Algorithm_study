import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())

tomato = []

for _ in range(H):
	lines = []
	for _ in range(N):
		tmp = list(map(int, input().split()))
		lines.append(tmp)
	tomato.append(lines)
	
# print(tomato)
bfs = deque()

for i in range(M):
	for j in range(N):
		for k in range(H):
			if tomato[k][j][i] == 1:
				xyh = [k, j, i]
				bfs.append(xyh)

new_h = [0, 0, -1, 0, 0, 1]
new_y = [0, -1, 0, 0, 1, 0]
new_x = [-1, 0, 0, 1, 0, 0]

# print(bfs)
while bfs:
    ch, cy, cx = bfs.popleft()

    for k in range(len(new_x)):
        nx = cx + new_x[k]
        ny = cy + new_y[k]
        nh = ch + new_h[k]

        
        if nx < 0 or nx >= M or ny < 0 or ny >= N or nh < 0 or nh >= H:
            continue
        else:
            if tomato[nh][ny][nx] == 0:
                tomato[nh][ny][nx] = tomato[ch][cy][cx] + 1
                new_xyh = [nh, ny, nx]
                bfs.append(new_xyh)


days = 0
all_visited = True

for k in range(H):
    for j in range(N):
        for i in range(M):
            if tomato[k][j][i] == 0:
                all_visited = False
                days = -1
                break
            days = max(days, tomato[k][j][i])

        if not all_visited: break
    if not all_visited: break


print(days-1 if days!=-1 else days)