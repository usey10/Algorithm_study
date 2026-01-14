import sys
from collections import deque


input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())

    tr = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        tr[b].append(a)
    
    def bfs(s):
        cnt = 0
        queue = deque([s])
        visited = [0] * (N+1)
        visited[s] = 1
        
        while queue:
            curr = queue.popleft()
            for j in tr[curr]:
                if not visited[j]:
                    visited[j] = 1
                    queue.append(j)
                    cnt += 1
        
        return cnt
    
    result = []
    max_cnt = -1

    for i in range(1, N+1):
        if not tr[i]:
            res = 0
        else:
            res = bfs(i)

        if res > max_cnt:
            max_cnt = res
            result = [str(i)]
        elif res == max_cnt:
            result.append(str(i))

    print(" ".join(result))


solve()