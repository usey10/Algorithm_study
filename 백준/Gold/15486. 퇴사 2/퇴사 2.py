import sys

input = sys.stdin.readline

def solve():
    N = int(input())

    ti = [0] * (N+1)
    pi = [0] * (N+1)
    dp = [0] * (N+2)

    for i in range(N):
        ti[i], pi[i] = map(int, input().split())
    
    # back dp
    for i in range(N-1, -1, -1):
        if i+ti[i] <= N:
            dp[i] = max(dp[i+1], pi[i]+dp[i+ti[i]])
        else:
            dp[i] = dp[i+1]
    
    print(dp[0])



if __name__=='__main__':
    solve()