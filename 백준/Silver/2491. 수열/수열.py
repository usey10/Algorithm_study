import sys

input = sys.stdin.readline

n = int(input())

n_set = list(map(int, input().rstrip().split()))

before = 0
max_len = 0
de_len = 0
in_len = 0

for i in range(n):
    # 증가
    if before < n_set[i]:
        in_len += 1
        max_len = max(max_len, de_len)
        de_len = 1
    elif before > n_set[i]:
        de_len += 1
        max_len = max(max_len, in_len)
        in_len = 1
    else:
        in_len += 1
        de_len += 1

    before = n_set[i]

max_len = max(max_len, max(de_len, in_len))
print(max_len)