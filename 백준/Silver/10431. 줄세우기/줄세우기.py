import sys

input = sys.stdin.readline

P = int(input())

for _ in range(P):
    line = list(map(int, input().rstrip().split()))
    T = line[0]
    childs = line[1:]
    
    sort_child = []
    works = 0

    for i in childs:
        if not sort_child:
            sort_child.append(i)
        else:
            idx = len(sort_child)
            A = 0
            while sort_child[idx-1] > i and idx >= 1:
                A += 1
                idx -= 1
            
            works += A
            sort_child = sort_child[:idx] + [i] + sort_child[idx:]
            # print(sort_child)
        
    print(str(T) + " " + str(works))