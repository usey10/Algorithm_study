import sys

input = sys.stdin.readline

N = int(input())

files = {}

for _ in range(N):
    f = input().strip().split('.')[1]

    if f not in files:
        files[f] = 1
    else:
        files[f] += 1

files = sorted(files.items(), key = lambda x:x[0])

for k,v in files:
    print(f"{k} {v}")