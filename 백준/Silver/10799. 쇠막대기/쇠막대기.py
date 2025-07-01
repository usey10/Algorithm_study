import sys

pipe = sys.stdin.readline().rstrip()

stack = []
before = ''
count = 0

for i in pipe:
    if i == '(':
        stack.append(i)
        before = i
    else:
        stack.pop()
        if before == '(':
            count += len(stack)
            before = i
        else:
            before = i
            count += 1

print(count)