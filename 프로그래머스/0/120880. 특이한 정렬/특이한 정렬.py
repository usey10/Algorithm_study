def solution(numlist, n):
    answer = []
    for i in numlist:
        a = abs(n-i)
        answer.append([a,i])

    answer.sort(key=lambda x:x[1], reverse=True)
    answer.sort(key=lambda x:x[0])
    
    return [i[1] for i in answer]