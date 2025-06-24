import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    nums = list(map(int, sys.stdin.readline().split()))
    for num in nums:
        if len(heap) < N:
            heapq.heappush(heap, num)
        else:
            if num > heap[0]:
                heapq.heappushpop(heap, num)

print(heap[0])