import sys
import math

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int,input().rstrip().split())
    alls = 1
    splits = 1


    for i in range(n):
        alls *= m-i
        splits *= i+1
    

    print(alls // splits)