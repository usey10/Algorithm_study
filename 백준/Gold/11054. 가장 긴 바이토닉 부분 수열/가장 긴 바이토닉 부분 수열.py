import sys

input = sys.stdin.readline

def solve():
    N = int(input())
    li = list(map(int, input().split()))

    in_dp = [0] * N
    de_dp = [0] * N

    in_dp[0] = 1
    de_dp[N-1] = 1

    for i in range(1, N):
        in_dp[i] = 1
        de_dp[N-i-1] = 1

        for j in range(i):
            if li[j] < li[i]:
                in_dp[i] = max(in_dp[i], in_dp[j]+1)
            
            if li[N-j-1] < li[N-i-1]:
                de_dp[N-i-1] = max(de_dp[N-i-1], de_dp[N-j-1]+1)

    
    result = 0

    for i in range(N):
        result = max(result, in_dp[i]+de_dp[i]-1)
    
    print(result)

solve()