# 못품..
# tabularization 문제
# table : 배낭에 넣은 개수 \ 배낭 무게를 얼마나 썼는지 여부
# N+1 * C+1 테이블
# DP[i][j] : i 번째 물건까지 고려하여 배낭의 무게 j 까지 채워 넣었을 때 달성할 수 있는 최대 가치
# DP[8][20] 을 찾기 위한 값 계산
# DP[i][j] = DP[i-1][?] 의 형식으로 채워 가기!
# --> DP[i][j] = DP[i-1][j] or DP[i-1][j-w[i]] + V[i] 두 값 중에서 큰 값을 채워 넣는 형식으로 작동
# solution
def solution(capacity, weight, value):
    N = len(weight)
    C = capacity
    dp = [[0 for _ in range(C+1)] for _ in range(N+1)]

    for i in range(1, N+1):
        for w in range(1, C+1):
            if w >= weight[i-1]:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight[i-1]] + value[i-1])
            else:
                dp[i][w] - dp[i-1][w]
    
    return dp[N][C]


if __name__ == '__main__':
    capacity = 20
    weight = [4, 5, 2, 3, 6, 8, 5, 5]
    value = [5, 2, 6, 7, 1, 3, 4, 6]
    sol = solution(capacity, weight, value)
    print(sol)
