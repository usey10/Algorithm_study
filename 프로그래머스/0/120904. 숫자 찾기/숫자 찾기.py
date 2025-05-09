def solution(num, k):
    for idx, i in enumerate(str(num)):
        if int(i) == k:
            return idx+1
    return -1