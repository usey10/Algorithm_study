import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    n_set = set(map(int, sys.stdin.readline().rstrip().split()))
    M = int(sys.stdin.readline())
    m_set = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in m_set:
        print(1 if i in n_set else 0)