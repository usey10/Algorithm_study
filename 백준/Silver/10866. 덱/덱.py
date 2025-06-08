import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

deq = deque()
def deque_check(order):
    if 'push' in order:
        order_i, k = order.split(' ')
        if order_i == 'push_front':
            deq.appendleft(int(k))
        elif order_i == 'push_back':
            deq.append(int(k))
    elif order == 'pop_front':
        if not deq:
            return print(-1)
        k = deq.popleft()
        return print(k)
    elif order == 'pop_back':
        if not deq:
            return print(-1)
        k = deq.pop()
        return print(k)
    elif order == 'size':
        return print(len(deq))
    elif order == 'empty':
        return print(0 if deq else 1)
    elif order == 'front':
        return print(deq[0] if deq else -1)
    elif order == 'back':
        return print(deq[-1] if deq else -1)


for _ in range(N):
    order = sys.stdin.readline().rstrip()
    deque_check(order)