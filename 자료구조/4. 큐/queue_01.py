# Prob1.
# 카드 섞기 문제
# 1부터 N 까지의 번호로 구성된 N장의 카드가 있다.
# 1번 카드가 가장 위에 그리고 N번 카드는 가장 아래의 상태로 카드가 순서대로 쌓여있다.
# 아래의 동작을 카드 한 장만 남을 때까지 반복했을 때, 가장 마지막 남는 카드 번호를 출력하시오.

# 1. 가장 위의 카드는 버린다.
# 2. 그 다음 위의 카드는 쌓여 있는 카드의 가장 아래에 다시 넣는다.

# 예시 입력)
# N = 4
# 결과: 4

# N = 7
# 결과: 6


def solution(N):
    queue = []
    for i in range(1,N+1):
        queue.append(i)
    
    while len(queue) != 1:
        queue.pop(0)
        val = queue.pop(0)
        queue.append(val)
    return queue[0]

# 모범답안
def solution(N):
    queue = list(range(1, N+1))
    while len(queue) > 1:
        queue.pop(0)
        queue.append(queue.pop(0))
    return queue[0]
# 리스트 한번에 넣을 수 있음
# pop 를 바로 append 에 넣을 수 있음.

if __name__ == '__main__':
    N = 4
    sol = solution(N)
    print(sol)
