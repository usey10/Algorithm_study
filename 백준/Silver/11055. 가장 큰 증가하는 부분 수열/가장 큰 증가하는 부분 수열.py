import sys

input = sys.stdin.readline

N = int(input())
a_list = list(map(int, input().split()))

m_list = [0] * N

for i in range(N):
    before_max = 0

    for j in range(i):
        if a_list[j] < a_list[i]:
            before_max = max(m_list[j], before_max)

    m_list[i] = a_list[i] + before_max


print(max(m_list))