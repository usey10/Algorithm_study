import sys

N,M = map(int, sys.stdin.readline().rstrip().split())
password = {}

for _ in range(N):
    x = sys.stdin.readline().rstrip().split()
    password[x[0]] = x[1]

for _ in range(M):
    y = sys.stdin.readline().rstrip()
    print(password[y])