import sys

input = sys.stdin.readline

N, S = map(int, input().split())
n_set = list(map(int, input().split()))

if sum(n_set) < S:
    print(0)
    sys.exit()

r, l = 0, 0
n_sum = n_set[0]
n_len = 1
ans = float('inf')

while True:
    if n_sum < S and r >= N-1:
        break
    elif n_sum < S:
        r += 1
        n_len += 1
        n_sum += n_set[r]
    else:
        ans = min(n_len, ans)
        n_sum -= n_set[l]
        l += 1
        n_len -= 1

print(ans)