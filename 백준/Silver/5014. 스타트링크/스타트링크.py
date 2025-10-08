import sys

input = sys.stdin.readline

F, S, G, U, D = map(int, input().rstrip().split())

dp = [-1] * (F+1)
queue = [[S,0]]
dp[S] = 0

while queue:
    tmp = queue.pop(0)

    count = tmp[1]+1
    up = [tmp[0]+U, count]
    down = [tmp[0]-D, count]

    if up[0] <= F:
        if dp[up[0]] == -1:
            dp[up[0]] = count
            queue.append(up)
    if down[0] > 0:
        if dp[down[0]] == -1:
            dp[down[0]] = count
            queue.append(down)

if dp[G] == -1:
    print("use the stairs")
else:
    print(dp[G])