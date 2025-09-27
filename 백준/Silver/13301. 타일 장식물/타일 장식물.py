import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (n + 1)

dp[0] = 0
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n]*4 + dp[n-1]*2)

# 1 1 2 3 5 8