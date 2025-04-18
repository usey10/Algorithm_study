# 1번 문제와 동일하게 힙으로 풀어보자.
from heapq import heappush, heappop
def solution(N, edge):
    dists = [float('inf') for _ in range(N)]
    heap = []

    dists[0] = 0

    heappush(heap, (0, dists[0]))

    while heap:
        n, d = heappop(heap)
        for _, adj, w in filter(lambda x:x[0] == n, edge):
            new_d = d + w
            if new_d < dists[adj]:
                dists[adj] = new_d
                heappush(heap, (adj, new_d))
    
    answer = 0
    for idx, i in enumerate(dists):
        if i > answer:
            answer = idx
    # 이 코드의 문제 : 같은 값이면 작은 인덱스가 나와야 하는데 그게 안됨!
    
    return answer

# # solution
def solution(N, edge):
    start = 0
    dists = [float('inf') for _ in range(N)]
    heap = []

    heappush(heap, (0, start))
    dists[start] = 0

    while heap:
        d, node = heappop(heap)
        for _, adj_node, w in filter(lambda x: x[0] == node, edge):
            new_dist = d + w
            if new_dist < dists[adj_node]:
                dists[adj_node] = new_dist
                heappush(heap, (new_dist, adj_node))
    
    mad_ind = -1
    max_val = -float('inf')
    for i in range(len(dists)):
        if dists[i] > max_val:
            max_val = dists[i]
            max_ind = i

    # 파이선 활용 간결하게.
    max_val = max(dists)
    return dists.index(max_val)


if __name__ == '__main__':
    N = 5
    edge = [[0, 1, 5], [0, 2, 7], [1, 3, 10], [3, 4, 8], [2, 4, 9], [4, 2, 1]]
    sol = solution(N, edge)
    print(sol)
