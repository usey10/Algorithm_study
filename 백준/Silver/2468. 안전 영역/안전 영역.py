import sys

input = sys.stdin.readline

N = int(input())

ground = []
max_num = 0

for _ in range(N):
	tmp = list(map(int, input().rstrip().split()))
	tmp_max = max(tmp)
	max_num = max(tmp_max, max_num)
	ground.append(tmp)

# max_num = max(ground)

def max_range(li, k):
	if k == 0:
		return 1
	
	visited = [[False] * len(li) for _ in range(len(li))]
	land = []
	l_count = 0
	dx = [-1, 1, 0, 0]
	dy = [0, 0, -1, 1]
	
	for i in range(len(li)):
		for j in range(len(li)):
			if li[i][j] > k and not visited[i][j]:
				idx = [i, j]
				land.append(idx)
				visited[i][j] = True
				
				while land:
					g = land.pop()
					
					for w in range(len(dx)):
						new_x = g[0] + dx[w]
						new_y = g[1] + dy[w]
						
						if new_x >= 0 and new_x < N and new_y >= 0 and new_y < N:
							if li[new_x][new_y] > k and not visited[new_x][new_y]:
								new_idx = [new_x, new_y]
								land.append(new_idx)
								visited[new_x][new_y] = True
				l_count += 1
				
	return max(l_count, max_range(li, k-1))

print(max_range(ground, max_num))