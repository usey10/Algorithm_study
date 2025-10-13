import sys

input = sys.stdin.readline

N = int(input())
a_set = list(map(int, input().split()))
a_set.sort()
# print(a_set)

x = int(input())

count = 0
left = 0
right = N-1

while left < right:
    sum = a_set[left] + a_set[right]
    
    if sum < x:
        left += 1
    elif sum > x:
        right -= 1
    else:
        count += 1
        left += 1

print(count)