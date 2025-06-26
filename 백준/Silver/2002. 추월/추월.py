import sys
from collections import deque


N = int(sys.stdin.readline())

deas = {sys.stdin.readline().rstrip():i+1 for i in range(N)}
nums = set()
count = 0

for i in range(N):
    x = sys.stdin.readline().rstrip()
    num = deas[x]
    nums.add(num)
    if 1 not in nums:
        count += 1
    else:
        if num != 1:
            set_num = set(i+1 for i in range(num-1))
            if set_num - nums:
                count += 1
            else:
                continue
        else:
            continue

print(count)