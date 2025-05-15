def solution(lines):
    start = min(i[0] for i in lines)
    end = max(i[1] for i in lines)
    answer = 0

    for i in range(start, end+1):
        check_i = 0
        for j in lines:
            check_i += 1 if i >= j[0] and i < j[1] else 0
        
        answer += 1 if check_i >= 2 else 0
    return answer