import sys

input = sys.stdin.readline

N = int(input())

count = 0
before = 1
tmp = 1

# bottom-up
for i in range(N):
    count += tmp
    count %= 15746
    tmp = before
    before = count
	
print(count)
