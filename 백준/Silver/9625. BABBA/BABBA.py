import sys

input = sys.stdin.readline

# A
# B
# BA
# BAB
# BABBA

n = int(input())

dp = [[0,0] for _ in range(n+1)]

dp[0][0] = 1
dp[0][1] = 0

for i in range(1, n+1):
    dp[i][0] = dp[i-1][1]
    dp[i][1] = dp[i-1][1] + dp[i-1][0]

print(dp[n][0], dp[n][1])