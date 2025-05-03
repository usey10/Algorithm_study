def solution(n):
    def method(k):
        count = 0
        for i in range(k):
            count += 1 if k % (i+1) == 0 else 0
            if count == 3:
                return True
        return False
    
    answer = 0
    for i in range(n):
        answer += method(i+1)
    return answer