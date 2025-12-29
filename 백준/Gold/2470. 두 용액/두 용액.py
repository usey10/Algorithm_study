import sys

input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))

low = 0
high = len(li) -1

li.sort()

result_index = [0,0]
result_sol = float('inf')

while low < high:
    x1 = li[low]
    x2 = li[high]
    sums = x1 + x2

    # 인덱스 값 최소 체크
    if abs(sums) < abs(result_sol):
        result_sol = sums
        result_index[0] = low
        result_index[1] = high

    # 인덱스값 올릴거 체크
    if sums < 0:
        low += 1
    else:
        high -= 1

print(" ".join(str(li[i]) for i in result_index))