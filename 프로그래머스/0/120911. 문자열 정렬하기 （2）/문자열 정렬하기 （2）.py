def solution(my_string):
    answer = ''.join(sorted(i.lower() for i in my_string))
    return answer