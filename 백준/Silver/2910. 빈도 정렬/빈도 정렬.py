import sys
from collections import Counter

N, C = map(int, sys.stdin.readline().split())

n_set = list(map(int,sys.stdin.readline().split()))

count = Counter(n_set)
t = count.most_common()
result = []

for x,i in t:
    for _ in range(i):
        result.append(str(x))

print(" ".join(result))