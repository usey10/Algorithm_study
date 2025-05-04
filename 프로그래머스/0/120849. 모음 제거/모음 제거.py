def solution(my_string):
    m = ['a','e','i','o','u']
    answer = ''.join(list(filter(lambda x: x not in m, my_string)))
    return answer