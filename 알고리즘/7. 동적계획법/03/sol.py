# dp 테이블 구조..
# N 개수 * 선택 개수 최대 (N//2)
# dp[0][j] = 다 0(N 이 0)
# dp[i][0] = 0 (선택된 거가 없어서)
# 다음을 모르겠음..


# solution
# i번째까지 고려했을 떄 최대 가치를 보기.
# dp[i] = dp[i-1], dp[i-2]+ rewards[i]
# 원으로 되어있기 때문에, 첫 값을 포함하고 마지막 값을 제외하거나 / 첫 값을 제외하고 두가지 방법을 모두 진행해보기!
def solution(N, rewards):
    # 0번째를 선택할 수도 있으면, N-1번쨰는 없다 친다.
    dp = [0 for _ in range(N-1)]
    dp[0] = rewards[0]
    dp[1] = max(dp[0], rewards[1])

    for i in range(2, N-1):
        dp[i] = max(dp[i-1], dp[i-2] + rewards[i])
    answer = dp[N-2]

    # 0번째를 선택하지 않고, N-1번쨰를 선택할 수 있게 한다.
    dp = [0 for _ in range(N)]
    dp[0] = 0
    dp[1] = rewards[1]
    for i in range(2,N):
        dp[i] = max(dp[i-1], dp[i-2] + rewards[i])
        
    return max(answer, dp[N-1])




if __name__ == '__main__':
    N = 6
    rewards = [5, 10, 5, 7, 5, 9]
    sol = solution(N, rewards)
    print(sol)
