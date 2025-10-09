import sys

input = sys.stdin.readline

N,M = map(int, input().split())

n_set = [i+1 for i in range(N)]

m_tmp = []

for i in range(N):
    check = n_set.copy()

    tmp = [check[i]]
    check.pop(i)
    k = [tmp, check]
    m_tmp.append(k)


result = []

while m_tmp:
    tmp = m_tmp.pop(0)
    # print(tmp)

    if len(tmp[0]) == M:
        result.append(tmp[0])
    else:
        for i in range(len(tmp[1])):
            check = tmp[1].copy()
            num = tmp[0].copy()
            num.append(check[i])
            check.pop(i)
            k = [num, check]
            m_tmp.append(k)

for i in range(len(result)):
    print(' '.join(str(j) for j in result[i]))
