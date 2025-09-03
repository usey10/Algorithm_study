import sys
from collections import deque

input = sys.stdin.readline
N = int(input().rstrip())
M = int(input().rstrip())

S = input().rstrip()


idx = 0
result = 0
cnt = 0

while idx < M-2:
    if S[idx:idx+3] == "IOI":
        result += 1

        if result == N:
            result -= 1
            cnt += 1
        
        idx += 2

    else:
        result = 0
        idx += 1


print(cnt)

