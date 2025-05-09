def solution(n, numlist):
    answer = []
    for i in numlist:
        if i % n == 0 and i >= n:
            answer.append(i)
    return answer