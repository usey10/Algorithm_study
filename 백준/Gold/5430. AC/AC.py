import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    p = input().strip()
    n = int(input())
    x = input().strip()[1:-1]

    if n == 0:
        x_list = deque()
    else:
        x_list = deque(x.split(','))


    rev = False
    error = False

    for i in p:
        if i == 'D' and x_list:
            if rev:
                x_list.pop()
            else:
                x_list.popleft()
        elif i == 'D' and not x_list:
            error = True
            break
        else:
            rev = not rev

    
    if error:
        print('error')
    else:
        if rev:
            x_list.reverse()

        print("[" + ",".join(str(k) for k in x_list) + "]")