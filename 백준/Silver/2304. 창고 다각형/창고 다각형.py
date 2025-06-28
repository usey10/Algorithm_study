import sys

N = int(sys.stdin.readline().rstrip())
cols = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
cols.sort()

max_h = max(cols, key=lambda x: x[1])[1]
max_index = [i for i, p in enumerate(cols) if p[1] == max_h][0]

area = 0

height = cols[0][1]
num = cols[0][0]
for i in range(1, max_index+1):
    if cols[i][1] >= height:
        area += (cols[i][0] - num) * height
        height = cols[i][1]
        num = cols[i][0]

height = cols[-1][1]
num = cols[-1][0]
for i in range(N-2, max_index-1, -1):
    if cols[i][1] >= height:
        area += (num - cols[i][0]) * height
        height = cols[i][1]
        num = cols[i][0]

area += max_h

print(area)