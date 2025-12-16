import sys

input = sys.stdin.readline

A, B = map(int, input().split())

count = 1

while A != B:
	if A > B:
		count = -1
		break
	
	if B % 2 == 0:
		B = B // 2
		count += 1
	elif B % 10 == 1:
		B = B // 10
		count += 1
	else:
		count = -1
		break

print(count)