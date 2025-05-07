def solution(n):
    answer = []
    # print(round(n**0.5))
    for i in range(1, n+1):
        if n % i == 0:
            answer.append(i)
    return answer