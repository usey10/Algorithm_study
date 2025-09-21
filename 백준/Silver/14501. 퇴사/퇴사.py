import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

n_set = []

for i in range(N):
    tmp = list(map(int, input().rstrip().split()))
    n_set.append(tmp)

dp = [0]*(N+1)
for i in range(N-1, -1, -1):
    if i + n_set[i][0] <= N:
        dp[i] = max(n_set[i][1] + dp[i+n_set[i][0]], dp[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[0])