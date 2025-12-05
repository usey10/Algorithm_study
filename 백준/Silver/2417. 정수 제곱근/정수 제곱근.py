import sys
import math

input = sys.stdin.readline

n = int(input())
a = int(math.sqrt(n))
# print(a**2)

if a**2 >= n:
    print(a)
else:
    print(a + 1)