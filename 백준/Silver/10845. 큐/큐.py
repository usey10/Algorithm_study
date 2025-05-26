import sys
from collections import deque

N = int(sys.stdin.readline())
que = deque()

def queueSystem(x):
    if x == "pop":
        if que:
            i = que.popleft()
            return print(i)
        else:
            return print(-1)
    elif x == "size":
        return print(len(que))
    elif x == "empty":
        return print(0 if que else 1)
    elif x == "front":
        return print(que[0] if que else -1)
    elif x == "back":
        return print(que[-1] if que else -1)
    else:
        i = int(x.replace("push ", ""))
        que.append(i)

for _ in range(N):
    x = sys.stdin.readline().rstrip()
    queueSystem(x)