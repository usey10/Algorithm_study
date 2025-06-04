import sys

N, M = map(int, sys.stdin.readline().rstrip().split(' '))
all_std = {}

for i in range(N):
    K = int(sys.stdin.readline())
    std_id = sys.stdin.readline().rstrip().split(" ")
    for j in range(K):
        if std_id[j] in all_std:
            all_std[std_id[j]] += 1
        else:
            all_std[std_id[j]] = 1

print(len(list(filter(lambda x:all_std[x] >= M, all_std))))