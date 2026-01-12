import sys
from collections import deque

def dfs(a, stop):
    queue.append(a)

    while queue:
        check = queue.pop()
        tmp = point[check]
        for i in tmp:
            if not visited[i]:
                visited[i] = visited[check] * -1
                queue.append(i)
            elif visited[i] * visited[check] == -1:
                continue
            else:
                stop = False
                break
        
        if not stop:
            break
    return stop

input = sys.stdin.readline

K = int(input())

for tc in range(K):
    V, E = map(int, input().split())

    point = [ [] for _ in range(V+1)]

    for _ in range(E):
        u, v = map(int, input().split())
        point[u].append(v)
        point[v].append(u)


    visited = [0] * (V+1)
    visited[0] = 1
    queue = deque()
    stop = True

    for j in range(1, V+1):
        if not visited[j]:
            visited[j] = 1
            stop = dfs(j, stop)

        if not stop:
            break
    
    if stop:
        print('YES')
    else:
        print('NO')