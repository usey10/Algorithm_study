import sys

N, M = map(int, sys.stdin.readline().split())

S = set(sys.stdin.readline().rstrip() for _ in range(N))

count = sum(1 for _ in range(M) if sys.stdin.readline().rstrip() in S)

print(count)