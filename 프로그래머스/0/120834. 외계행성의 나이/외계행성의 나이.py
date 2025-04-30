def solution(age):
    answer = []
    age_dict = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 
                5:'f', 6:'g', 7:'h', 8:'i', 9:'j'}
    
    while age // 10 or age % 10 != 0:
        one = age % 10
        answer.append(age_dict[one])
        age = age // 10
    
    return ''.join(answer[::-1])