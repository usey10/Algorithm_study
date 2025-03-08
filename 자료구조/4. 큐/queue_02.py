# Prob2.
# 요세푸스 문제
# N과 K가 주어졌을 때 (N, K) 요세푸스 순열을 구하시오.
# N과 K는 N >= K 를 만족하는 양의 정수이다.
# 1부터 N 번까지 N명이 순서대로 원을 이루어 모여 있다.
# 이 모임에서 원을 따라 순서대로 K번째 사람을 제외한다.
# 모든 사람이 제외될 때까지 반복하며 이 때, 제외되는 순서가 요세푸스 순열이다.

# 예시 입출력
# N = 5
# K = 2
# 결과: 2, 4, 1, 5, 3

# N = 7
# K = 3
# 결과: 3, 6, 2, 7, 5, 1, 4


def solution(N, K):
    queue = list(range(1,N+1))
    result = []
    while len(queue) > 1:
        for i in range(K-1):
            queue.append(queue.pop(0))
        result.append(queue.pop(0))
    result.append(queue.pop(0))
    return result

# 모범 답안
# while 에서 존재하는지 여부로 하면 쉽게 구현 가능!
# pre allocation 형식으로 진행(데이터가 커지면 조금 더 빨리 할 수 있다!)

def solution(N,K):
    queue = list(range(1,N+1))
    result = [0 for _ in range(N)]

    ind = 0
    while queue:
        for _ in range(K-1):
            queue.append(queue.pop(0))
        result[ind] = queue.pop(0)
        ind += 1

    return result
        

if __name__ == '__main__':
    N = 5
    K = 2
    sol = solution(N, K)
    print(sol)
