def solution(n):
    result = 0
    answer = 1
    
    for i in range(1, 11):
        k = answer * i
        if k <= n:
            answer,result = k, i
        else:
            break
            
    return result