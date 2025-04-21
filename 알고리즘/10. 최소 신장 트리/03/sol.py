# 노드를 만들 수는 있으니, 프림메소드!
from heapq import heappop, heappush
def solution(x, y):
    def manhattan(i,j):
        return abs(x[i] - x[j]) + abs(y[i] - y[j])
    
    N = len(x)
    visited = [False for _ in range(N)]
    start = 0

    heap = []
    visited[start] = True
    
    count = 0
    result = 0

    for i in range(1, N):
        heappush(heap, (manhattan(0,i), i))

    while heap:
        w, n = heappop(heap)
        if visited[n]:
            continue
        if count == N:
            break

        result += w
        count += 1
        visited[n] = True
        for i in range(1, N):
            if i != n:
                heappush(heap, (manhattan(n,i), i))

    return result

# solution
# 프림 메소드가 유리함 : 모든 점끼리 다 연결되어있는걸 다 계산하고 만들어야 하는 문제

def solution(x, y):
    N = len(x)
    start = 0

    visited = [False for _ in range(N)]
    heap = []
    visited[start] = True

    for i in range(N):
        if i == start:
            continue
        w = m_dist((x[start], y[start]), (x[i],y[i]))
        heappush(heap, (w, i))

    mst_weight = 0
    while heap:
        w, node = heappop(heap)

        if visited[node]:
            continue

        visited[node] = True
        mst_weight += w

        for i in range(N):
            if i == node:
                continue
            w = m_dist((x[node], y[node]), (x[i],y[i]))
            heappush(heap, (w, i))

    return mst_weight

def m_dist(pt1, pt2):
    return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])



if __name__ == '__main__':
    x = [0, 0, 3, 3, 6]
    y = [0, 3, 1, 4, 3]
    sol = solution(x, y)
    print(sol)
