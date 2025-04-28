def solution(num_list):
    a = list(filter(lambda x:x % 2 == 0, num_list))
    b = list(filter(lambda x:x % 2 == 1, num_list))
    return [len(a), len(b)]