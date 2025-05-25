import sys

K = int(sys.stdin.readline())
all = []

for _ in range(K):
    i = int(sys.stdin.readline())
    if i == 0:
        all.pop()
    else:
        all.append(i)

print(sum(all))