import sys

N = int(sys.stdin.readline())


count_5 = N // 5
left = N % 5

left_3 = left % 3

while left_3:
    if count_5 >= 1:
        count_5 -= 1
        left += 5
        left_3 = left % 3
    else:
        break
        
if left_3:
    print(-1)
else:
    print(count_5 + (left // 3))