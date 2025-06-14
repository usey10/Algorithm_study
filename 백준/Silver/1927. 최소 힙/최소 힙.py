import sys
from heapq import heappop, heappush, heapify

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap:
            result = heappop(heap)
            print(result)
        else:
            print(0)
    else:
        heappush(heap, x)