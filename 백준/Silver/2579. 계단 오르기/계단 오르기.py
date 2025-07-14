import sys

N = int(sys.stdin.readline())

score = [int(sys.stdin.readline()) for _ in range(N)]
dp = [[0] * 2 for _ in range(N)]


dp[0][0] = score[0]
dp[0][1] = score[0]

if N > 1:
    dp[1][0] = score[1]
    dp[1][1] = score[0] + score[1]

for i in range(2, N):
    dp[i][0] = max(dp[i-2]) + score[i]
    dp[i][1] = dp[i-1][0] + score[i]

print(max(dp[N-1]))