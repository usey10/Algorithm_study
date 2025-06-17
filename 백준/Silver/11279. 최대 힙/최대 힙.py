import sys
from heapq import heapify, heappop, heappush

N = int(sys.stdin.readline())
num = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if num:
            result = heappop(num)
            print(-result)
        else:
            print(0)
    else:
        heappush(num, -x)