import sys

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    N = int(input())
    scores = [[0,0] for _ in range(N)]
    for k in range(N):
        scores[k] = list(map(int, input().rstrip().split()))
    
    count = 0
    scores.sort(key = lambda x:x[0])
    # print(scores)
    min_sc = scores[0][1]

    for i in range(N):
        if scores[i][1] <= min_sc:
            count += 1
        min_sc = min(min_sc,scores[i][1])

    print(count)