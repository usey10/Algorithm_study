
import sys

input = sys.stdin.readline

def solve():
    N = int(input())

    min_dp = [[0]*3 for _ in range(2)]
    max_dp = [[0]*3 for _ in range(2)]

    for i in range(N):
        score = list(map(int, input().split()))
        n = i % 2
        b = 0 if n else 1
        max_dp[n][0] = max(max_dp[b][0], max_dp[b][1]) + score[0]
        max_dp[n][1] = max(max_dp[b][0], max_dp[b][1], max_dp[b][2]) + score[1]
        max_dp[n][2] = max(max_dp[b][1], max_dp[b][2]) + score[2]

        min_dp[n][0] = min(min_dp[b][0], min_dp[b][1]) + score[0]
        min_dp[n][1] = min(min_dp[b][0], min_dp[b][1], min_dp[b][2]) + score[1]
        min_dp[n][2] = min(min_dp[b][1], min_dp[b][2]) + score[2]

    print(f"{max(max_dp[(N-1)%2])} {min(min_dp[(N-1)%2])}")
    

if __name__=='__main__':
    solve()