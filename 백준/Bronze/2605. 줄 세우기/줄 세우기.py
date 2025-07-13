import sys

n = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().rstrip().split()))
dp = []

dp_left = []


for idx, i in enumerate(num):
    if i == 0:
        dp.append(idx+1)
    else:
        for j in range(i):
            dp_left.append(dp.pop())
        dp.append(idx+1)
        for j in range(i):
            dp.append(dp_left.pop())

print(" ".join(str(i) for i in dp))