def solution(array, height):
    return len(list(filter(lambda x:x > height , array)))