import sys

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())

nodes = {i+1:[] for i in range(n)}

for _ in range(m):
	x, y = map(int, input().split())
	nodes[x].append(y)
	nodes[y].append(x)
	
visited = [False] * (n+1)

check = [[a, 0]]
visited[a] = True
con = False
cn = 0


while check:
	k = check.pop()
	
	for i in nodes[k[0]]:
		if i == b:
			con = True
			cn = k[1]+1
			break
			
		if not visited[i]:
			visited[i] = True
			tmp = [i, k[1]+1]
			check.append(tmp)
			
			
	if con:
		break
	

print(cn if con else -1)
