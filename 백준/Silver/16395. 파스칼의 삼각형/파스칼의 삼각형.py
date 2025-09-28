import sys

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

dp = [[1]*(i+1) for i in range(n)]

for i in range(1, n):
    for j in range(1, len(dp[i-1])):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]


print(dp[n-1][k-1])