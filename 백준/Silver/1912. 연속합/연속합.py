import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

n_set = list(map(int, input().rstrip().split()))

# 힌트 : i 번째 원소로 끝나는 연속된 부분 수열의 최대 합 으로 정의하기
dp = [[0,0]] * t

dp[0] = [-1e9, n_set[0]]

max_value = n_set[0]

for i in range(1, t):
    dp[i] = [max(dp[i-1][0], dp[i-1][1]) + n_set[i] , n_set[i]]
    max_value = max(dp[i][0], dp[i][1], max_value)

print(max_value)