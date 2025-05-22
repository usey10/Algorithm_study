import collections, sys
stack = collections.deque()
def solution(comment):
    if "push" in comment:
        _, n = comment.split()
        stack.append(int(n))
    elif comment == "pop":
        if stack:
            n = stack.pop()
            return print(n)
        else:
            return print(-1)
    elif comment == "size":
        return print(len(stack))
    elif comment == "empty":
        return print(0 if stack else 1)
    else: # top
        return print(stack[-1] if stack else -1)

N = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for _ in range(N)]
for i in data:
    solution(i)