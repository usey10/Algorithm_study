import sys

input = sys.stdin.readline

N = int(input())
credit = list(map(int, input().split()))
T = int(input())


if sum(credit) <= T:
    print(max(credit))
    sys.exit() # 프로그램 종료


low = 0
high = max(credit)
result = 0

while low <= high:
    mid = (low+high)//2

    tmp = 0
    for i in credit:
        tmp += min(i, mid)
    
    if tmp <= T:
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)