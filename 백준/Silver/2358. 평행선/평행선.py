import sys
from collections import Counter

n = int(sys.stdin.readline())

dots = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
lines = set()

x_count = Counter()
y_count = Counter()

for x,y in dots:
    x_count[x] += 1
    y_count[y] += 1

result = sum(1 for v in x_count.values() if v >= 2)
result += sum(1 for v in y_count.values() if v >= 2)
print(result)