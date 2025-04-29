def solution(n):
    k = n // 2
    return sum([i*2 for i in range(1, k+1)])