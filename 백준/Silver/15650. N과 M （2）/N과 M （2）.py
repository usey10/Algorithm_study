import sys

input = sys.stdin.readline

N, M = map(int, input().split())


li = []
results = []

def backtracking(li, s):
    if len(li) == M:
        results.append(li)
        return
    
    if s > N:
        return
    
    if len(li) < M:
        for i in range(s, N+1):
            # print(i)
            backtracking(li + [i], i+1)

backtracking(li,1)

for i in results:
    print(" ".join(str(k) for k in i))