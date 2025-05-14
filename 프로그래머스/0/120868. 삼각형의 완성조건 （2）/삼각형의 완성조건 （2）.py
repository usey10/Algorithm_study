def solution(sides):
    max_n = max(sides)
    answer = []
    answer.extend([i for i in range(max_n - min(sides)+1, max_n+1)])
    answer.extend([i for i in range(max_n+1, sum(sides))])
    return len(set(answer))