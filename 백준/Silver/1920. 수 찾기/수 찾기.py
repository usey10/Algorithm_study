import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().strip().split(" ")))
A.sort()
M = int(sys.stdin.readline())
m_num = list(map(int, sys.stdin.readline().strip().split(" ")))

def binary_search(start, end, target):
    if start > end:
        return 0
    
    mid = (start + end) // 2
        
    if target == A[mid]:
        return 1
    elif target > A[mid]:
        return binary_search(mid+1, end, target)
    elif target < A[mid]:
        return binary_search(start, mid-1, target)

for i in m_num:
    print(binary_search(0, len(A)-1, i))