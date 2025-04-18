from heapq import heappop, heappush

def solution(N, flight, a, b, k):
    dists = [[0, float('inf')] for _ in range(N)]
    heap = []

    start = a
    end = b

    dists[start][1] = 0
    heappush(heap, (start, dists[start][1]))

    while heap:
        n, d = heappop(heap)
        # print(n, d)
        for _, adj, w in filter(lambda x: x[0] == n, flight):
            # print(n, adj, w)
            new_d = w + d
            if new_d < dists[adj][1]:

                if dists[adj][0] == k:
                    # print("k 넘어감",dists)
                    continue

                dists[adj][1] = new_d
                dists[adj][0] += 1
                heappush(heap, (adj, new_d))
                # print(heap) 
                
    if dists[end][0] > k:
        return -1
    else:
        return dists[end][1]



def solution(N, flight, a, b, k):
    adj_lists = [[] for _ in range(N)]
    for src, dst, price in flight:
        adj_lists[src].append((dst, price))
    
    best_cnt = [float('inf') for _ in range(N)]
    heap = []
    heappush(heap, (0,0,a))

    while heap:
        price, count, node = heappop(heap)
        if best_cnt[node] < count:
            continue

        best_cnt[node] = count
        if count > k:
            continue

        # heap 는 price 가 점점 커지기 때문에, 종료조건을 줄 수 있음.
        if node == b:
            return price

        for adj_node, add_price in adj_lists[node]:
            heappush(heap, (price + add_price, count + 1, adj_node))
    
    return -1


if __name__ == '__main__':
    N = 4
    flight = [[0, 2, 1], [1, 3, 20], [1, 0, 8], [2, 3, 1], [0, 3, 3]]
    a = 1
    b = 3
    k = 2
    sol = solution(N, flight, a, b, k)
    print(sol)
