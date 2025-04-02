# 1. 일단 질문 이해 못함.

# 거리가 1인 경우 ~~ 큰 숫자에서 이진 탐색으로 찾아가는 방법으로 구현
# a 거리보다 가까운 bucket 에는 공을 넣지 않음 -> 구현 가능한지??


# solution
def solution(buckets, m):
    left = 0
    right = max(buckets)

    buckets.sort()
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        n = 1
        last = 0
        for i in range(1, len(buckets)):
            if buckets[i] - buckets[last] >= mid:
                last = i
                n += 1

            if n >= m:
                break
        if n >= m:
            answer = max(answer, mid)
            left = mid + 1
        else:
            right = mid - 1
    return answer

if __name__ == '__main__':
    buckets = [1, 2, 3, 4, 7]
    m = 3
    sol = solution(buckets, m)
    print(sol)
