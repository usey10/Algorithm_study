import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)
dp[0] = -1
dp[1] = -1

for i in range(1, n+1):
    if i < 5 and i % 2 == 0:
        dp[i] = i // 2
        # print(i, dp[i], "첫번쨰")
    elif i < 5 and i % 2 != 0:
        dp[i] = -1
        # print(i, dp[i], "두번째")
    elif i == 5:
        dp[i] = 1
        # print(i, dp[i], "세번쨰")
    elif dp[i-2] != -1 and dp[i-5] != -1:
        dp[i] = min(dp[i-2] + 1, dp[i-5] + 1)
        # print(i, dp[i], "네번째")
    elif dp[i-2] != -1:
        dp[i] =  dp[i-2] + 1
        # print(i, dp[i], "다섯번째")
    else:
        dp[i] = dp[i-5] + 1
        # print(i, dp[i], "여섯번째")

print(dp[n])