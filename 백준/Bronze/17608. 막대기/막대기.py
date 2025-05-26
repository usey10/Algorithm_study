import sys
from collections import deque

N = int(sys.stdin.readline())

all_stick = deque([int(sys.stdin.readline()) for _ in range(N)])

count = 0
stick_length = 0


for _ in range(N):
    length = all_stick.pop()
    if stick_length < length:
        count += 1
        stick_length = length
    
print(count)