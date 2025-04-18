# 각 경로별 최단거리 찾기
# start 에서 가기 전에는 구현 할 수 있는데
# 그 다음에 경로를 전부 고려하는 법을 잘 모르겠음..
def solution(N, edge, start):
    result = [0 for _ in range(N)]

    for i,j,k in edge:
        if start == i:
            result[j] = k

# solution

from heapq import heappop, heappush
# 힙을 사용하는 이유 : 거리가 가까운 노드부터 선택해서 짧은 거리를 먼저 다루기 때문에 빠르게 업데이트 할 수 있음
def solution(N, edge, start):
    # 0번인덱스 제외하기 위해, 최단 경로를 가지고 오는 거기 때문에 무한대 설정
    dists = [float('inf') for _ in range(N+1)] 
    heap = []

    heappush(heap, (0, start))
    dists[start] = 0

    while heap:
        d, node = heappop(heap)
        # print(d, node)
        for _,adj_node, w in filter(lambda x: x[0] == node, edge):
            # print(node, adj_node, w)
            new_dist = d + w
            if new_dist < dists[adj_node]:
                dists[adj_node] = new_dist
                heappush(heap, (new_dist, adj_node))
                # print(heap)
    
    return dists[1:]



if __name__ == '__main__':
    N = 5
    edge = [[1, 2, 2], [1, 3, 3], [2, 3, 4], [2, 4, 5], [3, 4, 6], [4, 5, 1]]
    start = 1
    sol = solution(N, edge, start)
    print(sol)
