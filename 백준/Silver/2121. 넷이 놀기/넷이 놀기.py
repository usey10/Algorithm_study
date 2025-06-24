import sys

N = int(sys.stdin.readline())

A, B = map(int, sys.stdin.readline().rstrip().split())

dots = set(tuple(map(int, (sys.stdin.readline().rstrip().split()))) for _ in range(N))

count = 0

def match_dots(i, j, a, b):
    match_dot = set([(i+a,j), (i,j+b), (i+a, j+b)])
    return match_dot


while len(dots) >= 4:
    i = dots.pop()
    match_dot = []
    match_dot.append(match_dots(i[0], i[1], A, B))
    match_dot.append(match_dots(i[0], i[1], -A, B))
    match_dot.append(match_dots(i[0], i[1], A, -B))
    match_dot.append(match_dots(i[0], i[1], -A, -B))
    for dot in match_dot:
        if dot - dots:
            continue
        else:
            count +=1

print(count)