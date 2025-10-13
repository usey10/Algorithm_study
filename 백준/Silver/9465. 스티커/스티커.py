import sys

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    N = int(input())
    lines_0 = list(map(int, input().split()))
    lines_1 = list(map(int, input().split()))

    dp = [[0,0] for _ in range(N+1)]
    dp[1][0] = lines_0[0]
    dp[1][1] = lines_1[0]

    for i in range(2, N+1):
        dp[i][0] = max(dp[i-1][1], max(dp[i-2][0], dp[i-2][1])) + lines_0[i-1]
        dp[i][1] = max(dp[i-1][0], max(dp[i-2][0], dp[i-2][1])) + lines_1[i-1]

    result = max(dp[N-1][0], dp[N-1][1], dp[N][0], dp[N][1])
    print(result)
    