import sys
from collections import deque

input = sys.stdin.readline
N = int(input().rstrip())

matrix = []



for i in range(N):
    tmp = list(map(int, input().rstrip().split()))
    matrix.append(tmp)

for k in range(N):
    for i in range(N):
        for j in range(N):
           matrix[i][j] = max(matrix[i][j], (matrix[i][k]*matrix[k][j])) 

# print(matrix)

for i in range(N):
    print(" ".join(str(k) for k in matrix[i]))



