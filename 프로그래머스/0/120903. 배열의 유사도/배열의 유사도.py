def solution(s1, s2):
    count = 0
    a = s1 if len(s1) < len(s2) else s2
    b = s2 if a == s1 else s1
    for i in a:
        if i in b:
            count += 1
    return count