import sys

num = int(sys.stdin.readline())

for _ in range(num):
    N, M = map(int, sys.stdin.readline().rstrip().split(" "))
    paper = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    paper_index = list(i for i in range(N))
    sort_num = 0
    while paper:
        i = paper.pop(0)
        idx = paper_index.pop(0)
        if len(paper) == 0:
            sort_num += 1
            break
        elif max(paper) <= i:
            sort_num += 1
            if idx == M:
                break
        elif max(paper) > i:
            paper.append(i)
            paper_index.append(idx)
    print(sort_num)