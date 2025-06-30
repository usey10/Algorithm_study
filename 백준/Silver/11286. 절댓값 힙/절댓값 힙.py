import sys
from heapq import heapify, heappop, heappush

N = int(sys.stdin.readline())

heap = []
heapify(heap)

for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap:
            pops = heappop(heap)
            print(pops[1])
        else:
            print(0)
    else:
        heappush(heap, (abs(x), x))