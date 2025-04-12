# 풀려는 시도
# N+1
# dp[i]를 구해야 함.
# dp[i] =
# depth 가 커지면.. 여러 경로가 있는데 그걸 고려하지 않아도 되는걸까?
# -> 여기서 막힘

# solution
# 4*4 DP 테이블
# 각 해당 블록을 제거하는데 가장 최소의 에너지 기록
# 5626
# 1을 제거하기 위해 제거했어야 하는 블록 중 가장 작은 값 선택!
# 최적화
def solution(depth, n, blocks):
    # D = len(blocks)
    D = depth + 1 # 딱 구해야 하는 Depth 까지만 dp 테이블을 만들기 위해서. -> 계산 최적화
    N = len(blocks[0])

    # dp = [[0 for _ in range(N)] for _ in range(D)]
    dp = [[0 for _ in range(N)] for _ in range(2)] # Depth 가 정해져 있고, 그 Depth 에 도달하려면 앞 경로만 있으면 되니까 2줄만 있어도 됨! -> 메모리 최적화

    for i in range(N):
        dp[0][i] = blocks[0][i]
    
    for i in range(1, D):
        for j in range(N):
            if j == 0:
                # dp[i][j] = min(dp[i-1][j:j+2]) + blocks[i][j]
                dp[i%2][j] = min(dp[(i-1)%2][j:j+2]) + blocks[i][j]
            elif j == 3:
                # dp[i][j] = min(dp[i-1][j-1:j+1]) + blocks[i][j]
                dp[i%2][j] = min(dp[(i-1)%2][j-1:j+1]) + blocks[i][j]
            else:
                # dp[i][j] = min(dp[i-1][j-1:j+2]) + blocks[i][j]
                dp[i%2][j] = min(dp[(i-1)%2][j-1:j+2]) + blocks[i][j]

    return  dp[depth%2][n]

if __name__ == '__main__':
    depth = 3
    n = 3
    blocks = [[5, 6, 2, 6],
             [1, 6, 4, 9],
             [5, 6, 9, 4],
             [55, 14, 21, 14]]
    sol = solution(depth, n, blocks)
    print(sol)
