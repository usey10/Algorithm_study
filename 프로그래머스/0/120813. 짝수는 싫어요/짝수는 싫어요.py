def solution(n):
    N = n // 2 if n%2==0 else n//2 + 1
    return [i*2+1 for i in range(N)]