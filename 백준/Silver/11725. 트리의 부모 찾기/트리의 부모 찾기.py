import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

node = [[] for _ in range(N+1)]

for _ in range(N-1):
    x,y = map(int, sys.stdin.readline().rstrip().split())

    node[x].append(y)
    node[y].append(x)

parents = [0] * (N+1) # 부모노드 idx
visited = [False] * (N+1)
deq = deque()

visited[1] = True
deq.append(1)

while deq:
    k = deq.popleft()
    k_set = node[k]

    for t in k_set:
        if visited[t] == False:
            visited[t] = True
            parents[t] = k
            deq.append(t)

for i in range(2, N+1):
    print(parents[i])