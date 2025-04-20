def solution(N, edge):
    sort_edge = sorted(edge, key=lambda x:x[2])
    # print(sort_edge)
    result = 0
    connect = [False for _ in range(N+1)]
    # print(connect)

    for n, adj_n, w in sort_edge:
        # print(n, adj_n, w)
        if connect[adj_n] == False and connect[n] == True:
            result += w
            connect[adj_n] = True
            # print(connect)
        elif connect[adj_n] == False and connect[n] == False:
            result += w
            connect[adj_n], connect[n] = True, True
            # print(connect)
        elif connect[adj_n] == True and connect[n] == False:
            result += w
            connect[n] = True
            # print(connect)
        else:
            continue

    return result
        
# solution
# union find 구현이 없었음...
from heapq import heappop, heappush
def solution(N, edge):
    # heap sort 방식으로 구현
    rank = [1 for _ in range(N+1)]
    parent = [i for i in range(N+1)]

    def union(x, y):
        x_root = find(x)
        y_root = find(y)
        if x_root == y_root:
            return False
        
        if rank[x_root] < rank[y_root]:
            x_root, y_root = y_root, x_root

        parent[y_root] = x_root
        rank[x_root] += rank[y_root]

        return True
    
    def find(x):
        if parent[x] == x: # 종료조건
            return x
        parent[x] = find(parent[x])
        return parent[x]
    
    heap = []
    for a, b, w in edge:
        heappush(heap, (w,a,b))
    
    mst_weight = 0
    count = 0 # 노드 추가시 올려서 출력

    while heap:
        w, a, b = heappop(heap)
        if union(a, b):
            mst_weight += w
            count += 1
        if count == N:
            break

    return mst_weight



if __name__ == '__main__':
    N = 5
    edge = [[1, 2, 2], [1, 3, 3], [2, 3, 4], [2, 4, 5], [3, 4, 6], [5, 1, 1]]
    sol = solution(N, edge)
    print(sol)
