def solution(n):
    answer = 0
    natural = []
    natural.extend(set([1,n]))
    for i in range(n):
        if i+1 not in natural:
            if n % (i+1) == 0:
                natural.extend(set([i+1, n//(i+1)]))
    return len(natural)