# Prob2.

# 누적 중간값
# 리스트 arr에 정수로 이루어진 자료가 주어져 있다.
# 출력 역시 정수로 이루어진 동일한 길이의 리스트로,
# 이 리스트의 i번째 값은 arr의 처음부터 i번째까지 값의 중간값이다.
# 단, 짝수개의 값의 중간값은 중간값 2개의 평균으로 계산한다.
# 이 프로그램을 구현하시오.

from heapq import heapify, heappop, heappush

def solution(arr):
    res = []
    for i in range(len(arr)):
        heap = arr[:i+1]
        heapify(heap)
        print(heap)
        mid = i//2
        if i % 2 == 0:
            res.append(heap[mid])
        else:
            num = (heap[mid] + heap[mid+1])/2
            res.append(num)
    return res
# 틀린 답안
# 하나의 힙을 가지고 하는 경우, 레벨에 따라서 중간 값이 중간으로 들어가지 않을 수 있음.
# -> 이 부분에서 틀린 답안이 됨.

# 모범답안
def solution(arr):
    min_heap = []
    max_heap = []
    result = []

    for elem in arr:
        if not min_heap or elem >= min_heap[0]:
            heappush(min_heap, elem)
            if len(min_heap) > len(max_heap) + 1:
                heappush(max_heap, -heappop(min_heap))
        else:
            heappush(max_heap, -elem)
            if len(max_heap) > len(min_heap):
                heappush(min_heap, -heappop(max_heap))
        
        if len(max_heap) == len(min_heap):
            result.append((-max_heap[0] + min_heap[0])/2.0)
        else:
            result.append(min_heap[0])
    return result


if __name__ == '__main__':
    arr = [1, 3, 5, 2, 7, 4, 5, 23, -4, 52, 45]
    sol = solution(arr)
    print(sol)
