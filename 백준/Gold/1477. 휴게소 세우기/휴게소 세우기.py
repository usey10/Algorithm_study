import sys

input = sys.stdin.readline

N, M, L = map(int, input().split())

n_set = [0]

n_set.extend(list(map(int, input().split())))

n_set.append(L)

n_set.sort()
dis = [n_set[i+1] - n_set[i] for i in range(N+1)]

low = 1
high = L

while low < high:
    new_spot = 0
    mid = (low + high) // 2
    for i in dis:
        if i > mid:
            new_spot += (i-1) // mid
    
    if new_spot > M:
        low = mid + 1
    else:
        high = mid

print(high)