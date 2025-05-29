import sys
from collections import deque

n = int(sys.stdin.readline())
num = deque()
result = ""
max_num = 0

for j in range(n):
    i = int(sys.stdin.readline())
    if j == 0:
        for k in range(i):
            num.append(k+1)
            result += "+"
        
        before_num = num.pop()
        max_num = max(before_num, max_num)
        result += "-"

    elif before_num < i:
        for k in range(max_num, i):
            num.append(k+1)
            result += "+"
        before_num = num.pop()
        max_num = max(before_num, max_num)
        result += "-"

    elif before_num > i:
        new_num = num.pop()
        if new_num == i:
            result += "-"
            before_num = new_num
            max_num = max(before_num, max_num)
        else:
            result = "NO"
            break
            
    
if result != "NO":
    print("\n".join(i for i in result))
else:
    print(result)