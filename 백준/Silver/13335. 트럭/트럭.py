import sys
from collections import Counter

n, w, l = map(int, sys.stdin.readline().rstrip().split())

n_set = list(map(int, sys.stdin.readline().rstrip().split()))

pass_brige = [0 for _ in range(w)]
time = 0

while n_set:
    pass_brige.pop(0)
    if sum(pass_brige) + n_set[0] <= l:
        pass_brige.append(n_set.pop(0))
        time += 1
    else:
        pass_brige.append(0)
        time += 1

time += w

print(time)