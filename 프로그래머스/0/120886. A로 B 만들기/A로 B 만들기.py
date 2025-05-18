def solution(before, after):
    answer = 0
    count = set(before)
    
    if count != set(after):
        return 0
    
    for i in count:
        if before.count(i) != after.count(i):
            return 0
    return 1