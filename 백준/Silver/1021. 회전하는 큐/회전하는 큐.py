import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split(" "))
que = deque(i+1 for i in range(N))
    
count = 0


nums = map(int, sys.stdin.readline().rstrip().split(" "))
for x in nums:
    i_num = que.index(x)
    if i_num <= (len(que) // 2):
        while que[0] != x:
            que.append(que.popleft())
            count += 1
    else:
        while que[0] != x:
            que.appendleft(que.pop())
            count += 1

    que.popleft()

print(count)