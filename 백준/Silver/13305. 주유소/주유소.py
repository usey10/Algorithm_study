import sys

input = sys.stdin.readline

N = int(input())
lines = list(map(int, input().rstrip().split()))
prices = list(map(int, input().rstrip().split()))

result = 0
min_price = prices[0]

for i in range(N-1):
    min_price = min(min_price, prices[i])
    result += min_price * lines[i]

print(result)