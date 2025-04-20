from heapq import heappop, heappush
# def solution(N, edge):
#     def insert_heap(node, adj_node, use_node):
        
#     mst = [False for _ in range(N+1)]
#     heap = []
#     result = 0
#     use_node = set()

#     mst[0] = True
#     mst[1] = True
#     # print(all(mst))
#     print(edge)
    
#     for n, adj_n, w in filter(lambda x : x[0] == 1 or x[1] == 1, edge):
#         print(n, adj_n, w)
#         heappush(heap, (w, n, adj_n))
#         use_node.append([n, adj_n, w])
#     print(heap)
#     print(use_node)

#     while all(mst) == False:
#         weight, node, adj_node = heappop(heap)
#         if all([mst[node], mst[adj_node]]) == False:
#             result += weight
#             mst[node], mst[adj_node] = True, True
#             # for n, adj_n, w in filter(lambda x:)
#         else:
#             continue
#     return result

# 중복을 고려해서 heap 하는 방법 구현에서 막힘..

# solution
def solution(N, edge):
    visited = [False for _ in range(N+1)]
    start = 1

    heap = []
    visited[start] = True

    for a, b, w in filter(lambda x:x[0] == start or x[1] == start,edge):
        node = a if start == b else b
        heappush(heap, (w, node))
        # print('첫 엣지', a, b, w)

    mst_weight = 0
    while heap:
        w, node = heappop(heap)

        # 막혔던 부분
        # 그냥.. 썼든 안썼든 다 고려 한 다음에 visited node 로 체크(어차피 쓴거는 걸러지니까!)
        if visited[node]:
            continue

        visited[node] = True
        mst_weight += w

        for a, b, new_w in filter(lambda x:x[0] == node or x[1] == node,edge):
            new_node = a if start == b else b
            heappush(heap, (new_w, new_node))
            # print("새로운 엣지", a, b, new_w)
    
    return mst_weight


if __name__ == '__main__':
    N = 5
    edge = [[1, 2, 2], [1, 3, 3], [2, 3, 4], [2, 4, 5], [3, 4, 6], [5, 1, 1]]
    sol = solution(N, edge)
    print(sol)
