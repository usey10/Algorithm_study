def solution(n):
    answer = []
    result = n
    for i in range(2, n+1):
        if result % i == 0:
            answer.append(i)
            while result % i == 0:
                result = result // i
            
    return answer