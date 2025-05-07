def solution(my_string, num1, num2):
    a = list(my_string)
    a[num2], a[num1] = a[num1], a[num2]
    return ''.join(a)