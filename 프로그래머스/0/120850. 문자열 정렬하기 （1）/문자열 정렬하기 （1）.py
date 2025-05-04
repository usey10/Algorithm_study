def solution(my_string):
    num = [f'{i}' for i in range(0,10)]
    answer = sorted(list(filter(lambda x:x in num, my_string)))
    return [int(i) for i in answer]