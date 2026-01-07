import sys

input = sys.stdin.readline

H, W = map(int, input().split())

blocks = list(map(int, input().split()))

tf_blocks = [[0] * W for _ in range(H)]

for i in range(W):
	t = blocks[i]
	for j in range(t):
		tf_blocks[j][i] = 1

result = 0	

for i in range(H):
    walls = False
    idx = 0
    for j in range(W):
        if not walls and tf_blocks[i][j]==1:
            walls = True
            idx = j
        elif walls and tf_blocks[i][j] ==1:
            result += j - idx - 1
            idx = j


				
print(result)