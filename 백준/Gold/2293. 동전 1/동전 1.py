import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

li = [0] * (k+1)

li[0] = 1

for c in coins:
    for i in range(c, k+1):
        li[i] = li[i] + li[i-c]

print(li[k])