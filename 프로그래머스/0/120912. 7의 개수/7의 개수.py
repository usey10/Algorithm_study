def solution(array):
    count = 0
    for i in array:
        for j in str(i):
            if j == '7':
                count += 1
    return count