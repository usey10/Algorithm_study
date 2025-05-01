def solution(hp):
    a = hp // 5
    less = hp - (5*a)
    b = less // 3
    less -= b*3
    return a + b + less