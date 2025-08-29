import sys


n = int(sys.stdin.readline().rstrip())
cnt = 0

for _ in range(n):
    words = sys.stdin.readline().rstrip()
    stack = []

    # print(words)
    for i in words:
        # print(i)
        if len(stack) != 0:
            if i != stack[-1]:
                stack.append(i)
            else:
                stack.pop()
        else:
            stack.append(i)
    # print(stack)
    
    
    if len(stack) == 0:
        cnt += 1



print(cnt)