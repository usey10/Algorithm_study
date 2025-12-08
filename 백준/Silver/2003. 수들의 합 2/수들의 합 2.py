import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int, input().split())
a_set = list(map(int, input().split()))

count = 0
dq = deque()
for k in range(N):
	dq.append(a_set[k])
	# print(dq)
	
	if sum(dq) == M:
		count += 1
		# print("M 맞음")
		# print(dq)
	elif sum(dq) > M:
		while sum(dq) > M:
			dq.popleft()
		
		if sum(dq) == M:
			count += 1
			# print("빼고 M 맞음")
			# print(dq)

	else:
		continue
		
print(count)